import random

print("Welcome to Number Guessing Game!!!\n")
print("Get ready....\n\n")
print("You'll be having 3 chances for guessing the correct number \n")
r=random.randint(1,50)
ch=1
while ch<=3:
    print("\n",ch,"st chance")
    b=int(input("Enter the Number:"))
    if b==r:
        print("\033[1;32;40m Congratulation!!! You won :)\n\033[1;37;40m")
        break
    elif b>r:
        print("Your guess is higher")
    else:
        print("Your guess is lower")
    ch+=1
if not ch<4:
    print("\033[1;31;40m Sorry :( you lost\n\033[1;37;40m")
    