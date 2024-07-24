l1=[]
for x in range (5,20,2):
     l1.append(x)
print(l1)

t1=(x for x in range (0,20,2))
l2=list(t1)
print(l2)

t1=(x for x in range (0,20,2))
[*x1]=t1
print(l2)



