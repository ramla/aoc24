import itertools
from random import shuffle
import time

filename = "7/input.txt"
# filename = "7/testinput.txt"

data = []
longest_equation = 0
permutations = []
alternate_perms = []

with open(filename, "r") as file:
    for row in file:
        row = row.strip().split(": ")
        row[1] = row[1].split(" ")
        data.append(row)
        if len(row[1]) > longest_equation:
            longest_equation = len(row[1])

for i in range(0,longest_equation):
    permutations.append(list(itertools.product("01",repeat=i)))
for i in range(0,longest_equation):
    alternate_perms.append(list(itertools.product("012",repeat=i)))

def calculate(value1,value2,operator):
    if operator == "1":
        return int(value1) + int(value2)
    elif operator == "0":
        return int(value1) * int(value2)
    elif operator == "2":
        return int(str(value1)+value2)
    

def find_matches(eq,perms):
    result = int(eq[0])
    values = eq[1]
    print(result,"??",values)
    for permutation in perms[len(values)-1]:
        rolling = int(values[0])
        for i in range(0,len(values)-1):
            rolling = calculate(rolling,values[i+1],permutation[i])
            if rolling > result:
                #print(f"on operand {i}: {result} < {rolling}, breaking)")
                break
        if rolling == result:
            print("possible valid equation found, breaking (result {result})")
            return True
    return False

calibrated = 0
started = time.process_time_ns()
for eq in data:
    if not find_matches(eq,permutations):
        print("trying with concatenation operand")
        if find_matches(eq,alternate_perms):
            calibrated += int(eq[0])
    else:
        calibrated += int(eq[0])

print(calibrated)
print((time.process_time_ns() - started)/1000/1000, " ms")