n = int(input("Input number of seconds:"))
hours = n//3600
minutes = (n%3600)//60
seconds = (n%3600)%60
print(hours,"hours",minutes,"minutes",seconds,"seconds")
