t1=(10,20,30,50) # it;s packing
[a,b,c,d]=t1     # it's unpacking
print("a:::",a)
print("b:::",b)
print("c:::",c)
print("d:::",d)
t2=("hello","suma","ravi","kavitha","bye")
[x1,x2,*x3]=t2
print("x1:::",x1)
print("x2:::",x2)
print("x3:::",x3)
t3=("hello","suma","ravi","kavitha","bye")
[y1,*y2,y3]=t3
print("y1:::",y1,":::",y2,":::",y3)
