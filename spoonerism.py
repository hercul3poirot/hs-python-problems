vowels = ["a","e","i","o","u"]
trivialwords = ["for", "has", "have", "she", "that", "the", "this", "will", "with"]
numberssymbols = "123456789!@#$%^&*()"

def vow(word):
    count = 0
    for i in word:
        if i in vowels:
            break
        else:
            count += 1
    return count 

line = input("Enter: ")
statement = []
fullstatement = []
prefixlist = []
choplist = []

for word in line.split(" "):
    if word not in trivialwords and len(word) > 2 and vow(word) != 0:
        statement.append(word)
        fullstatement.append("")
    else:
        fullstatement.append(word)
if len(fullstatement) > 1:
    for position,word in enumerate(statement):
        if word[0:1] == "qu":
            prefixlist.append("qu")
            choplist.append(word[-(len(word)-2):])
        else:
            prefixlist.append(word[0:vow(word)])
            choplist.append(word[-(len(word)-vow(word)):])
    for position,word in enumerate(statement):
        if word == statement[-1]:
            pass
        else:
            statement[position+1] = prefixlist[position] + choplist[position+1]
    statement[0] = prefixlist[-1] + choplist[0]
    addcount = 0 
    for position,word in enumerate(fullstatement):
        if word == "":
            fullstatement[position] = statement[addcount]
            addcount += 1
    print(" ".join(fullstatement))
elif line in numberssymbols:
    print("")
else:
    print(line)
    




        
