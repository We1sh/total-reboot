n = int(input())
m = 0
a = len(str(n))
for i in range(a):
    m = m*10 + n%10
    n = n//10
print(m)