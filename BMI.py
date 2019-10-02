# Cameron Matteoni
# 9-23-19
# BMI

weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in inches: "))

bmi = weight * 703 / height ** 2

if bmi < 18.5:
    print("BMI is ", format(bmi, ",.1f"))
    print("This is considered underweight.")
elif bmi > 25:
    print("BMI is ", format(bmi, ",.1f"))
    print("This is considered overweight.")
else:
    print("BMI is ", format(bmi, ",.1f"))
    print("This is considered optimal.")
