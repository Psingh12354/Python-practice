units=float(input("Please enter Number of Units you Consumed : "))
if units<50:
    amounts=units*2.60
    surcharge=25
elif units<=100:
    amounts=130+((units-50)*3.25)
    surcharge=35
elif units<=200:
    amounts=130+162.50+((units-100)*5.26)
    surcharge=45
else:
    amounts=130+162.50+526+((units-200)*8.45)
    surcharge=75
total=amounts+surcharge
print("Total electricity Bill = ",total)
