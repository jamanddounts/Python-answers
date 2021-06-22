a = input("Input string:")
if len(a) >= 5:
    a5 = True
else:
    a5 = False
print("No less than 5 characters?", a5)
if len(a) < 10:
    a10 = True
else:
    a10 = False
print("Less than 10 characters?", a10)
if a5 == True and a10 == True:
    a510 = True
else:
    a510 = False
print("No less than 5 characters and less than 10 characters?", a510)

#optionally you could have like "alength = len(a)" after the input and use alength instead of len(a)
#you can call the variables whatever btw
    
