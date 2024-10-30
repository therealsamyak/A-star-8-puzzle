puzzle_type = 8
cutoff = int((puzzle_type + 1) ** (0.5))
final_state = [(i + 1) % (cutoff**2) for i in range(cutoff**2)]


def uniform_cost(state: list = None) -> int:
    return 0


def misplaced_tile(state: list) -> int:
    incorrect_tiles = 0
    for index in range(len(state)):
        if state[index] != final_state[index]:
            incorrect_tiles += 1

    return incorrect_tiles


def hypotenuse(x, y) -> float:
    return (x**2 + y**2) ** (0.5)


def euclidean_distance(state: list) -> int:
    state_mappings = {}
    final_state_mappings = {}

    for index, value in enumerate(state):
        x = index % cutoff
        y = index // cutoff

        state_mappings[value] = (x, y)

    for index, value in enumerate(final_state):
        x = index % cutoff
        y = index // cutoff

        final_state_mappings[value] = (x, y)

    total_distance = 0
    for value in state:
        if value != 0:
            curr_x, curr_y = state_mappings[value]
            final_x, final_y = final_state_mappings[value]
            total_distance += hypotenuse(curr_x - final_x, curr_y - final_y)

    return total_distance
