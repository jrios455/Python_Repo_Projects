import sys
import math

print('Welcome To The Fahrenheit Calculator')
opt = input('Please Choose Fahrenheit or Celsius:')
fahrenheit = 'fahrenheit'
celsius = 'celsius'

if opt == fahrenheit:
    fahrenheit = int(input('Please Enter a Numerical Value:'))
    celsius = round((fahrenheit - 32)/1.8,1)
    print('Celsius is:',celsius)

elif opt == celsius:
    celsius = int(input('Please Enter a Numerical Value:'))
    fahrenheit = round((celsius * 1.8) + 32,1)
    print('Fahrenheit is:', fahrenheit)

else:
    print('Please Choose Fahrenheit or Celsius')
