from . rewriter import *


class PlusPlusTransformer(NodeTransformer):
    def visit_Assign(self, node):
        if isinstance(node.value, BinOp):
            if node.targets[0].id == node.value.left.id:
                return [AugAssign(
                    target=Name(id=node.targets[0].id, ctx=Store()),
                    op=Add(),
                    value=node.value.right)]
        return node


class PlusPlusRewriterCommand(RewriterCommand):
    def apply(self, ast):
        new_tree = fix_missing_locations(PlusPlusTransformer().visit(ast))
        return new_tree