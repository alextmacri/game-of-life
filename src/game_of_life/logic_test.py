"""
This is just a rough outline for what I will use in the actual game.
Just a way to get my thoughts onto "paper" and test out the algorithms
I thought out. Because of this, all the names are a work-in-progress, and
there are no comments or docstrings (since this is all coming from a writing
document where basically the only thing is equivalents to comments and
docstrings).
"""


def dead_check(cells, universe):
    for cell in cells:
        counter = 0

        for offset in [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]:
            row, col = cell[1] + offset[1], cell[0] + offset[0]
            if universe[row][col] == 1:
                counter += 1

        if not 2 <= counter <= 3:
            universe[cell[1]][cell[0]] = 0

def live_check(cells, universe):
    counters = {}

    for cell in cells:
        for offset in [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]:
            coords = (cell[0] + offset[0], cell[1] + offset[1])

            if universe[coords[1]][coords[0]] == 0:
                if coords in counters:
                    counters[coords] += 1
                else:
                    counters[coords] = 1

    for coords, counter in counters.items():
        if counter == 3:
            universe[coords[1]][coords[0]] = 1


universe = [[0 for _ in range(16)] for _ in range(16)]
cells = []

cells.append((10, 10))
cells.append((11, 10))
cells.append((11, 11))

for cell in cells:
    universe[cell[1]][cell[0]] = 1

dead_check(cells, universe)
live_check(cells, universe)


for line in universe:
    print(line)