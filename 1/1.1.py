import numpy

#infile = "1/testinput.txt"
infile = "1/input.txt"
leftlist = []
rightlist = []

with open(infile, "r") as file:
    for row in file:
        entry = row.split("  ")
        leftlist.append(int(entry[0]))
        rightlist.append(int(entry[1]))

leftsorted = sorted(leftlist)
rightsorted = sorted(rightlist)

def diff(left, right):
    d = left - right
    if d >= 0:
        return d
    else:
        return -d

def similarityscore(left, right):
    final = 0
    for value in left:
        n = 0
        for element in right:
            if element == value:
                n += 1
        final += value * n
    return final

answer2 = similarityscore(leftsorted, rightsorted)
print(answer2)
#answer1 = str(sum(map(diff, leftsorted, rightsorted)))
