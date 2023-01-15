import sys
# def can_see_stage(people):
#     for row in people:
#         for person in row:
#             pass

# construction of the initial list
def can_see_stage(people): 
    temperlist = []
    for number, group in enumerate(people):
        i = 0 
        templist = []
        while i < len(people[number])-1:
            templist.append(people[i][number])
            i += 1
        temperlist.append(templist)

    # checking of each column of people     
    for templist in temperlist:
        for place, person in enumerate(templist):
            if place + 1 == len(templist):
                continue
            if person >= templist[place + 1]:
                print("False")
                sys.exit()
            else:
                continue
    return True
