class Cars:
    wheels=4 # class variable
    def __init__(self,brand,model):
        self.brand=brand # instance variable
        self.model=model # instance variable
        self.year=None # instance variable

car1=Cars("BMW","X5") #object of the class Cars
car2=Cars("Audi","Q7") #object of the class Cars

print(car1.wheels) #accessing class variable using object
print(car2.wheels) #accessing class variable using object

print(car1.brand) #accessing instance variable using object
print(car2.brand) #accessing instance variable using object


#__init___ init is a built in method which is used to initialize the instance variable when the object is created. It is also called constructor.

class Cars:
    wheels=4 # class variable
    def __init__(self,brand,model):
        self.brand=brand # instance variable
        self.model=model # instance variable
        self.year=None # instance variable

    def display(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
        print("Year:",self.year)
        print("-------------------")

car1=Cars("BMW","X5") #object of the class Cars
car2=Cars("Audi","Q7") #object of the class Cars
