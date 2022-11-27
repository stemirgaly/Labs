def Election(a,b,c):
    if(a==b==c or a==b or a==c):
        return a
    elif(b==c):
        return b
a,b,c=map(int,input().split())
print(Election(a,b,c))