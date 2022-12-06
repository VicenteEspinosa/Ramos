from . rule import *

class SuspiciousVariableNameVisitor(WarningNodeVisitor):

    def visit_Name(self, node):
        if isinstance(node, Name) and len(node.id) == 1:
            self.addWarning('SuspiciousVariableNameWarning', node.lineno, 'variable ' + node.id + ' has a suspicious name.')
        NodeVisitor.generic_visit(self, node)

    def visit_Attribute(self, node):
        if len(node.attr) == 1:
            self.addWarning('SuspiciousVariableNameWarning', node.lineno, 'variable ' + node.value.id + "." +
                            node.attr +  ' has a suspicious name.')
        NodeVisitor.generic_visit(self, node)


class SuspiciousVariableNameRule(Rule):
    def analyze(self, ast):
        visitor = SuspiciousVariableNameVisitor()
        visitor.visit(ast)
        return visitor.warningsList()