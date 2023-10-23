## with open('acronym.txt') as file:
##    result = file.readlines()
##    for acronym in result:
##        print(acronym)
##      for line in file:
##        print(line)

look_up = input("what acronym would you like to lookup?\n") 

found = False
with open('acronym.txt') as file:
    for line in file:
        if look_up in line:
            print(line)
            found = True
            break

if  not found:
    print('acronym does not exist')


