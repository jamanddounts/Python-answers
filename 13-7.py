def sub_func1():
    print('sub_func1 was called')

def sub_func2():
    print('sub_func2 was called')

#Define a function top_func that calls both sub_func1 and sub_func2 in that order
def top_func():
    sub_func1()
    sub_func2()
    
top_func()
