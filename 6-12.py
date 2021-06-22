n = int(input("Input integer:"))
if n%2 == 0:
    n2 = True
else:
    n2= False
print("multiple of 2?", n2)
if n%3 == 0:
    n3 = True
else:
    n3= False
print("multiple of 3?", n3)
if n2==True and n3==True:
    n23 = True
else:
    n23 = False
print("multiple of 2 and 3?",n23)

#there is probably a better way of doing this tho...
