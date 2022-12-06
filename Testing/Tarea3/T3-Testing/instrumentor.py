from ast import *
import threading
from multiprocessing.dummy import Array
import os

class Instrumentor(NodeTransformer):
    def __init__(self):
        super().__init__()

    def visit_FunctionDef(self, node: FunctionDef):
        transformedNode = NodeTransformer.generic_visit(self, node)
        injected_code = 'Profile.record(\''+ transformedNode.name+'\',['
        i = 0
        for arg in transformedNode.args.args:
            if i == 0:
                injected_code = injected_code + arg.arg
            else:
                injected_code = injected_code + ', '+ arg.arg
            i = i + 1
        injected_code = injected_code + '])'
        
        ast_to_inject = parse(injected_code)
        
        if isinstance(transformedNode.body, list):
            transformedNode.body.insert(0, ast_to_inject.body[0])
        else:
            transformedNode.body = [ast_to_inject.body[0], node.body]
        
        fix_missing_locations(transformedNode)
        
        return transformedNode

    def visit_Expr(self, node: Expr):
        profile = Profile.getInstance()
        if len(node.value.args) == 1 and isinstance(node.value.args[0], Constant):
                if node.value.func.id in profile.parameters:
                    if profile.parameters[node.value.func.id] != node.value.args[0].value:
                        del profile.parameters[node.value.func.id]
                else:
                    profile.parameters[node.value.func.id] = node.value.args[0].value
        
class Profile:
    __singleton_lock = threading.Lock()
    __singleton_instance = None
    @classmethod
    def getInstance(cls):
        if not cls.__singleton_instance:
            with cls.__singleton_lock:
                if not cls.__singleton_instance:
                    cls.__singleton_instance = cls()
        return cls.__singleton_instance

    @classmethod
    def reset(cls):
        cls.__singleton_instance = None

    @classmethod
    def record(cls, functionName, args):
        cls.getInstance().ins_record(cls, functionName, args)
    
    # instance method
    def __init__(self):
        self.functions_called=[]
        self.parameters={}

    def ins_record(self, cls, functionName, args): 
        self.functions_called.append(functionName)

    def printReport(self):
        print("\n-- cacheable functions --")
        for fun_key in self.parameters:
            print(fun_key)
        print()

def instrument(ast):
    visitor = Instrumentor()
    fixed_locations = fix_missing_locations(visitor.visit(ast))
    return fixed_locations