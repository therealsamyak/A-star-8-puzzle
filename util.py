from puzzle import Node

puzzle_type = 8
cutoff = int((puzzle_type + 1) ** (0.5))
final_state = [(i + 1) % (cutoff**2) for i in range(cutoff**2)]


def uniform_cost(current_state: "Node" = None) -> int:
    return 0


def misplaced_tile(current_state: "Node") -> int:
    incorrect_tiles = 0
    state = current_state.get_state()
    for index in range(len(state)):
        if state[index] != final_state[index]:
            incorrect_tiles += 1

    return incorrect_tiles


def euclidian_distance(current_state: "Node") -> int:
    # implement later
    pass
