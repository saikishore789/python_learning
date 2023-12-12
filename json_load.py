import json

print("Started Reading JSON file")
with open("myfile.json", "r") as read_file:
    file = json.load(read_file)

    for key, value in file.items():
        print(key, ":", value)
    print("done reading json file")
