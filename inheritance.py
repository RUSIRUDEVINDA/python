class Animal:
    def __init__(self,breed):
        print("hello this is Animal class")
        self.breed = breed 

    def talk(self):
        print("Animal is talking")

    def move(self):
        print("Animal is moving")

class Dog(Animal):
    def __init__(self, name="unknown"):
        super(Dog, self).__init__("jermanshepherd")
        print("hello this is dog class")
        self.name = name

    def set_name(self,name):
        self.name = name

    def bark(self,message):
        msg = "This dog is named" + self.name + "." + message
        print(msg)  

    def walking(self):
        print("walking....")

dog1 = Dog()

dog1.talk()
print(dog1.breed)