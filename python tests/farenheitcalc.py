print('Welcome To The Fahrenheit Calculator')

fahrenheit = input('Fahrenheit:')

try:
    fahrenheit = int(fahrenheit)
    celsius = (fahrenheit - 32)/1.8
    print('Celsius:',celsius)
except:
    print('Please enter a number')
    
