class car():
    # args receives unlimited no. of arguments as an array
    def __init__(self, *args):
        # access args index like array does
        self.speed = args[0]
        self.color = args[1]
        self.gear = args[2]
 
 
# creating objects of car class
audi = car(200, 'red', 'manual')
bmw = car(250, 'black', 'automatic')
mb = car(190, 'white', 'manual')
 
print(audi.color)
print(bmw.speed)
print(mb.gear)