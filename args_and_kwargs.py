def ex(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)
 
 
# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ("args", "kwargs", "examples")
ex(*args)
 
kwargs = {"arg1": "sai", "arg2": "kishore", "arg3": "reddy"}
ex(**kwargs)


def myFun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)
 
 
# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun('args', 'for', 'kwargs', first="args", mid="for", last="kwargs")