# Lists: Ordered,  mutable, allows duplicate elements
from numba.cpython.listobj import list_copy

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


# Generating Lists
generatedLists = ["James"] * 10
print(generatedLists)


#Concatinating Lists
numList = [1,2,3,4,5]
new_list = myNumbers + numList
print(new_list)

#Slicing
myListAgain = [1,2,3,4,5,6,7,8,9]

# [start:stop]
a =  myListAgain[3:4]
ab = myListAgain[:5]
ac = myListAgain[2:]
print(a)
print(ab)
print(ac)

# Step 1
step = myListAgain[::-1]
print(step)

# Copying List from Existing Lists

list_org =  ["banana", "cherry", "apple"]


#list_copy = list_org
#list_copy = list_org.copy()
#list_copy = list(list_org)
list_copy = list_org[:]

list_copy.append("lemon")

print(list_copy)
print(list_org)


#ListComprehension
anumber = [1,2,3,4,5,6]
asquared = [i*i for i in anumber]

print(anumber)
print(asquared)
