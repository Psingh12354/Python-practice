units=eval(input("Enter number of units use : "))
if units<=100:
    print("Bill = ",str(units*10))
elif units<=200:
    print("Bill = ",str((100 * 10) + (units - 100) * 15))
elif units<=300:
    print("Bill = ",str((100 * 10) + (100 * 15) + (units - 200) * 20))
elif units>300:
    print("Bill = ",str((100 * 10) + (100 * 15) + (100 * 20) + (units - 300) * 25))
