
def make_increment(n):
    return  lambda x: x + n

f = make_increment(3)
print(f(1))

x = lambda a, b : a**b
print(x(3,4))
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
print(type(pairs[0]))