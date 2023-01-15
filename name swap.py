def name_shuffle(txt):
    forwards = txt.split(" ")
    forwards.reverse()
    backwards = forwards.join(" ")
    return backwards
