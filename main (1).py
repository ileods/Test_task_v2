import os

str = str(input())

with open("expression.py", "w") as file:
  file.write("print(" + str + ")")

os.system('python expression.py')