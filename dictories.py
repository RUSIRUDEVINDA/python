x = {1:'A', 2:'B'}

y = x[1]
print(y)

y1 =x.get(2)
print(y1)

y2 =x.get(3,0)
print(y2)


x={'1000':'pilipinas', '1001':'america', '1002':'england'}
x[0] = 'canada'

x['country'] = {1:'english', 2:'french'}
print(x)

print(x.keys())
print(x.values())

del x['1000']
print(x)
del x['country'][2]
print(x)

x.clear()
print(x)