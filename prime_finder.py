# A program to check whether the given number is prime or not
def primeFinder(n):
    if n > 1:
        for i in range(2, num):
            if num % i == 0:
                print("{0} is not a prime number\n".format(num))
                break
        else:
            print("{0} is a prime number\n".format(num))


num = int(input("Enter the number\n"))
primeFinder(num)
