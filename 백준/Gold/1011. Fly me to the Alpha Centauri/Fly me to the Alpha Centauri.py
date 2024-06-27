T=int(input())
for i in range(T):
    x, y=map(int,input().split())
    d=y-x
    n=1
    while d>n**2:
        n+=1
    n-=1
    if d<=n**2+n:
        print(2*n)
    else:
        print(2*n+1)