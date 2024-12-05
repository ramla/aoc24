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

print(str(sum(map(diff, leftsorted, rightsorted))))