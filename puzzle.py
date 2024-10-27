from queue import PriorityQueue
from time import time


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

    def get_state(self):
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


class Problem:
    def __init__(
        self, puzzle_type: int, initial_state: list, heuristic: callable
    ) -> None:
        # row width
        self.cutoff = int((puzzle_type + 1) ** (0.5))

        # heuristic function
        self.heuristic = heuristic

        # states
        self.initial_state = Node(0, self.cutoff, initial_state, heuristic)
        self.goal_state = Node(
            0,
            self.cutoff,
            [(i + 1) % (self.cutoff**2) for i in range(self.cutoff**2)],
            heuristic,
        )

        # solution
        self.solution_path = []
        self.nodes_expanded = 0
        self.time_taken = 0
        self.max_queue_length = 0

        if not self.solve():
            print("No Solution Possible!")

    def get_initial_state(self) -> Node:
        return self.initial_state

    def get_goal_state(self) -> Node:
        return self.goal_state

    def backtrack(self, node: Node) -> None:
        self.solution_path.clear()
        while node is not None:
            self.solution_path.append(node)
            node = node.parent

        self.solution_path.reverse()

    def print_solution(self) -> None:
        for state in self.solution_path:
            print(state)
            print()

    def solve(self) -> bool:
        start = time()

        # priority queue
        frontier = PriorityQueue()
        frontier.put(self.initial_state)
        frontier_set = set()
        frontier_set.add(self.initial_state)

        self.nodes_expanded += 1

        # explored set
        visited = set()

        while not frontier.empty():
            self.max_queue_length = max(self.max_queue_length, frontier.qsize())

            curr_state: Node = frontier.get()
            frontier_set.remove(curr_state)
            self.nodes_expanded += 1

            # save solution path if solution found & leave
            if curr_state == self.goal_state:
                self.time_taken = time() - start
                self.backtrack(curr_state)
                return True

            visited.add(curr_state)

            # GENERATE CHILDREN AND ADD THEM TO FRONTIER IF NOT IN FRONTIER OR EXPLORABLE SET ALREADY
            for move_state in curr_state.valid_moves():
                child_node = Node(
                    curr_state.depth,
                    self.cutoff,
                    move_state,
                    self.heuristic,
                    curr_state,
                )
                if child_node not in frontier_set and child_node not in visited:
                    frontier.put(child_node)
                    frontier_set.add(child_node)

        if frontier.empty():
            return False
