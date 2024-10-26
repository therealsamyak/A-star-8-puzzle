def print_puzzle(puzzle):
    for tile in range(len(puzzle)):
        print(puzzle[tile], end=" ")
        if ((tile - 2) % 3 == 0):
            print()
    print()


class Node:
    def __init__(self, parent: 'Node', state: list, score_func: callable) -> None:
        self.parent = parent
        self.state = state
        self.score = score_func(state)


class Problem:
    def __init__(self, cutoff: int, initial_state: list) -> None:
        self.cutoff = cutoff
        self.initial_state = Node(initial_state)
        self.final_state = [(i + 1) % (cutoff**2) for i in range(cutoff**2)]
