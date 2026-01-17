x = [-12,-23,-567,-123,-88]
print(type(x))

total = 0

for i in x:
    total += i
print(total)
print(total/len(x))

max = x[0]
min = x[0]

for j in x:
    if max < j:
        max = j
    if min > j:
        min = j
        
print(max)
print(min)