'''Timer'''
import time

print("Seconds Timer...\n")


def timer(sec=0):
    print("\nTimer starts!!!\n")
    s = sec

    while s > 0:
        print("{0}:{1}".format(0, s))
        s -= 1
        time.sleep(1)
    print("\nTime out")


sec = int(input("Enter how many seconds\n"))

timer(sec)
