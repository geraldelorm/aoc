from collections import defaultdict
from math import inf
from os import path, sep


def main():
    p1 = 0
    p2 = inf
    cwd = ""
    dir_sizes = defaultdict(int)

    with open("day07/input.txt") as f:
        for line in f:
            parts = line.strip().split(" ")

            if parts[0] == "$" and parts[1] == "cd":
                cwd = path.normpath(path.join(cwd, parts[2]))

            if parts[0].isnumeric():
                dirs = cwd.split(sep)

                for i in range(len(dirs)):
                    dir_path = path.normpath(path.join(*dirs[: i + 1]))
                    dir_sizes[dir_path] += int(parts[0])

    avail_space = 7e7 - dir_sizes["."]
    sizes = dir_sizes.values()

    p1 = sum((v for v in sizes if v <= 1e5))
    p2 = min((v for v in sizes if v + avail_space >= 3e7))

    print(f"p1: {p1}, p2: {p2}")


if __name__ == "__main__":
    main()