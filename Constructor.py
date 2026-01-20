class Dog:
    # Constructor method
    def __init__(self, name):  # Constructor method is automatically create when we create the object, in here we use it using overloading
        self.name = name

    def set_name(self,name):
        self.name = name
            
    def bark(self,message):
        msg = f"This dog is named {self.name}.{message}"
        print(msg)

dog1 = Dog("scrappy")
dog1.bark("hey!!!")