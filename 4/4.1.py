contents = []
filename = "4/input.txt"
#filename = "4/testinput.txt"
with open(filename, "r") as file:
    for row in file:
        contents.append(row.replace("\n",""))

def findx3string(string): #only 3 long string
    stringamount = 0
    for row in range(1,len(contents)-1):
        for letter in range(1,len(contents[row])-1):
            if contents[row][letter] == string[1]:
                stringamount += findx3letters(string,row,letter)
    print(stringamount)
                
def findx3letters(string,row,letter):
    if findx3nwse(string[0],string[2],row,letter) and findx3nesw(string[0],string[2],row,letter):
        return 1
    else:
        return 0
def findx3nwse(char1,char2,row,letter):
    char_nw = contents[row-1][letter-1]
    char_se = contents[row+1][letter+1]
    if char_se != char_nw:
        if char1 == char_nw or char2 == char_nw:
            if char1 == char_se or char2 == char_se:
                return True
    else:
        return False

def findx3nesw(char1,char2,row,letter):
    char_ne = contents[row-1][letter+1]
    char_sw = contents[row+1][letter-1]
    if char_sw != char_ne:
        if char1 == char_ne or char2 == char_ne:
            if char1 == char_sw or char2 == char_sw:
                return True
    else:
        return False


findx3string("MAS")