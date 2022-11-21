import math

a = input("Enter a number:")

if int(a) >= 1 and int(a) <= 99:
    result1 = int(a[0]) + int(a[1])
    print(result1)
elif int(a) >= 100 and int(a) <= 999:
    result2 = int(a[0]) + int(a[1]) + int(a[2])
    print(result2)