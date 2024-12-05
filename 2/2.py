file = "2/reports.txt"
#file = "2/test.txt"

reports = []

with open(file, "r") as input:
    for row in input:
        reports.append([int(entry) for entry in row.strip("\n").split(" ")])


def is_safe(report:list):
    if len(report) == 1:
        return True
    increasing = False
    decreasing = False
    for i in range(0,len(report)-1):
        diff = report[i] - report[i+1] 
        if 1 <= diff <= 3:
            decreasing = True
        elif -1 >= diff >= -3:
            increasing = True
        else:
            return False
        if decreasing and increasing:
            return False
    return True

def is_safe2(report:list):
    if len(report) == 1:
        return True
    increasing = False
    decreasing = False
    offending_index = 0 
    for i in range(0,len(report)-1):
        diff = report[i] - report[i+1] 
        if 1 <= diff <= 3:
            decreasing = True
        elif -1 >= diff >= -3:
            increasing = True
        else:
            return (False, offending_index)
        if decreasing and increasing:
            offending_index = i
            return (False, offending_index)
    return (True, 0)

def find_safe_variation(report, offending_index):
    current_index = offending_index
    for i in range(0,len(report)):
        variation = report[:]
        variation.pop(current_index)
        if is_safe2(variation)[0]:
            # print(f"{variation}, {offending_index}, {current_index}")
            return True
        else:
            current_index += 1
            if current_index > len(report)-1:
                current_index = 0
    return False

def find_safe_reports(reports):
    sumsafe = 0
    for report in reports:
        analysis = is_safe2(report)
        if analysis[0]:
            sumsafe += 1
        elif find_safe_variation(report, analysis[1]):
            sumsafe += 1
    return sumsafe


#part1
answer = sum(map(is_safe, reports))
print(f"{answer} safe reports")

print(f"{find_safe_reports(reports)} safe reports with margin of 1")
    # if not is_safe_by_itself(reports[index]):
        # return False
    # if index < len(reports) -1:
    #     if not is_safe_compared_to(reports[index], reports[index+1]):
    #         return False
    # if index > 0:
    #     if not is_safe_compared_to(reports[index], reports[index-1]): 
    #         return False
    # return True

# # def is_safe_by_itself(report:list):
#     pass


# def is_safe_compared_to(report1:list, report2:list):
#     try:
#         pass
#         #tsekkaa ylempi rivi
#     except:
#         pass
#         #ylempää riviä ei oo