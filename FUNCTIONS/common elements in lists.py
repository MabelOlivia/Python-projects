a = [2, 4, 7, 9]
b = [4, 3, 2, 8]


'''for i in a:
    if i in b:
        z.append(i)'''

z = [ i for i in a if i in b]
print(z)

