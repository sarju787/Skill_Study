
def is_ok(prompt, retries=4, reminder="Please try again"):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('no', 'n','nope'):
            return False
        retries -=1
        if retries<0:
            raise ValueError("Invalid user input")
        print(reminder)

is_ok("do y really want to quit?")

def f(a, l=[]):
    l.append(a)
    return l
def fone(a, l=None):
    if l == None:
        l = []
    l.append(a)
    return l

print(fone(1,[1,2]))
print(fone(2))
print(fone(3))

print(f(1))
print(f(2))
print(f(3))