# Define the function of trapezoid_area that will receive the three arguments for upper base, lower base, and height and return the area of the trapezoid 
def trapezoid_area(j, k, t):
    return (j+k)*t*0.5

j = int(input('upper base:'))
k = int(input('lower base:'))
t = int(input('height:'))
result = trapezoid_area(j, k, t)
print('Area of trapezoid with upper base %d, lower base %d, height %d: %f' % (j, k, t, result))

#this works too
def trapezoid_area(j, k, t):
    return ((j+k)/2)*t
