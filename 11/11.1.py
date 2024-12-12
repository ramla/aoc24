import time
from collections import Counter

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
        self.db = {}
        for stone in self.stones:
            if stone not in self.db:

                print(f"put new result in COUNTDB for {stone}")
                self.db[stone] = self.smart_blink_25([stone])
        all25 = []
        
        countdb = {}
        all25 = Counter()
        for stone in self.stones:
            countdb[stone] = Counter(self.smart_blink_25([stone]))

            print(f"Made COUNTDB an COUNTER() ENTRY for {stone}:")
            print(f"{countdb[stone].most_common()}")
            all25.update(countdb[stone])

        counted25 = Counter(all25)
        print(counted25.total(), "== counted25.total()")
        counted50 = Counter([])
        i25 = 0
        i50 = 0
        for stone, count in counted25.items():
            print(f"stone {stone} ({count} pieces) i25 {i25}/{len(counted25.keys())}")
            if stone not in countdb:
                countdb[stone] = Counter(self.smart_blink_25([stone]))
            temp = Counter()
            for stone, amount in countdb[stone].items():
                temp[stone] = count * amount
            counted50.update(temp)
            i25 += 1

        stonecount = 0
        len50 = len(counted50.keys())
        for stone, count in counted50.items():
            print(f"in 50; stonecount {stonecount} ; i50 {i50}/{len50} ; stone {stone} ({count} pieces)")
            if stone not in countdb:
                countdb[stone] = Counter(self.smart_blink_25([stone]))
            stonecount += countdb[stone].total() * count
            i50 += 1
        print(stonecount, "is the final result")

    def smart_blink_25(self,stones):
        result_stones = []
        length = len(stones)
        for i in range(length):
            #print(f"smart blink stone {i} out of {length}")
            stone = stones[i]
            if stone in self.db:
                result_stones += self.db[stone]
                print(f"put new result in self.db for {stone}")
            else:
                self.db[stone] = self.dumb_blink_multiple([stone],25)
                result_stones += self.db[stone]
        print("25 SMART BLINKS RESULT == ",len(result_stones))
        return result_stones
    
    def dumb_blink_multiple(self,stones,blinks):
        for i in range(blinks):
            stones = self.blink(stones)
        return stones
        #print(" ".join(list(map(lambda x: str(x),self.stones))))
    
    def blink(self,stones):
        i = 0
        max = len(stones)
        while True:
            if i >= max:
                break
            stone = stones[i]
            if stone == 0:
                stones[i] = 1
                i += 1
            elif len(str(stone))%2 == 0:
#                timetosplit = time.process_time_ns()
                
                stoned_ass_string = str(stone)
                stones[i] = int(stoned_ass_string[:len(stoned_ass_string)//2])
                stones.insert(i+1, int(stoned_ass_string[len(stoned_ass_string)//2:]))
                #print(f"{stone} split into two:", self.stones[i], self.stones[i+1])
                i += 2
                max += 1

                #timetosplit = time.process_time_ns() - timetosplit
#                self.timetosplit += timetosplit
            else:
                #timetomulti = time.process_time_ns()
                stones[i] = stone * 2024
                i += 1
                #timetomulti = time.process_time_ns() - timetomulti
               # self.timetomulti += timetomulti
        #timetocount = time.process_time_ns()
        #n = self.count_stones(stones)
        #print(f"n = {n}, split/multi = {self.timetosplit / self.timetomulti}")
        #print(len(stones),":"," ".join(list(map(lambda x: str(x), stones))))
        #timetocount = time.process_time_ns() - timetocount
        #print("one time count/multi = ",timetocount/timetomulti)
        return stones
    
    def count_stones(self, stones):
        count = 0
        for stone in stones:
            if type(stone) == list:
                count += self.count_stones(stone)
        else:
            count += 1
        return count
started = time.process_time_ns() 
observer(25)
print((time.process_time_ns() - started)/1000/1000, " ms")

# 261936432123724 is the final result
# 158976.751709  ms