a=int(input())
b=[int(j) for j in input().split()]
for element in b:
    if element%2==0:
        print(element)
for element in b:
    if element%2!=0:
        print(element)