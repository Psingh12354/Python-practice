class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myFunct(self):
        print("Hello my name is " + self.name)
p1=Student('Priyanshu Singh',19)
p1.age=19
print(p1.age)
p1.myFunct()
