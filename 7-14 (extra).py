height = float(input("Input your height:"))
weight = float(input("Input your weight:"))
bmi = weight/(height*height)
if bmi >=40:
    print("Your BMI Category is Obese Class III.")
elif bmi >=35:
    print("Your BMI Category is Obese Class II.")
elif bmi >=30:
    print("Your BMI Category is Obese Class I.")
elif bmi >=25:
    print("Your BMI Category is Overweight.")
elif bmi >=18.5:
    print("Your BMI Category is Normal.")
elif bmi >=17:
    print("Your BMI Category is Underweight.")
elif bmi >=16:
    print("Your BMI Category is Severely underweight.")
else:
    print("Your BMI Category is Very severely underweight.")
    
#alternatively you could:
if bmi >=40:
  bmi_category = "Obese Class III"
#etc for every category and then have only one print statement at the bottom (unindented)
print("Your BMI Category is", bmi_category)
#have not tested but it should work

#MAKE SURE TO CAPITALISE Category....
