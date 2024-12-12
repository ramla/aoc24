import time

productionfilename = "input.txt"
testfilename = "testinput.txt"

class coord:
    def __init__(self,pos):
        self.x = pos[0]
        self.y = pos[1]
    
    def __sub__(self,pos):
        return coord((self.x - pos.x, self.y - pos.y))
    
    def __add__(self,pos):
        return coord((self.x + pos.x, self.y + pos.y) )
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def tuplify(self):
        return (self.x,self.y)

class topography:
    def __init__(self, window, production = False):
        if production:
            filename = str(window) + "/" + productionfilename
        else:
            filename = str(window) + "/" + testfilename

        self.topo = []
        with open(filename, "r") as file:
            for row in file:
                self.topo.append(row.strip())
        self.process_data()
        self.height = len(self.topo)
        self.width = len(self.topo[0])
        self.trailheads = self.find_trailheads()
        self.score_trailheads()
    
    def find_trailheads(self):
        trailheads = []
        for row in range(self.height):
            for column in range(self.width):
                if self.topo[row][column] == 0:
                    trailheads.append(coord((column,row)))
        return trailheads

    def is_on_map(self, pos:coord):
        return 0 <= pos.x < self.width and 0 <= pos.y < self.height
    
    def find_trail(self, pos:coord):
        score = []
        height = self.get_height(pos) + 1
        if height < 10:
            candidates = [coord((pos.x+1,pos.y)), coord((pos.x,pos.y+1)), coord((pos.x-1,pos.y)), coord((pos.x,pos.y-1))]
            #print(list(map(self.is_on_map,candidates)))
            # try:
            for candidate in candidates:
                if self.is_on_map(candidate):
                    if self.get_height(candidate) == height:
                        #print(f"next pos: {candidate}, height {height}")
                        score += self.find_trail(candidate)
                    else:
                        #print(f"Dead end: candidate {candidate}: wrong height ({self.get_height(candidate)}, looking for {height})")
                        pass
                else:
                    #print(f"Dead end: candidate {candidate} not on map")
                    pass
        elif height == 10:
            score += [pos]
            #print(f"reached the PEAK adding a ----- peak to the scores")
        #print(f"returning {list(map(lambda x: str(x),score))}")
        return score
    
    def score_trailheads(self):
        trailhead_scores = 0
        #print(list(map(lambda x: str(x), self.trailheads)))
        for i in range(len(self.trailheads)):
        # if True:
            trailhead = self.trailheads[i]
            score = self.find_trail(trailhead)
            #{list(map(lambda x: str(x), list(map(lambda x: x.tuplify(), set(score)))))}")
            score = len(list(set(list(map(lambda x: x.tuplify(), score)))))
            print(f"trailhead {trailhead} score = {score}") 
            trailhead_scores += score
        print(trailhead_scores)

    def process_data(self):
        for row in range(len(self.topo)):
            self.topo[row] = list(map(lambda x: int(x), self.topo[row]))

    def get_height(self, pos:coord):
        #print(f"candidate height = {self.topo[pos.y][pos.x]}")
        return self.topo[pos.y][pos.x]
    
started = time.process_time_ns() 
topography(10,True)
print((time.process_time_ns() - started)/1000/1000, " ms")