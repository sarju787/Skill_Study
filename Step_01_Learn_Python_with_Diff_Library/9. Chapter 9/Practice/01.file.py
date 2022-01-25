


# from math import log2


# s = "abcdefg"

# print(s[::-1])

# l = [1,3,4]

# l2= list(l)


# print(l)
# print(l2)

# l[1] = 66
# l2[2] = [1,4,5]
# l2[0] = str(l2[0]) + "hello"
# print(l)
# print(l2)
# print(l)

# a = 1
# b = 4

# a,b = b, a

# print(type(a))
# print(type(b))


# def fn(a, b):
#     return max(a,b), min(a,b)

# a ,b = fn(10, 70)

# print(a)
# print(b)

l = [20,68,77,2,6,6]


def sort_one(l):
    
    print(l)
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    
    print(l)

sort_one(l)
