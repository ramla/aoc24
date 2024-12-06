import re
import time
from random import shuffle

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
        # if p > 0:
        #     for update_page in update[:p]:
        #         #print(f"is {update_page} from {update[:p]} in list of pages that should come after it: {after[update[p]]}")
        #         #print(f"og uprate: {update}\nshiterate: {update[:p] + [update[p]] + update[p+1:]}")
        #         if update_page in after[update[p]]:
        #             print(f"page {update_page} should come after {update[p]}: {sorted(after[update[p]])}\nupdate: {update}")
        #             return False
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
        if len(update)%2 != 0:
            if not page_order_correct(update):
                corrected = correct_page_order(update,n)
                midpagesum += int(corrected[len(corrected)//2])
                n+=1

    return midpagesum

def correct_page_order(update,n):
    shuffle(update)
    shuffled = 1
    while not page_order_correct(update):
        shuffle(update)
        shuffled+=1
    nose = n*shuffled*"-"
    print(f"got it! :{nose}D")
    print(f"shuffled {shuffled} time(s)")
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
#4354 2low