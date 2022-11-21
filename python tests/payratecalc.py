import math 

rate = float(input('Hourly Rate:'))
hours = int(input('Hours:'))
pay = rate * hours
overtime = int(input('Enter Overtime Hours:'))

if hours+overtime > 40:
    OT = ((rate * 2) * overtime)
    print('Your overtime is:', OT)
    print("Your pay is:",pay + OT)
else:
    print('You did not work any overtime, your pay is:', pay)
