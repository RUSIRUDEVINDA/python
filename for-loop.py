fruits = ["apple", "banana", "cherry"]

index = 0

for x in fruits:
  print(index,x)
  index +=1

for i in "banana":
 print(i)

x = ["car", "bike", "bus"]

for i in x:
  if i == "bus":
    break
  else:
    print(i)

for x in range(6):
  print(x)

for x in range(2, 6):
  print(x)

for x in range(2, 30, 3):
  print(x)

i = [3,6,9,12,15]
j = [4,8,12,16,20]

for x in i:
  for y in j:
    print(x,",",y)