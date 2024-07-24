a  =True
b  =False
type(a)
type(b)
print(type(a))
print(type(b))
print(True and True) # True
print(True and False) # False
print(not  True) # False
print(bool([])) # False
print(bool("")) # False
print([10,20,40]) # True


def f1():
     return True
def f2():
     return False

print(f1()and f2())
print(f1()or f2())
print(not f1())