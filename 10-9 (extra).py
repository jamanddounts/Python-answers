a =int(input("Input integer:"))
b = 1
factorial = 1
while b<=a:
    factorial = factorial * b
    b = b +1
print(factorial)

#as in 10-8 you could while factorial instead
#.... make sure to check your variable names, i accidentally caused an infinite loop cause i had a=a+1...
