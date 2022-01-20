# # from cgi import print_environ
# # from re import I

# # from pyrsistent import ny


# # a = 0

# # while (a<10):
# #     print(a)
# #     a += 1

# from ast import Break


# myList = ["sarju", "raj", "Darshan"]

# # i = 0

# # while (i < len(myList)):
# #     print(myList[i])
# #     i += 1

# for i in myList:
#     for j in range(9):
#         if i == "sarju" or i == "Darshan":
#             print(i)
#             print("hello")
#             continue
#     else:
#         print("end of loop")

from re import I
from secrets import randbelow
from xml.sax.xmlreader import InputSource


n = int (input("Enter number"))

for i in range(1, n+1):
    print("*" * i, end="")
    print("\n", end="")

for i in range(0, n):
    print(" " * (n-i-1), end="")
    print("*" * (2*i + 1), end="")
    print(" " * (n-i-1))

for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for j in range((2*i)-1):
        print("*", end="")
    for j in range(n-i):
        print(" ", end="")
    print("\n", end="")

for i in range(n):
    for j in range(n):
        if (i==0 or j==0 or i==(n-1) or j==(n-1)):
            print("* ",end="")
        else:
            print("  ",end="")
    print("\n", end="")

for i in range(10):
    print(f"{n}X{i+1}={n*(i+1)}")
