num = int(input("enter any number: \n"))

flag = False

if (num == 1):
    print(f"{num} is not a prime number")
elif (num > 1):
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

if flag:
    print(f"{num}, is not prime number")
else:
    print(f"{num}, is  prime number")
