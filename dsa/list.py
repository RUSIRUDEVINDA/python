x = [12,40,66,79,10]
x.append(25)
x.append(30)

print(x, end="\n")

x.insert(2, 50)
print(x, end="\n")
x[3] = 100

print(x, end="\n")

x.remove(40)
print(x, end="\n")

x.pop(4)
print(x, end="\n")

z = [55,65,78,90]

k = x+z
print(k, end="\n")

is_in_10 = 10 in k
print(is_in_10)

is_in_99 = 99 not in k
print(is_in_99)
