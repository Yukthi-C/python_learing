import random as ran

print("Random Password Generator!!!")
n = int(input("Enter the length of password to be generated\n"))
password = "1234567890abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ*^!%@$&_"
pws = "".join(ran.choices(password, weights=None, k=n))
print("Password generated:", pws)
