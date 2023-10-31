my_list = [1, 2, 3, 4, 5]

number_to_check = int(input("enter a number to check:\n"))

result = number_to_check in my_list

if result == True:
    print("entered number is in the list")
else:
    print("entered number is not in the list")
