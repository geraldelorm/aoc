# def p1(file):
#     maxCal = 0
#     try:
#         fp = open(file)
#         currMax = 0
#         for line in fp:
#             if "\n" in line:
#                 line = line.strip()
#                 if line == "":
#                     maxCal = max(maxCal, currMax)
#                     currMax = 0
#                 else:
#                     currMax += int(line)
#             else:
#                 maxCal = max(maxCal, currMax + int(line)) #last line
#     finally:
#         fp.close()

#     return maxCal

# print(p1('day01/day1.txt'))




import heapq

def p2(file):
    max3, currMax, cap  = [], 0, 3
    
    with open(file) as f:
        for indx, line in enumerate(f):
            if "\n" in line:
                line = line.strip()

                if line == "":
                    heapq.heappush(max3, currMax)

                    if len(max3) > cap:
                        heapq.heappop(max3)

                    currMax = 0
                else:
                    currMax += int(line)
            else:
                heapq.heappush(max3, currMax + int(line))

                if len(max3) > cap:
                    heapq.heappop(max3)

    return sum(max3)

print(p2('day01/day1.txt'))