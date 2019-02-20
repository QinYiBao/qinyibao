N=966
s=0
for i in range(1,N+1):
    if i%2==0:
        s-=i
    else:
        s+=i
print (s)
