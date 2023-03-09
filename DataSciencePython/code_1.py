import ast
tuple1 = ast.literal_eval(input("Enter a tuple = "))
a = list(tuple1)
a.append("Python")
tuple1 = tuple(a)
print(tuple1)