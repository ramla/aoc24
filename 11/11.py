import time

productionfilename = "input.txt"
testfilename = "testinput.txt"

def getinput(window, production = True):
    if production:
        filename = str(window) + "/" + productionfilename
    else:
        filename = str(window) + "/" + testfilename
    
    input = []
    with open(filename, "r") as file:
        for row in file:
            input.append(row.strip().split(" "))
    return input[0]

class observer:
    def __init__(self, blinks):
        self.stones = list(map(lambda x: int(x),getinput(11,True)))
        for i in range(blinks):
            print("blink",i)
            self.blink()
        #print(" ".join(list(map(lambda x: str(x),self.stones))))
        print(f"n = {len(self.stones)}")
    
    def blink(self):
        i = 0
        max = len(self.stones)
        while True:
            if i >= max:
                break
            stone = self.stones[i]
            if stone == 0:
                self.stones[i] = 1
                i += 1
            elif len(str(stone))%2 == 0:
                stoned_ass_string = str(stone)
                self.stones[i] = int(stoned_ass_string[:len(stoned_ass_string)//2])
                self.stones.insert(i+1, int(stoned_ass_string[len(stoned_ass_string)//2:]))
                #print(f"{stone} split into two:", self.stones[i], self.stones[i+1])
                i += 2
                max += 1
            else:
                self.stones[i] = stone * 2024
                i += 1
    
started = time.process_time_ns() 
observer(75)
print((time.process_time_ns() - started)/1000/1000, " ms")