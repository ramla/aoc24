import re

contents = []

filename = "3/input.txt"

with open(filename, "r") as file:
    for row in file:
        contents.append(row)

pattern = re.compile("mul\([0-9]{1,3},[0-9]{1,3}\)")
#pattern = re.compile("mul")

matches = []

for row in contents:
    result = pattern.findall(row)
    for match in result:
        matches.append(match.strip("mul(").strip(")").split(","))

sum = 0
for match in matches:
    sum += int(match[0]) * int(match[1])
print(sum)