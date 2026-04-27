import ast

def make_ast():
  
    for_loop_code = """
for i in range(5):
    print(i)
"""

    generator_function_code = """
def generate_numbers():
    for i in range(5):
        yield i
"""

    complex_condition_code = """
x = 10

if x > 0 and x < 20:
    print("Valid")
else:
    print("Invalid")
"""

    complex_arithmetic_code = """
a = 5
b = 3
c = 10
d = 2

result = (a + b) * (c - d) / 2
"""

    print("1. for loop ")
    print(ast.dump(ast.parse(for_loop_code), indent=4))

    print("\n2. AST Generational function ")
    print(ast.dump(ast.parse(generator_function_code), indent=4))

    print("\n3. AST Complex conditional statement ")
    print(ast.dump(ast.parse(complex_condition_code), indent=4))

    print("\n4. AST Complex arithmetic operation ")
    print(ast.dump(ast.parse(complex_arithmetic_code), indent=4))

make_ast()