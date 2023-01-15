import sys 

def binaryconverter(number):
    numlist = []
    i = 1
    for digit in number:
        numlist.append(int(digit))
    for position, number in enumerate(numlist):
        numlist[position] = number * (2**(len(numlist)-i))
        i += 1
    return sum(numlist)

propernumbers = [x for x in sys.stdin.readline().strip().split(",") if binaryconverter(x) % 5 == 0]
print(",".join(propernumbers))


