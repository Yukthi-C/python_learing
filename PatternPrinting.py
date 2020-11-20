# To print the * pattern
print('Triangle pattern\n')
n = int(input('Enter the number of lines : '))

for i in range(0, n, +1):
    print(i * '' + (n - i) * '*')
