"""
This is just a rough outline for what I will use in the actual game.
Just a way to get my thoughts onto "paper" and test out the algorithms
I thought out. Because of this, all the names are a work-in-progress, and
there are no comments or docstrings (since this is all coming from a writing
document where basically the only thing is equivalents to comments and
docstrings).
"""

DEAD = '.'
LIVE = '0'

size = 16
universe = [[DEAD for _ in range(size)] for _ in range(size)]
cells = []


for row in [5, 6]:
    for col in range(2, 2+9):
        cells.append((col, row))


for cell in cells:
    universe[cell[1]][cell[0]] = LIVE

def update():
    def in_bounds(coordinates: tuple[int]):
        x = 0 <= coordinates[0] < size
        y = 0 <= coordinates[1] < size
        return x and y

    remove_from_cells = []
    make_dead = []
    live_surrounding_dead = {}

    offsets = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]

    for i, cell in enumerate(cells):
        dead_surrounding_live = 0

        for offset in offsets:
            coord = (cell[0] + offset[0], cell[1] + offset[1])

            if in_bounds(coord):
                if universe[coord[1]][coord[0]] == DEAD:
                    dead_surrounding_live += 1

                    if coord in live_surrounding_dead:
                        live_surrounding_dead[coord] += 1
                    else:
                        live_surrounding_dead[coord] = 1
            else:
                dead_surrounding_live += 1

        if 8 - dead_surrounding_live not in [2, 3]:
            make_dead.append(cell)
            # building this list "backwards" so I don't get an IndexError
            remove_from_cells.insert(0, i)

    for i in remove_from_cells:
        del cells[i]

    for coord in make_dead:
        universe[coord[1]][coord[0]] = DEAD

    for coord, counter in live_surrounding_dead.items():
        if counter == 3 and in_bounds(coord):
            universe[coord[1]][coord[0]] = LIVE
            cells.append(coord)


def display():
    for line in universe:
        for cell in line:
            print(cell, end=' ')
        print()
    print()


from time import sleep

while True:
    display()
    sleep(0.2)
    update()