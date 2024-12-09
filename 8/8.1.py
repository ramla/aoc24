from itertools import product

productionfilename = "input.txt"
testfilename = "testinput.txt"

def getinput(window, production = False):
    if production:
        filename = str(window) + "/" + productionfilename
    else:
        filename = str(window) + "/" + testfilename
    
    input = []
    with open(filename, "r") as file:
        for row in file:
            input.append(row.strip())
    return input

class coord:
    def __init__(self,pos):
        self.x = pos[0]
        self.y = pos[1]
    
    def __sub__(self,pos):
        return coord((self.x - pos.x, self.y - pos.y))
    
    def __add__(self,pos):
        return coord((self.x + pos.x, self.y + pos.y))
    
    def __mul__(self,n):
        return coord((self.x * n, self.y * n))
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def tuplify(self):
        return (self.x,self.y)


class mapoftheland:
    def __init__(self):
        self.antmap = getinput(8,production=True)

    def build_antdict(self):
        self.antdict = {}
        self.antpairs = {}
        self.max_y = len(self.antmap) 
        self.max_x = len(self.antmap[0])
        for row in range(0,self.max_y):
            for column in range(0,self.max_x):
                char = self.antmap[row][column]
                if char != ".":
                    if char not in self.antdict:
                        self.antdict[char] = set()
                    self.antdict[char].add((column,row))
        for char in self.antdict:
            self.antdict[char] = list(product(self.antdict[char],repeat = 2)) 
    
    def antinoder(self):
        self.anmap = set()
        for frequency, ant_pairs in self.antdict.items():
            print(ant_pairs)
            for ant_pair in ant_pairs:
                nodes = self.get_nodes(ant_pair)
                
                # if ant_pair[0] != ant_pair[1]:
                #     diff = coord((ant_pair[0][0] - ant_pair[1][0], ant_pair[0][1] - ant_pair[1][1]))
                #     antinode1 = coord(ant_pair[0]) + diff
                #     print(f"{coord(ant_pair[0])} + {diff} = {antinode1}")
                #     antinode2 = coord(ant_pair[1]) - diff
                #     print(f"{coord(ant_pair[1])} - {diff} = {antinode2}")
                #     if self.is_valid(antinode1):
                #         self.anmap.add(antinode1.tuplify())
                #     if self.is_valid(antinode2):
                #         self.anmap.add(antinode2.tuplify())
        
        #print(list(map(lambda x: str(x),self.anmap)))
   
    def is_valid(self,pos):
        if 0 <= pos.x < self.max_x and 0 <= pos.y < self.max_y:
            return (pos.x, pos.y)
        else:
            print(pos, "is not valid")

    def get_nodes(self, ant_pair):
        if ant_pair[0] != ant_pair[1]:
            diff = coord((ant_pair[0][0] - ant_pair[1][0], ant_pair[0][1] - ant_pair[1][1]))
            self.anmap.add(ant_pair[0])
            self.anmap.add(ant_pair[1])
            node = 0
            while True:
                antinode = coord(ant_pair[0]) + diff * node
                if self.is_valid(antinode):
                    self.anmap.add(antinode.tuplify())
                    node += 1
                else:
                    break
            node = 0
            while True:
                antinode = coord(ant_pair[1]) - diff * node
                if self.is_valid(antinode):
                    self.anmap.add(antinode.tuplify())
                    node += 1
                else:
                    break

antinoder = mapoftheland()
antinoder.build_antdict()
antinoder.antinoder()
print(len(antinoder.anmap))
