
def inch2cm(n):
    return (n*2.54)

# print(inch2cm(2))

def process(l, word):
    word = word.strip()
    l.remove(word)

    return l

l1 = [' sarju', 'kirti', 'ramesh']
l1 = process(l1, " sarju     ")
print(l1)


