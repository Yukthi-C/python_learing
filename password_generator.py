import random as ran

print("Random Password Generator!!!")
n = int(input("Enter the length of password to be generated\n"))
num = "1234567890"
alpa = "abcdefghigklmnopqrstuvwxyz"
calpa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sp = "*^!%@$&_"
p_s = num + alpa + calpa + sp
pws = "".join(ran.choices(p_s, weights=None, k=n))
print("Password generated:", pws)
