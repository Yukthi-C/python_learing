'''Unit Converter'''
print("Unit Converter Program\nThis Unit Converter will perform following conversions:\n")
print(
    "\t1.mm --> cm\n\t2.cm --> m\n\t3.m --> km\n\t4.cm --> mm\n\t5.m --> cm\n\t6.km --> m\n\t7.mm --> m\n\t8.m --> mm\n\t9.m --> km")
print("Note:It should follow the same order\n")
c = int(input("Enter the option nummber\n"))
unit = float(input("Enter the unit value:"))

# calculations
if c == 1:
    res = unit / 10
elif c == 2:
    res = unit / 100
elif c == 3:
    res = unit / 1000
elif c == 4:
    res = unit * 10
elif c == 5:
    res = unit * 100
elif c == 6:
    res = unit * 1000
elif c == 7:
    res = unit / 1000
elif c == 8:
    res = unit * 1000
else:
    res = unit / 1000

print("\n{0} is converted to {1}\n".format(unit, res))
