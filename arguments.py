import sys
import os

def add(num1, num2):
    add = num1 + num2
    return add

def sub(num1, num2):
    s = num1 - num2
    return s

def mul(num1, num2):
    m = num1 * num2
    return m

num1 = int(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])

if operation == "add":
    output = add(num1, num2)
    print("addition of two numbers:", output)
elif operation == "sub":
    output = sub(num1, num2)
    print("subtraction of two numbers:", output)
else:
    output = mul(num1, num2)
    print("multiplication of two numbers:", output)

print("env variable:", os.getenv("course"))
