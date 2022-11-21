height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
result =  round(weight / (height * height))

if result == 18.5:
    print("Your BMI is", result,",You are underweight")
elif result > 18.5 and result < 25:
    print("Your BMi is", result,",You have a normal weight")
elif result > 25 and result < 30:
    print("Your BMI is", result,",You are slightly overweight")
elif result > 30  and result < 35:
    print("Your BMI is", result,",You are obese")
elif result > 35:
    print("Your BMI is", result,",You should change your diet now")
