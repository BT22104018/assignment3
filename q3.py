myList = []
print("Enter 5 integers:")
for i in range(0,5):
    ele = int(input())
    myList.append(ele)

myListNew = []
for item in myList:
    value = item
    square = item**2
    tup = (value,square)
    myListNew.append(tup)
print(myListNew)