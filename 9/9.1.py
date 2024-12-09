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
        self.data = getinput(9, production = False)
        self.data = list(map(int,self.data))
        self.data_copy = self.data[:]
        self.size = len(self.data)
        self.first_free_index = 1
        self.process_data()
        self.i_still_needed_the_block_representation()
        self.checksum()
    
    def reset_file_iterator(self):
        return len(self.data)-1

    def reset_free_iterator(self):
        free = self.first_free_index
        while True:
            if self.data[free] > 0:
                free = self.first_free_index
                break
            else:
                free += 2
        return self.first_free_index

    def process_data(self):
        file = self.reset_file_iterator()
        free = self.reset_free_iterator()
        
        while True:
            print("free index:",free,"space:",self.data[free],"file index:",file//2,"filesize:",self.data[file])
            filecandidate = self.data[file]
            freecandidate = self.data[free]
            if filecandidate > freecandidate:
                if free < file-2:
                    free += 2
                    freecandidate = self.data[free]
                    #print("file too big")
                    continue
                else:
                    if file > free:
                        file -= 2
                        filecandidate = self.data[file]
                        free = self.reset_free_iterator()
                        print("no space for whole file")
                    else:
                        
                        break
            else:
                # data up to file before free space + now empty space between files + copy file into new location + remaining free space + everything after
                self.data = self.data[:free] + [0] + [self.data[file]] + [freecandidate - filecandidate] + self.data[free+1:]
                self.data.pop(file+2) #remove copied file
                if file+2 != len(self.data):
                    self.data[file+1] = self.data[file+1] + filecandidate + self.data.pop(file+2) #combine free space at and around removed file
                else:
                    self.data.pop(file+1) #remove trailing free space
                print(self.data)

    def i_still_needed_the_block_representation(self):
        self.blocks = []
        fileid = 0
        blockcounter = 0
        i = 0
        for val in self.data:
            if i%2 == 0:
                for block in range(0,val):
                    self.blocks.append(fileid)
                blockcounter += val
                fileid += 1
            else:
                for block in range(0,val):
                    self.blocks.append(-1)
                blockcounter += val
            i += 1
        print("".join(list(map(str,self.blocks)))) #fuck how I still needed the block representation

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