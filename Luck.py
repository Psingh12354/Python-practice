import random
Name=input("Enter the name : ")
n=int(input("Enter the number between 1 to 10 : "))
if n == random.randrange(1, 10):
    print("Hello! {name}, you are lucky today...".format(name=Name))
else:
    print("Oops {name}, you are not lucky...".format(name=Name))
