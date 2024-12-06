import re
import time

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
                if row != "":
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

def correct_updates_get():
    midpagesum = 0
    for update in updates:
        if len(update)%2 != 0:
            if page_order_correct(update):
                midpagesum += int(update[len(update)//2])
    return midpagesum

def main():
    data_get()
    process_rules()
    print(correct_updates_get())

#RUN
started = time.process_time_ns()
main()
print((time.process_time_ns() - started)/1000/1000, " ms")
#4354 2low