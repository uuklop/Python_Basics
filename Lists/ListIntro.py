# Lists: Ordered,  mutable, allows duplicate elements
myList = ["banana", "cherry", "apple"]
print(myList)

myListTwo = [5, True, "apple", "apple"]
itemOne = myListTwo[-1]
print(itemOne)

#Iterating
for item in myListTwo:
    print(item)


#checking Item
if "banana" in myListTwo:
    print("yes")

else:
    print("no")


#Total Number of elements
print(len(myList))


#Addinng
myList.append("Lemon")
print(myList)

#Inserting Precision
myList.insert(1, "blueberry")
print(myList)

#remove last item
item =  myList.pop()
print(item)
print(myList)

#remove via value
item = myList.remove("cherry")
print(item)

#remove all elements
#myList.clear()

#reverse the list
myList.reverse()
print(myList)

myNumbers = [2,1,4,10,23,231,44,12,5]
sortedNumbers = sorted(myNumbers)

#or
myNumbers.sort()
print(myNumbers)
print(sortedNumbers)

