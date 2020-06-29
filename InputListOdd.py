values=input("Enter a list with comma in between them")
numbers=[x for x in values.split(",") if int(x)%2!=0]
print(",".join(numbers))
