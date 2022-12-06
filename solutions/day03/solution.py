import pathlib
import sys


def parse(puzzle_input):
    """Parse input."""
    return puzzle_input.splitlines()


def part1(data):
    """Solve part 1."""
    data = [[i[0:len(i)//2], i[len(i)//2:]] for i in data]
    res = []
    for line in data:
        [l1, l2] = line
        found = False
        for i in l1:
            for j in l2:
                if i == j:
                    res.append(i)
                    found = True
                    break
            if found:
                break

    glyphs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return sum([glyphs.index(i) + 1 for i in res])


def part2(data):
    """Solve part 2."""
    glyphs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = []

    for i in range(len(data)//3):
        [l1, l2, l3] = data[i*3:i*3+3]
        res.append(''.join(set(l1).intersection(
            set(l2)).intersection(set(l3))))

    return sum([glyphs.index(i) + 1 for i in res])


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    path = 'data.txt'
    print(f"{path}:")
    puzzle_input = pathlib.Path(path).read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
