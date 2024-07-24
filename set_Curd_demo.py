s1={"apple"}
for x in range(10):
    print("1.adding Element")
    print("2.Deleting Element")
    print("3.display Elements")
    print("4.update the Given Element")
    print("5.unknown op")
    print("Enter your choice")
    n1=input("Enter your choice")

match n1:
    case "1":
     ele=input("Enter Ele ")
     s1.add(ele)
    case "2":
     ele2=input("Enter Ele for delete")
     s1.remove(ele2)

    case "3":
      for i in s1:
       print(i)

    case "4":
      l1=list(s1)
      n1=(input("Enter a index for updating ele "))
      upele=input("Enter a update Ele")
      l1[n1]=upele
      s1=set(l1)
    case "5":
     print("unknown op")

      