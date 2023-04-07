def get_priority(item):
    if item.islower():
        return ord(item) - ord("a") + 1
    else:
        return ord(item) - ord("A") + 27

def p1(file):
    with open(file) as f:
        total_priority = 0
        for line in f:
            line = line.strip()
            n = len(line)
            first_sack = set(line[:n//2])
            second_sack = set(line[n//2:])

            for item in first_sack:
                if item in second_sack:
                    total_priority += get_priority(item)

        return total_priority

print(p1("day03/test.txt"))
print(p1("day03/day3.txt"))


def p2(file):
    with open(file) as f:
        total_priority = 0
        lines = []
        for line in f:
            lines.append(line.strip())
            if len(lines) == 3:
                first_elf = set(lines[0])
                second_elf = set(lines[1])
                third_elf = set(lines[2])

                for item in first_elf:
                    if item in second_elf and item in third_elf:
                        total_priority += get_priority(item)
                lines = []

        return total_priority

print(p2("day03/test.txt"))
print(p2("day03/day3.txt"))