# Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

def dicmaker():
    dicto = {}
    for i in range(1,21):
        dicto[i] = i*i 
    return dicto

print(dicmaker())