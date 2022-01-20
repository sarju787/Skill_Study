import msilib


def solution(myList):
    # write your code in Python 3.6
        
    myListtwo = []
    myListtree = []
    ans = []
    mySet = set()
    mySetTwo = set()


    l = len(myList)

    r1 = myList[0]
    r2 = myList[l-1]

    for i in range(r1, r2+1):
        myListtree.append(i)

    for i in myList:
        mySet.add(i)

    for i in mySet:
        myListtwo.append(i)

    myListtwo.sort()
    # print(myListtwo)
    # print(myListtree)

    for i in range(l):
        if i == None:
            break
        else:
            if myListtree[i]==myListtwo[i]:
                pass
            else:
                if (myListtree[i]<=0):
                    continue
                else:
                    ans.append(myListtree[i])
                    break

    if len(ans)==0:
        if r2 <= 0:
            print(1)
        else:
            print(r2+1)
    else:
        print(ans[0])
        pass

myList = []
n = int(input("enter number: "))

for i in range(n):
    Num = int(input("enter numer : "))
    myList.append(Num)
    myList.sort()

solution(myList)