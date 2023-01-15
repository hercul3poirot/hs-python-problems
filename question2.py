import sys

def fact(x):
    if int(x) == 1:
        return 1
    else:
        return(int(x) * fact(x-1))

x = int(sys.stdin.readline())
print(fact(x))