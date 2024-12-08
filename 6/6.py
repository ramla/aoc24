class laboratory:
    #filename = "6/testinput.txt"
    filename = "6/input.txt"

    room = []
    dir = "^"

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
                    self.room[row] = self.room[row].replace("^",".")
        print(f"lab init done h {self.height}, w {self.width}")

    def position_check(self, pos):
        if 0 <= pos[0] < self.width and 0 <= pos[1] < self.height:
            #print(self.room[pos[1]][pos[0]])
            return self.room[pos[1]][pos[0]]
        else:
            return None

class guard:
    lab = laboratory()
    visited = set([])
    
    def __init__(self):
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
            #print("guard out, returning visited")
            #return len(self.visited) lol maximum recursion depth exceeded
            return False
        elif candidate == "#":
            match self.dir:
                case "^": self.dir = ">"
                case ">": self.dir = "v"
                case "v": self.dir = "<"
                case "<": self.dir = "^"
            return True
        elif candidate == ".":
            self.pos = newpos
            #print(f"adding visited, sofar {self.visited}")
            self.visited.add(newpos)
            return True

brian = guard()
while brian.patrol():
    pass
print(len(brian.visited))