score = int(input("Input score:"))
if score <0 or score >100:
    print("Please input the correct score.")
elif score >= 90:
    print("Superb")
elif score >= 80:
    print("Excellent")
elif score >= 70:
    print("Good")
elif score >= 60:
    print("Pass")
else:
    print("Fail")
    
#technically you could do ">=80 and <90" etc but because python tries every elif statement in order it's not neccssary
