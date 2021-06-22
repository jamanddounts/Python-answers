# Prompt the user to enter a number
# Define a function `convert_to_old_roman_numeral` that accepts the entered number as an argument
# If the argument passed is a number between 1 and 10, then its corresponding old roman numeral, as a string, is set as the return value
# If the input value is out of the range of the function,
# Then the string, “A number entered is out of range” is set as the return value
n = int(input('integer:'))
def convert_to_old_roman_numeral(n):
    if n==1:
        print("I")
    elif n==2:
        print("II")
    elif n==3:
        print("III")       
    elif n==4:
        print("IIII")      
    elif n==5:
        print("V")    
    elif n==6:
        print("VI")
    elif n==7:
        print("VII")    
    elif n==8:
        print("VIII")    
    elif n==9:
        print("VIIII")    
    elif n==10:
        print("X")
    else:
        print("A number entered is out of range")
        
# This is where the function convert_to_old_roman_numeral should be used and
# n should be converted to the old Roman numerals and its results should be printed
convert_to_old_roman_numeral(n)

#why did they say "return" when using return doesn't work? we will never know...
#that said using this many elif statements is considered really bad practice...
#anyways congrats that's the last exercise!!!
