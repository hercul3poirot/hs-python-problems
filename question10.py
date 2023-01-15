import sys 

nodupes = []
for word in sys.stdin.readline().strip().split(" "):
    if word not in nodupes:
        nodupes.append(word)
print(" ".join(sorted(nodupes))) 
