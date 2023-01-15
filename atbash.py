import sys

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
reverse = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

def atbash(word):
    atbashed = []
    for character in word:
        if character.lower() in alphabet:
            if character.isupper():
                atbashed.append(reverse[alphabet.index(character.lower())].upper())
            else:
                atbashed.append(reverse[alphabet.index(character)])
        else:
            atbashed.append(character)
    return "".join(atbashed)

print(atbash("Hello World!"))