class Dog:
    def set_name(self, name):
        self.name = name
    def bark(self,message):
        msg = f"This dog is named {self.name}.{message}"
        print(msg)

dog1 = Dog()

dog1.set_name("Scamper")
dog1.bark("hey!!!")

dog2 = Dog()

dog2.bark("hello")
