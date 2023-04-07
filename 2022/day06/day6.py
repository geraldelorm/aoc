def hasUnique(val):
    table = set()
    for c in val:
        if c in table:
            return False
        else:
            table.add(c)
    return True

def p(file, marker):
    with open(file) as f:
        for line in f:
            lookup = set()
            line = line.strip()
            left, right = 0, marker
            
            while right < len(line):
                if hasUnique(line[left:right]):
                    print(right)
                    break
                else:
                    left += 1
                    right += 1

p("day06/test.txt", 4)
p("day06/day6.txt", 4)

p("day06/test.txt", 14)
p("day06/day6.txt", 14)