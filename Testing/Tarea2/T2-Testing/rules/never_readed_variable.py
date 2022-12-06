from . rule import *

class UnusedVariableNameVisitor(WarningNodeVisitor):
    def __init__(self):
      super().__init__()
      self.visited_dictionary = {}

    def visit_Assign(self, node):
      if isinstance(node, Assign):
        if isinstance(node.targets[0], Name):
          self.visited_dictionary[node.targets[0].id] = [0, node.lineno]
      NodeVisitor.generic_visit(self, node)

    def visit_Name(self, node):
        if isinstance(node, Name):
          if node.id in self.visited_dictionary:
            if self.visited_dictionary[node.id][0] == 0:
              self.visited_dictionary[node.id][0] = 1
            else:
              del self.visited_dictionary[node.id]
        NodeVisitor.generic_visit(self, node)

    def setWarnings(self):
      for key in self.visited_dictionary:
          self.addWarning('NeverReadedVariable', self.visited_dictionary[key][1], 'variable "' + key + '" is unused.')


class SuspiciousVariableNameRule(Rule):
    def analyze(self, ast):
        visitor = UnusedVariableNameVisitor()
        visitor.visit(ast)
        visitor.setWarnings()
        return visitor.warningsList()