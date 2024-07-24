x1=[1,1,"app1","app1",10.8,True,"bye"]
print("list:::",type(x1))
print(x1)
for i in x1:
    print(i)
s=int(input("Enter a start range"))   
n=int(input("Enter a ends range"))    
for k in range(s,n):
    x1.append(k)
print("after adding dynamic elements::",x1)