keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# The zip() function and a dict() constructor
dictionary = dict(zip(keys, values))

print(dictionary)

# Using a loop and update() method of a dictionary
res_dict = dict()

for i in range(len(keys)):
    res_dict.update({keys[i]: values[i]})

print(res_dict)