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
            input.append(row.strip())
    return input

class fencer:
    def __init__(self):
        self.gardenmap = getinput(12,True)
        self.counted_cells = [] #cell counted towards an area
        self.current_counted_cells = [] #cell counted towards an area in current map_area() call
        self.areas = {}
        self.max_y = len(self.gardenmap)
        self.max_x = len(self.gardenmap[0])
        self.iterate_through_map()
        self.get_result()

        # AREA IDEA 1
        # iterate through in reading order, start blobbing up an area when new 
        # letter found in a yet unaccounted for cell. have a dict for areas
        # have a list for mapped cells
        # AND ACTUALLY just keep track of fence pieces by how many expansion searches
        # result in dead ends

        # area dict = key(plant): [ [starting pos , area , fence length] , [starting pos , area , fence length] ]

    def get_result(self):
        total_cost = 0
        for areas in self.areas.values():
            for area in areas:
                total_cost += (area[1]+1) * area[2]
                #print(f"Planter starting at {area[0]}: area {area[1]+1}, fence length, cells = {area[2:]}")
        print("fence costs",total_cost,"in total")

    def iterate_through_map(self):
        for y in range(self.max_y):
            for x in range(self.max_x):
                pos = (x,y)
                if pos not in self.counted_cells:
                    plant = self.getplant(pos)
                    if not plant in self.areas:
                        self.areas[plant] = []
                    self.areas[plant].append([pos] + self.map_area(pos, plant) + self.current_counted_cells)
                    self.counted_cells += [pos] + self.current_counted_cells
                    self.current_counted_cells = []

    def map_area(self, pos, plant):
        candidates = [(pos[0]+1,pos[1]), (pos[0],pos[1]+1), (pos[0]-1,pos[1]), (pos[0],pos[1]-1)]
        gathered_data = [0,0]
        self.current_counted_cells.append(pos)
        for candidate in candidates:
            if self.is_valid(candidate):
                if plant == self.getplant(candidate):
                    if candidate not in self.current_counted_cells:
                        recurse = self.map_area(candidate,plant)
                        gathered_data[0] += 1 + recurse[0] #found area + amount of further found area
                        gathered_data[1] += recurse[1] #further found fences
                else:
                    gathered_data[1] += 1 #different plant, adding fence
            else:
                gathered_data[1] += 1 #out of boundaries, adding fence
        return [gathered_data[0],gathered_data[1]]
    
    def getplant(self, pos):
        return self.gardenmap[pos[1]][pos[0]]

    def is_valid(self, pos):
        return 0 <= pos[0] < self.max_x and 0 <= pos[1] < self.max_y and pos not in self.counted_cells

started = time.process_time_ns() 
fencer()
print((time.process_time_ns() - started)/1000/1000, " ms")