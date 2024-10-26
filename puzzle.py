def print_puzzle(puzzle):
    for tile in range(len(puzzle)):
        print(puzzle[tile], end=" ")
        if ((tile - 2) % 3 == 0):
            print()
    print()


class Problem:
    def __init__(self) -> None:
        pass