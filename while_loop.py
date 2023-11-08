sum = 0
num = 2 

while(num<=20):
    sum = num + sum
    num = num + 2

print("sum of first 10 natural numbers:", sum)

print("-------")

num1 = int(input("enter a number:\n"))
k = 0
if num1 == 0 or num1 == 1:
    print(num1, "is not a prime number")

i = 2
while(i<num1):
    if num1 % i == 0:
        k = k + 1
    i = i + 1

if k == 0:
    print(num1, "is a prime number")
else:
    print(num1, "is not a prime number")
