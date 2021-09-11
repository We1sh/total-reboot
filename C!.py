for i in range(5):
    (a, b, c)=[int(s) for s in input().split()]
    if 0<=a<=23 and 0<=b<=60 and 0<=c<=60:
        print("YES")
    else:
        print("NO")