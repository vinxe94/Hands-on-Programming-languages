# AST.py Evaluation

This README explains how `AST.py` constructs its output line by line. The program uses Python's built-in `ast` module to convert small Python code examples into Abstract Syntax Tree (AST) representations, then prints those trees.

## How to Run

```bash
python3 AST.py
```

## Line-by-Line Evaluation

### Line 1

```python
import ast
```

This imports Python's `ast` module. The `ast` module can parse Python source code and represent it as a tree of nodes.

### Line 3

```python
def make_ast():
```

This defines a function named `make_ast`. All code examples and output printing are placed inside this function.

### Lines 5-8

```python
for_loop_code = """
for i in range(5):
    print(i)
"""
```

This stores a Python `for` loop as a multiline string. The code loops through numbers from `0` to `4` and prints each value.

When parsed, this becomes an AST with the following important parts:

- `Module` is the root node that contains the whole parsed code.
- `For` represents the loop statement `for i in range(5):`.
- `Name(id='i', ctx=Store())` shows that `i` is the loop variable receiving values.
- `Call(func=Name(id='range'))` represents the function call `range(5)`.
- `Expr` contains the `print(i)` call that runs inside the loop.

### Lines 10-14

```python
generator_function_code = """
def generate_numbers():
    for i in range(5):
        yield i
"""
```

This stores a generator function as a multiline string. The function contains a `for` loop and uses `yield` to return values one at a time.

When parsed, this becomes an AST with the following important parts:

- `Module` is the root node that contains the function definition.
- `FunctionDef` represents the function named `generate_numbers`.
- `arguments` shows that the function does not accept parameters.
- `For` represents the loop inside the generator function.
- `Yield` represents `yield i`, which produces one value at a time.

### Lines 16-23

```python
complex_condition_code = """
x = 10

if x > 0 and x < 20:
    print("Valid")
else:
    print("Invalid")
"""
```

This stores a conditional statement as a multiline string. It first assigns `10` to `x`, then checks if `x` is greater than `0` and less than `20`.

When parsed, this becomes an AST with the following important parts:

- `Assign` represents assigning the value `10` to `x`.
- `If` represents the whole conditional statement.
- `BoolOp(op=And())` represents the combined `and` condition.
- The first `Compare` node represents `x > 0`.
- The second `Compare` node represents `x < 20`.
- The `print("Valid")` call is stored in the `body` for the true case.
- The `print("Invalid")` call is stored in the `orelse` for the false case.

### Lines 25-32

```python
complex_arithmetic_code = """
a = 5
b = 3
c = 10
d = 2

result = (a + b) * (c - d) / 2
"""
```

This stores several assignments and one arithmetic expression as a multiline string.

When parsed, this becomes an AST with the following important parts:

- Four `Assign` nodes represent the values given to `a`, `b`, `c`, and `d`.
- One `Assign` node represents storing the final answer in `result`.
- Nested `BinOp` nodes represent the arithmetic operations inside the expression.
- `a + b` becomes a `BinOp` with the `Add()` operator.
- `c - d` becomes a `BinOp` with the `Sub()` operator.
- `(a + b) * (c - d)` becomes a `BinOp` with the `Mult()` operator.
- The final `/ 2` becomes a `BinOp` with the `Div()` operator.

### Lines 34-35

```python
print("1. for loop ")
print(ast.dump(ast.parse(for_loop_code), indent=4))
```

Line 34 prints the title for the first output section.

Line 35 constructs the first AST output:

1. `ast.parse(for_loop_code)` reads the string stored in `for_loop_code`.
2. Python converts that source code into an AST.
3. `ast.dump(..., indent=4)` converts the AST object into a readable string.
4. `print(...)` displays the formatted AST in the terminal.

### Lines 37-38

```python
print("\n2. AST Generational function ")
print(ast.dump(ast.parse(generator_function_code), indent=4))
```

Line 37 prints a blank line first because of `\n`, then prints the title for the generator function section.

Line 38 constructs the second AST output:

1. `ast.parse(generator_function_code)` parses the generator function string.
2. The parser creates a `Module` node containing a `FunctionDef` node.
3. The function body contains a `For` node.
4. The loop body contains a `Yield` node.
5. `ast.dump(..., indent=4)` formats the tree.
6. `print(...)` displays the formatted AST.

### Lines 40-41

```python
print("\n3. AST Complex conditional statement ")
print(ast.dump(ast.parse(complex_condition_code), indent=4))
```

Line 40 prints a blank line and the title for the conditional statement section.

Line 41 constructs the third AST output:

1. `ast.parse(complex_condition_code)` parses the assignment and `if` statement.
2. The assignment `x = 10` becomes an `Assign` node.
3. The `if` statement becomes an `If` node.
4. The condition `x > 0 and x < 20` becomes a `BoolOp` node using `And`.
5. Each comparison becomes a `Compare` node.
6. The `if` and `else` print statements become `Call` nodes inside `Expr` nodes.
7. `ast.dump(..., indent=4)` formats the AST.
8. `print(...)` displays it.

### Lines 43-44

```python
print("\n4. AST Complex arithmetic operation ")
print(ast.dump(ast.parse(complex_arithmetic_code), indent=4))
```

Line 43 prints a blank line and the title for the arithmetic section.

Line 44 constructs the fourth AST output:

1. `ast.parse(complex_arithmetic_code)` parses all assignment statements.
2. The assignments to `a`, `b`, `c`, and `d` each become an `Assign` node.
3. The assignment to `result` also becomes an `Assign` node.
4. The expression `(a + b) * (c - d) / 2` is broken into nested `BinOp` nodes.
5. The operators are represented by `Add`, `Sub`, `Mult`, and `Div` nodes.
6. `ast.dump(..., indent=4)` formats the complete tree.
7. `print(...)` displays the result.

### Line 46

```python
make_ast()
```

This calls the `make_ast` function. Without this line, the function would only be defined, but none of the AST examples would be parsed or printed.

## How the Output Is Constructed

Each output section follows the same pattern:

```python
print(ast.dump(ast.parse(code_string), indent=4))
```

The construction happens from the inside outward:

1. `code_string` contains Python code written as text.
2. `ast.parse(code_string)` converts that text into an AST object.
3. The root of the parsed tree is always a `Module` node.
4. The `body` list inside `Module` contains the statements from the code string.
5. Each statement is represented by a node such as `For`, `FunctionDef`, `Assign`, or `If`.
6. Expressions inside statements are represented by nodes such as `Call`, `Name`, `Constant`, `BoolOp`, `Compare`, `Yield`, or `BinOp`.
7. `ast.dump(..., indent=4)` turns the AST object into readable text with indentation.
8. `print(...)` sends the readable AST text to the terminal.

## Summary of the Four AST Outputs

| Output Section                         | Source Code Example                   | Main AST Nodes                                           |
| -------------------------------------- | ------------------------------------- | -------------------------------------------------------- |
| `1. for loop`                          | `for i in range(5): print(i)`         | `Module`, `For`, `Call`, `Name`, `Constant`              |
| `2. AST Generational function`         | `def generate_numbers(): ... yield i` | `Module`, `FunctionDef`, `arguments`, `For`, `Yield`     |
| `3. AST Complex conditional statement` | `x = 10`, `if x > 0 and x < 20`       | `Module`, `Assign`, `If`, `BoolOp`, `Compare`, `Call`    |
| `4. AST Complex arithmetic operation`  | `result = (a + b) * (c - d) / 2`      | `Module`, `Assign`, `BinOp`, `Add`, `Sub`, `Mult`, `Div` |
