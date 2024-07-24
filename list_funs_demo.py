l1=[50,30,10,20,5]
l2=[70,34]
l1.extend(l2)
print("after adding :::",l1)

l1.pop()
print("after calling pop:::",l1)
l1.remove(50)
print("after calling remove :::",l1)

l1.sort()
print("after calling sort asceding order::",l1)

l1.sort(reverse=True)
print("after calling sort descending order::",l1)

print()