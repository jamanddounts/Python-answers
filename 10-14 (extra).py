n = int(input("Input integer:"))
total = 0
a = 1
while a<=n:
    if a%2==1:
        total = total + a
        a = a+1
    else:
        a=a+1
print("Sum of odd numbers from 1 to input value",total)

#FUCK THIS STUPID EXERCISE
#i accidentally did it for even numbers... it took me so long to realise...
#also continue is so useless, it skips back to the beginning

#you dont need the else section btw
while a<=n:
    if a%2==1:
        total = total + a
    a = a+1
print("Sum of odd numbers from 1 to input value",total)
#works too
