class Dog:
  name = ""
  breed: str = ""

  def walking(self):
     print("walking...", self)

dog1 = Dog()
dog1.walking()

Dog.walking(dog1)