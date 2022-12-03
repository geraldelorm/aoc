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
