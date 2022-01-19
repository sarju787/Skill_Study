from queue import PriorityQueue
from re import T
from traceback import print_tb


a = 2
b = "hi"
c = False

myList = [a,b,c]
print(myList)
print(type(myList))
print(type(myList[0]))
print(type(myList[1]))
print(type(myList[2]))

print(myList.append("Sarju"))
print(myList)

myListTwo = myList.copy()
print(myListTwo)
myListTwo.reverse()
print(myListTwo)
myListTwo.remove("Sarju")
print(myListTwo)
myListTwo.pop(1)
print(myListTwo)
myListTwo.insert(0, "Sarju Kathiriya")
print(myListTwo)

myTuple = (1,3,4,"sarju")
print(myTuple)
print(type(myTuple))
print(type(myTuple[0]))

mytupleTwo = tuple()
print(mytupleTwo)