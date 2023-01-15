import operator
ops = {"+": operator.add, "-": operator.sub}



def will_hit(eqn, coordinates):
    terms = eqn.split(" ")
    xcoeff = int(terms[2][:-1])
    operator = terms[3]
    const = int(terms[4])
    if operator == "+":
        if coordinates[1] == xcoeff*coordinates[0] + const:
            print("True")
        else:
            print("False")
    else:
        if coordinates[1] == xcoeff*coordinates[0] - const:
            print("True")
        else:
            print("False")

will_hit("y = 2x - 5", (0, 0))
will_hit("y = -4x + 6", (1, 2))
will_hit("y = 2x + 6", (3, 2))