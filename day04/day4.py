def p1(file):
        
    with open(file) as f:
        fully_contained = 0
        for line in f:
            elf1, elf2 = line.strip().split(",")
            elf1_start, elf1_end = int(elf1.split("-")[0]), int(elf1.split("-")[1])
            elf2_start, elf2_end = int(elf2.split("-")[0]), int(elf2.split("-")[1])
                
            if ((elf1_start >= elf2_start and elf1_end <= elf2_end) or 
                (elf2_start >= elf1_start and elf2_end <= elf1_end)):
                fully_contained  += 1
                
        return fully_contained

print(p1("day04/test.txt"))
print(p1("day04/day4.txt"))

def p2(file):
    with open(file) as f:
        overlaps = 0
        for line in f:
            elf1, elf2 = line.strip().split(",")
            elf1_start, elf1_end = int(elf1.split("-")[0]), int(elf1.split("-")[1])
            elf2_start, elf2_end = int(elf2.split("-")[0]), int(elf2.split("-")[1])

            if ((elf1_start <= elf2_start and elf1_end >= elf2_start) or 
                (elf2_start <= elf1_start and elf2_end >= elf1_start)):
                overlaps += 1

        return overlaps

print(p2("day04/test.txt"))
print(p2("day04/day4.txt"))