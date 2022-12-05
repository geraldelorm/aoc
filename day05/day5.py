def p1(file, crates):
    make_moves = False
    with open(file) as f:
        for line in f:
            if line == "\n":
                make_moves = True
                continue

            if not make_moves:
                # To do - Build crates from input
                # print(line.split("\n")[:-1])
                continue
            
            if make_moves:
                line = line.strip().split(" ")
                to = int(line[5]) - 1
                from_ = int(line[3]) - 1
                moves = int(line[1])
                
                for i in range(moves):
                    crates[to].append(crates[from_].pop())

        return "".join(stack[-1] for stack in crates)


def p2(file, crates):
    make_moves = False
    with open(file) as f:
        for line in f:
            if line == "\n":
                make_moves = True
                continue

            if not make_moves:
                # To do - Build crates from input
                # print(line.split("\n")[:-1])
                continue

            if make_moves:
                line = line.strip().split(" ")
                to = int(line[5]) - 1
                from_ = int(line[3]) - 1
                moves = int(line[1])

                crates[to]  = crates[to] + crates[from_][len(crates[from_]) - moves:]
                del crates[from_][len(crates[from_]) - moves:]
             
        return "".join(s.pop() for s in list(filter(lambda x : len(x) > 0 , crates)))

test_crates = [["Z", "N"], ["M", "C", "D"], ["P"]]
crates = [["T", "P", "Z", "C", "S", "L", "Q", "N"], 
              ["L", "P", "T", "V", "H", "C", "G"],
              ["D", "C", "Z", "F"],
              ["G", "W", "T", "D", "L", "M", "V", "C"],
              ["P", "W", "C"],
              ["P", "F", "J", "D", "C", "T", "S", "Z"],
              ["V", "w", "G", "B", "D"], 
              ["N", "J", "S", "Q", "H", "W"], 
              ["R", "C", "Q", "F", "S", "L", "V"]]

print(p1("day05/test.txt", test_crates))
print(p1("day05/day5.txt", crates))

test_crates = [["Z", "N"], ["M", "C", "D"], ["P"]]
crates = [["T", "P", "Z", "C", "S", "L", "Q", "N"], 
              ["L", "P", "T", "V", "H", "C", "G"],
              ["D", "C", "Z", "F"],
              ["G", "W", "T", "D", "L", "M", "V", "C"],
              ["P", "W", "C"],
              ["P", "F", "J", "D", "C", "T", "S", "Z"],
              ["V", "w", "G", "B", "D"], 
              ["N", "J", "S", "Q", "H", "W"], 
              ["R", "C", "Q", "F", "S", "L", "V"]]

print(p2("day05/test.txt", test_crates))
print(p2("day05/day5.txt", crates))
