# Define `print_addition_result` function to receive two integers as arguments and print the result of their addition
def print_addition_result(a,b):
    c = a + b
    print('%s+%s=%s' %(a,b,c))
    
print_addition_result(1, 2)
print_addition_result(4, 5)

#why 3 %s?
#it's really picky about the spaces between the symbols and that's the easiest way to get rid of them

#you could do this instead too
def print_addition_result(a,b):
    print('%s+%s=%s' %(a,b,a+b))
    
#might be worth using different variable names? don't really think it matters    
