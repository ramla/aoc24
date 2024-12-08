class laboratory:
    #filename = "6/testinput.txt"
    filename = "6/input.txt"
    
    room = []
    dir = "^"
    obstruction = (-1,-1)
    good_obstruction_positions = set([])
    invalid_obstruction_positions = set([])

    def __init__(self):
        with open(self.filename, "r") as file:
            for row in file:
                self.room.append(row.strip())
        self.height = len(self.room)
        self.width = len(self.room[0])
        
        for row in range(self.height):
            for column in range (self.width):
                if self.position_check((column,row)) == "^":
                    self.guard_init_pos = (column,row)
                    self.guard_init_dir = "^"
                    self.invalid_obstruction_positions.add(self.guard_init_pos)
                    self.room[row] = self.room[row].replace("^",".")
        #print(f"lab init done h {self.height}, w {self.width}")

    def position_check(self, pos):
        if pos == self.obstruction:
            return "O"
        if 0 <= pos[0] < self.width and 0 <= pos[1] < self.height:
            #print(self.room[pos[1]][pos[0]])
            return self.room[pos[1]][pos[0]]
        else:
            return None
    
    def obstruct(self,pos):
        self.obstruction = pos

    def note_obstruction(self):
        self.good_obstruction_positions.add(self.obstruction)

class guard:
    #lab = laboratory()
    visited = set([])
    turned = set([])
    
    def __init__(self, workplace):
        self.lab = workplace
        self.pos = self.lab.guard_init_pos
        self.dir = self.lab.guard_init_dir
        self.visited.add(self.pos)

    def patrol(self):
        match self.dir:
            case "^": 
                newpos = (self.pos[0], self.pos[1]-1)
                candidate = self.lab.position_check(newpos)
            case ">": 
                newpos = (self.pos[0]+1, self.pos[1])
                candidate = self.lab.position_check(newpos)
            case "v": 
                newpos = (self.pos[0], self.pos[1]+1)
                candidate = self.lab.position_check(newpos)
            case "<": 
                newpos = (self.pos[0]-1, self.pos[1])
                candidate = self.lab.position_check(newpos)
        
        if candidate == None:
            #print("guard out, obstruction didn't work")
            return False
        elif candidate == "#" or candidate == "O":
            match self.dir:
                case "^": self.dir = ">"
                case ">": self.dir = "v"
                case "v": self.dir = "<"
                case "<": self.dir = "^"
            if self.pos in self.turned:
                self.lab.note_obstruction()
                #print("frank is looping, rtb frank")
                return False
            self.turned.add(self.pos)
            return True
        elif candidate == ".":
            self.pos = newpos
            self.visited.add(newpos)
            if self.turned == set():
                self.lab.invalid_obstruction_positions.add(newpos)
            return True

lab = laboratory()
brian = guard(lab)
while brian.patrol():
    pass
possible_obstruction_positions = brian.visited.copy()
for pos in possible_obstruction_positions:
    #print(pos)
    frank = guard(lab)
    lab.obstruct(pos)
    while frank.patrol():
        pass
print(len(lab.good_obstruction_positions - lab.invalid_obstruction_positions))

#5208 all looping incl visible to guard
#5174 all looping except guard spawn + what's in front before turning first time
# so I guess it's rectangular loops only like in the example??