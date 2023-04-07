
class Solution:
    def __init__(self, fileName) -> None:
        self.grid, self.R, self.C, self.file = None, 0, 0, fileName
        self.readFile()

    def readFile(self):
        with open(self.file) as f:
            self.grid = [list(map(int, line.strip())) for line in f.readlines()]

        self.R = len(self.grid)
        self.C = len(self.grid[0])

    def isVisible(self, row, col):
        # it is an edge
        if row == 0 or row == self.R - 1 or col == 0 or col == self.C - 1:
            return 1
        
        tree = self.grid[row][col]

        # look left
        if max([self.grid[row][cc] for cc in range(col)]) < tree:
            return 1

        # look right
        if max([self.grid[row][cc] for cc in range(col + 1, self.C)]) < tree:
            return 1

        # look up
        if max([self.grid[cr][col] for cr in range(row)]) < tree:
            return 1

        # look down
        if max([self.grid[cr][col] for cr in range(row + 1, self.R)]) < tree:
            return 1

        return 0

    def scenic_score(self, row, col):
        # it is an edge - score is Zero
        if row == 0 or row == self.R - 1 or col == 0 or col == self.C - 1:
            return 1

        tree = self.grid[row][col]

        # left scene
        for cc in range(1, col + 1):
            if self.grid[row][col - cc] >= tree:
                break
        left = cc

        # right scene
        for cc in range(1, self.C - col):
            if self.grid[row][col + cc] >= tree:
                break
        right = cc

        # top scene
        for cr in range(1, row + 1):
            if self.grid[row - cr][col] >= tree:
                break
        top = cr

        # down scene
        for cr in range(1, self.R - row):
            if self.grid[row + cr][col] >= tree:
                break
        down = cr

        return left * right * top * down
    
    def partOne(self):
        total = 0

        for r in range(self.R):
            for c in range(self.C):
                total += self.isVisible(r, c)

        return total

    
    def partTwo(self):
        score = 0

        for r in range(self.R):
            for c in range(self.C):
                score = max(score, self.scenic_score(r, c))

        return score



if __name__ == "__main__":
    t_solution = Solution("day08/test.txt")
    solution = Solution("day08/input.txt")


    assert t_solution.partOne() == 21
    print("Part One: ", solution.partOne())
    assert t_solution.partTwo() == 8
    print("Part Two: ", solution.partTwo())