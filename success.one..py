x=[1,2,3]
y=0
for a in range(len(x)):
    b=str(x.pop(a))
    x.insert(a,int(b))
    for c in range(len(x)):
        v=str(x.pop(c))
        x.insert(c,int(v))
        for n in range(len(x)):
            m=str(x.pop(n))
            x.insert(n,int(m))
            y+=1
            print(b+v+m)
print("y=",y)
    