from . rewriter import *


class IfWithoutElseTransformer(NodeTransformer):
    def visit_If(self, node):
        if node.orelse:
            if isinstance(node.orelse[0], Pass):
                node.orelse = None
        return node


class IfWithoutElseRewriterCommand(RewriterCommand):
    def apply(self, ast):
        new_tree = fix_missing_locations(IfWithoutElseTransformer().visit(ast))
        return new_tree