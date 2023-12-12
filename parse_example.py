import parser
print("Input expression for parser module")
expression = "2 + 2"
print(" parsing the input expression")
parsing = parser.expr(expression)
print(parsing)
print(" Converting parsed object to code object")
code = parsing.compile()
print(code)
print(" Parsed result: ")
res = eval(code)
print(res)
