from . rule import *

class DataClassVisitor(WarningNodeVisitor):
  
    def __init__(self):
      super().__init__()
      self.classes = []
      
    def visit_ClassDef(self, node):
      isDataClass = True
      if isinstance(node, ClassDef):
        for function in node.body:
          if isinstance(function, FunctionDef):
              for line in function.body:
                if not (isinstance(line, Assign) or isinstance(line, Return) or isinstance(line, Pass) or isinstance(line, Expr)):
                  isDataClass = False
                  break
      if isDataClass:
        self.addWarning('DataClass', node.lineno, 'class ' + node.name + ' is a DataClass.')

class DataClassNameRule(Rule):
    def analyze(self, ast):
        visitor = DataClassVisitor()
        visitor.visit(ast)
        return visitor.warningsList()