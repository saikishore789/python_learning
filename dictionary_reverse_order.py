def sort_dict_by_key(d, reverse = False):
    return dict(sorted(d.items(), reverse=reverse))

students = { 'name2': 'sai', 'name1': 'mouni', 'name4': 'avi', 'name3': 'hyma' }

print("original dictionary:")
print(students)

print("\nSort the said dictionary by key (Ascending order):")
print(sort_dict_by_key(students))

print("\nSort the said dictionary by key (Descending order):")
print(sort_dict_by_key(students, True))