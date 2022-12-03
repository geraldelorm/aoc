def p1(file):
    with open(file) as f:
        lose, draw, win = 0, 3, 6
        values = {"rock": 1, "paper": 2, "scissors": 3}
        look_up_table = {("A", "X"): values["rock"] + draw, ("A", "Y"): values["paper"] + win, ("A", "Z"): values["scissors"] + lose,
                         ("B", "X"): values["rock"] + lose, ("B", "Y"): values["paper"] + draw, ("B", "Z"): values["scissors"] + win,
                         ("C", "X"): values["rock"] + win, ("C", "Y"): values["paper"] + lose, ("C", "Z"): values["scissors"] + draw}
        score = 0
        for line in f:
            opponent_move, my_move = line.strip().split(" ")
            score += look_up_table[(opponent_move, my_move)]

        return score

print("P1 Test: ", p1("day02/test.txt"))
print("P1 Actual: ", p1("day02/day2.txt"))


def p2(file):
    with open(file) as f:
        lose, draw, win = 0, 3, 6
        values = {"rock": 1, "paper": 2, "scissors": 3}
        look_up_table = {("A", "X"): values["scissors"] + lose, ("A", "Y"): values["rock"] + draw, ("A", "Z"): values["paper"] + win,
                         ("B", "X"): values["rock"] + lose, ("B", "Y"): values["paper"] + draw, ("B", "Z"): values["scissors"] + win,
                         ("C", "X"): values["paper"] + lose, ("C", "Y"): values["scissors"] + draw, ("C", "Z"): values["rock"] + win}
        score = 0
        for line in f:
            opponent_move, my_move = line.strip().split(" ")
            score += look_up_table[(opponent_move, my_move)]

        return score

print("P2 Test: ", p2("day02/test.txt"))
print("P2 Actual: ", p2("day02/day2.txt"))





# def p1(file):
#     with open(file) as f:
#         score = 0
#         for line in f:
#             opponent_move, my_move = line.strip().split(" ")
#             if opponent_move == "A":
#                 if my_move == "X":
#                     score += 1 + 3
#                 elif my_move == "Y":
#                     score += 2 + 6
#                 elif my_move == "Z":
#                     score += 3 + 0

#             elif opponent_move == "B":
#                 if my_move == "X":
#                     score += 1 + 0
#                 elif my_move == "Y":
#                     score += 2 + 3
#                 elif my_move == "Z":
#                     score += 3 + 6

#             elif opponent_move == "C":
#                 if my_move == "X":
#                     score += 1 + 6
#                 elif my_move == "Y":
#                     score += 2 + 0
#                 elif my_move == "Z":
#                     score += 3 + 3
#         return score

# print("P1 Test: ", p1("day02/test.txt"))
# print("P1 Actual: ", p1("day02/day2.txt"))



# def p2(file):
#     with open(file) as f:
#         score = 0
#         for line in f:
#             opponent_move, my_move = line.strip().split(" ")
#             if opponent_move == "A":
#                 if my_move == "X":
#                     score += 3 + 0
#                 elif my_move == "Y":
#                     score += 1 + 3
#                 elif my_move == "Z":
#                     score += 2 + 6

#             elif opponent_move == "B":
#                 if my_move == "X":
#                     score += 1 + 0
#                 elif my_move == "Y":
#                     score += 2 + 3
#                 elif my_move == "Z":
#                     score += 3 + 6

#             elif opponent_move == "C":
#                 if my_move == "X":
#                     score += 2 + 0
#                 elif my_move == "Y":
#                     score += 3 + 3
#                 elif my_move == "Z":
#                     score += 1 + 6
#         return score

# print("P2 Test: ", p2("day02/test.txt"))
# print("P2 Actual: ", p2("day02/day2.txt"))
