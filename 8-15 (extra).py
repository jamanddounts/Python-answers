a = int(input("Input integer:"))
lista = list(range(0,a+1))
print(len(lista))
if 10 in lista:
    print("True")
else:
    print("False")
lista.append(5)
lista.insert(0,10)
lista.remove(0)
print(lista)

#theres probs a better way of doing this
#i guess you can swap line 9 and 10 around? 
# .replace() wasnt recognised :(
