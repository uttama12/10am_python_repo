t1=(10,20,30,True,"hello",10.5,10,10)
t2=21,22,34
t3=()
t4=(31,)
t5=t1 + t2 + t3 + t4
print("after adding objs :::",t5)
print("1 inde value:::",t5[0])
print("-1 inde value:::",t5[-1])
print("slice :::",t5[1:5]) # 5 index not included
print("slice ::",t5[1:])     
print ("slice ::",t5[:3])    # 3 index not inclded
print ("slice ::",t5[3:])


for x in t5:
    print (x)


l1=list(t5)
l1[0]=45
print("after updating 0 the element :::",l1)
l1.pop()
print("after removing  the last element :::",l1)
l1.remove(30)
print("after removing  the 30th element :::",l1)


