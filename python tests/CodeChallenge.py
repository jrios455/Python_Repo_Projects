import math

print("Odd or Even Calculator")

opt = input("Enter a number:")
result = int(opt) % 2


if result == 0:
    print("This number is even")
elif result > .01:
    print("This number is odd")

