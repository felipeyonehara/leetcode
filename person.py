class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
print("address of object:",id(p1))

class check:
    def __init__(self):
        print("Address of self=",id(self))

obj = check()
print("address of object:",id(obj))