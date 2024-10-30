class Node:
    def __init__(
        self,
        depth: int,
        cutoff: int,
        state: list,
        score_func: callable,
        parent: "Node" = None,
    ) -> None:

        if (
            len(state) != cutoff**2
            or len(state) != len(set(state))
            or any(value >= cutoff**2 for value in state)
        ):
            raise ValueError(f"Invalid Node arguments.")

        self.parent = parent
        self.state = state

        self.depth = depth
        self.heuristic_score = score_func(state)
        self.cutoff = cutoff
        self.score = depth + self.heuristic_score

    # need to override operators so they are compatible with set() and PriorityQueue()
    def __lt__(self, other: "Node") -> bool:
        return self.score < other.score

    def __eq__(self, other: "Node") -> bool:
        return self.state == other.state

    def __hash__(self) -> int:
        return hash(tuple(self.state))

    # so we can print(Node) directly
    def __repr__(self) -> str:
        result = ""
        for tile in range(len(self.state)):
            result += str(self.state[tile]) + " "
            if (tile + 1) % self.cutoff == 0 and tile != len(self.state) - 1:
                result += "\n"
        return result

    def get_state(self) -> list:
        return self.state

    def valid_moves(self) -> list:
        possibleMoves = []

        zero_index = self.state.index(0)

        if (zero_index + self.cutoff) < self.cutoff**2:
            # Create a copy of the current state to modify for this move
            new_state = self.state[:]
            # Swap the zero tile with the tile in the target position (move down)
            new_state[zero_index], new_state[zero_index + self.cutoff] = (
                new_state[zero_index + self.cutoff],
                new_state[zero_index],
            )
            possibleMoves.append(new_state)

        if (zero_index - self.cutoff) >= 0:
            # Create a copy of the current state to modify for this move
            new_state = self.state[:]
            # Swap the zero tile with the tile in the target position (move up)
            new_state[zero_index], new_state[zero_index - self.cutoff] = (
                new_state[zero_index - self.cutoff],
                new_state[zero_index],
            )
            possibleMoves.append(new_state)

        if (zero_index % self.cutoff) != 0:
            # Create a copy of the current state to modify for this move
            new_state = self.state[:]
            # Swap the zero tile with the tile in the target position (move left)
            new_state[zero_index], new_state[zero_index - 1] = (
                new_state[zero_index - 1],
                new_state[zero_index],
            )
            possibleMoves.append(new_state)

        if (zero_index % self.cutoff) != (self.cutoff - 1):
            # Create a copy of the current state to modify for this move
            new_state = self.state[:]

            # Swap the zero tile with the tile in the target position (move right)
            new_state[zero_index], new_state[zero_index + 1] = (
                new_state[zero_index + 1],
                new_state[zero_index],
            )
            # Add the new state to possible moves
            possibleMoves.append(new_state)

        return possibleMoves
