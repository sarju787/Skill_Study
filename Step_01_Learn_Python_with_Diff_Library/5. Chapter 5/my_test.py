oxford = {
    "gift" : "yor are my brother.",
    "this" : "this is keyword in c++",
    "myList" : [1, 4, 5, "Sarju kathiriya"]
}

print(oxford)
dict_two = oxford.fromkeys("this", "sarju kathiriya")

print(type(dict_two))

set_one = {1,4,67,3}
set_two = {3,4,7,5}

set_three = set_one.intersection(set_two)
print(set_three)