import re
import time
from math import log10

filename = "5/input.txt"
#filename = "5/testinput.txt"

rules = []
rulepattern = re.compile(r"..\|")

before = {}
after = {}

updates = []

def data_get():
    with open(filename, "r") as file:
        for line in file:
            row = line.replace("\n","")
            if re.match(rulepattern, row):
                rule = row.split("|")
                rules.append( ( rule[0] , rule[1] ) )
            else:
                updates.append(row.split(","))

def process_rules():
    for n in range(1,100):
        after[str(n)] = []
        before[str(n)] = []
    for rule in rules:
        after[rule[0]].append(rule[1])
        before[rule[1]].append(rule[0])

def page_order_correct(update):
    for p in range(0,len(update)):
        if p < len(update)-1:
            for update_page in update[p+1:]:
                if update_page in before[update[p]]:
                    #print(f"page {update_page} (index {p}) should come before {update[p]}: ({before[update[p]]})")
                    return False
    return True

def incorrect_updates_get():
    midpagesum = 0
    n = 1
    for update in updates:
        operations = 0
        if len(update)%2 != 0 and not page_order_correct(update):
            while not page_order_correct(update):
                update = correct_page_order(update,n)
                operations += 1
            midpagesum += int(update[len(update)//2])
            n+=1

            nose = int(log10(n*operations))*"-"
            print(f"got it! :{nose}D")
    return midpagesum

def correct_page_order(update,n):
    for p in range(0,len(update)):
        if p < len(update)-1:
            #for update_page in update[p+1:]:
            for i in range(p+1, len(update)):
                update_page = update[i]
                if update_page in before[update[p]]:
                    print(f"page {update_page} (index {p}) should come before {update[p]}: ({before[update[p]]})")
                    # switch indexes of update_page (update[p+n]) and update[p]:
                    update[i], update[p] = update[p], update[i]
    
    return update

def main():
    data_get()
    updates.pop(0)
    process_rules()
    print(incorrect_updates_get())

#RUN
started = time.process_time_ns()
main()
print((time.process_time_ns() - started)/1000/1000, " ms")