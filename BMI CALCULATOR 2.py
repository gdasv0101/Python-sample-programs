print("BODY MASS INDEX CALCULATOR")
print(".......................................................................................")
print('\n Hello, this is a BMI Calculator!')
n=input("Enter your name :  ")#user should input his name
a = float(input("Enter Body mass (In Kg) :"))#a=weight in kg
b = float(input("Enter Body height (In m) :"))#b=height in m
BMI=a/(b**2)
if BMI<18.5:
    print(n,"is Underweight by",BMI,"BMI")
elif 18.6<= BMI <=24.9:
    print(n,"is Normal by",BMI,"BMI")
elif 25.0<= BMI <=30.9:
    print(n,"is overweight by",BMI,"BMI")
elif BMI>30:
    print(n,"is obese by",BMI,"BMI")
else:
     print(" wrong input")
#the calculations are done in float
