def fancy_generator():
    my_list = [1, 2, 3]
    for i in my_list:
        yield i * 2
mygen = fancy_generator()

print(mygen)
next(mygen)
next(mygen)
next(mygen)


for x in fancy_generator():
    print(x)



