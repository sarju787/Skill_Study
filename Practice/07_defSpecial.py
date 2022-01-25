
from ast import arg


def std_pos(arg):
    print(arg)

def pos_only(arg, /):
    for argument in arg:
        print(argument)

def kwd_only(*, arg):
    print(arg)

def pos_kwd_only(p_arg, /, std, *, k_arg):
    print(p_arg)
    print(std)
    print(k_arg)


std_pos("hello")
pos_only("Position Argument")
kwd_only(arg="Sarju Kathiriya")