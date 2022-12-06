from ast import *

print(dump(parse("""\
def comer(cantidad):
  print("Comiendo", cantidad, "gramos")

comer(3)
comer(3)
comer(3)

beber(2)
"""), indent=4))