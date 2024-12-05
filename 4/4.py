contents = []
filename = "4/input.txt"
#filename = "4/testinput.txt"
with open(filename, "r") as file:
    for row in file:
        contents.append(row.replace("\n",""))

def findstring(string):
    stringamount = 0
    for row in range(0,len(contents)):
        for letter in range(0,len(contents[row])):
            if contents[row][letter] == string[0]:
                validdirections = getvaliddirections(string[1:],row,letter)
                for direction in validdirections: 
                    if validdirections[direction] == True:
                        if not findnextletter(string[1:],row,letter,direction) == None:
                            stringamount += findnextletter(string[1:],row,letter,direction)
    print(stringamount)

def findnextletter(string,row,letter,direction):
    match direction:
        case "E":
            nextrow = row
            nextletter = letter+1
            return cont_or_term(string,nextrow,nextletter,direction)
        case "S": 
            nextrow = row+1
            nextletter = letter
            return cont_or_term(string,nextrow,nextletter,direction)
        case "W": 
            nextrow = row
            nextletter = letter-1
            return cont_or_term(string,nextrow,nextletter,direction)
        case "N": 
            nextrow = row-1
            nextletter = letter
            return cont_or_term(string,nextrow,nextletter,direction)
        case "SE":
            nextrow = row+1
            nextletter = letter+1
            return cont_or_term(string,nextrow,nextletter,direction)
        case "SW": 
            nextrow = row+1
            nextletter = letter-1
            return cont_or_term(string,nextrow,nextletter,direction)
        case "NW": 
            nextrow = row-1
            nextletter = letter-1
            return cont_or_term(string,nextrow,nextletter,direction)
        case "NE": 
            nextrow = row-1
            nextletter = letter+1
            return cont_or_term(string,nextrow,nextletter,direction)

def cont_or_term(string,nextrow,nextletter,direction):
    if string[0] == contents[nextrow][nextletter]:
        if len(string) == 1:
            print(f"found XMAS ending at {nextrow},{nextletter} direction {direction}")
            return 1
        else:
            # print(f"{string[0]} found, looking for {string[1]} next from {direction} at {contents[nextrow][nextletter]}")
            return findnextletter(string[1:],nextrow,nextletter,direction)
    else:
        return 0

def getvaliddirections(remainingstring,row,letter):
    requirement = len(remainingstring)
    width = len(contents[0])-1
    height = len(contents)-1
    validdirections = { "E" : isvaliddirection(requirement,letter,width),
                        "S" : isvaliddirection(requirement,row,height),
                        "W" : isvaliddirection(requirement,letter,0),
                        "N" : isvaliddirection(requirement,row,0)
                    }
    validdirections["SE"] = validdirections["S"] and validdirections["E"]
    validdirections["SW"] = validdirections["S"] and validdirections["W"]
    validdirections["NW"] = validdirections["N"] and validdirections["W"]
    validdirections["NE"] = validdirections["N"] and validdirections["E"]
    return validdirections

def isvaliddirection(req,value,max):
    if abs(max-value) >= req:
        return True
    else:
        return False

findstring("XMAS")