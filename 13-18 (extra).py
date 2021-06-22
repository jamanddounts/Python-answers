#Define a function squared to receive an argument n and return the value of n squared
def squared(n):
    return n*n

n = int(input('integer:'))
print('%d squared:%d' % (n, squared(n)))
