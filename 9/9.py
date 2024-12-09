import time

productionfilename = "input.txt"
testfilename = "testinput.txt"

def getinput(window, production = True):
    if production:
        filename = str(window) + "/" + productionfilename
    else:
        filename = str(window) + "/" + testfilename
    data = ""
    with open(filename, "r") as file:
        for row in file:
            data += row.strip()
    return data

class defragger:
    def __init__(self):
        self.data = getinput(9, production = True)
        self.process_data()
        self.checksum()
    
    def process_data(self):
        self.blocks = []
        self.size = len(self.data)
        fileid = 0
        blockcounter = 0
        i = 0
        for char in self.data:
            if i%2 == 0:
                for block in range(0,int(char)):
                    self.blocks.append(fileid)
                blockcounter += int(char)
                fileid += 1
            else:
                for block in range(0,int(char)):
                    self.blocks.append(-1)
                blockcounter += int(char)
            i += 1
        self.blocks_copy = self.blocks[:]
        
        blockcounter = 0
        for block in self.blocks_copy:
            if block < 0:
                try: 
                    while True:
                        candidate = self.blocks.pop()
                        if candidate >= 0:
                            break
                except:
                    print("no more blocks to move")
                    return
                if blockcounter >= len(self.blocks):
                    print("no more blocks to defragment")
                    self.blocks.append(candidate)
                    return
                self.blocks[blockcounter] = candidate
                #print("".join(list(map(str, self.blocks))))
            blockcounter += 1
    
    def checksum(self):
        checksum = 0
        blockcounter = 0
        for block in self.blocks:
           checksum += block * blockcounter
           blockcounter += 1
        print(checksum)

started = time.process_time_ns() 
defragger()
print((time.process_time_ns() - started)/1000/1000, " ms")