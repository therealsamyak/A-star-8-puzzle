from queue import PriorityQueue


class Node:
    def __init__(
        self, cutoff: int, state: list, score_func: callable, parent: "Node" = None
    ) -> None:
        self.parent = parent
        self.state = state

        self.cutoff = cutoff
        self.max_len = len(state)
        self.score = score_func(state)

    # score comparison
    def __lt__(self, other: "Node"):
        return self.score < other.score

    # state comparison
    def isGoal(self, goal_state: "Node") -> bool:
        return self.state == goal_state.get_state()

    # so we can print(Node) directly
    def __repr__(self):
        result = ""
        for tile in range(len(self.state)):
            result += str(self.state[tile]) + " "
            if (tile + 1) % self.cutoff == 0 and tile != len(self.state) - 1:
                result += "\n"
        return result

    def get_state(self):
        return self.state


class Problem:
    def __init__(
        self, puzzle_type: int, initial_state: list, heuristic: callable
    ) -> None:
        # row width
        self.cutoff = int((puzzle_type + 1) ** (0.5))

        # heuristic function
        self.heuristic = heuristic

        # states
        self.initial_state = Node(self.cutoff, initial_state, heuristic)
        self.goal_state = Node(
            self.cutoff,
            [(i + 1) % (self.cutoff**2) for i in range(self.cutoff**2)],
            heuristic,
        )

        # solution path
        self.solution_path = []

    def get_initial_state(self):
        return self.initial_state

    def get_goal_state(self):
        return self.goal_state

    def ValidMoves(self, node: Node) -> list:
        # Find the empty tile's (0) position in the state array
        zero_index = node.state.index(0)

    def backtrack(self, node: Node):
        while node.parent != None:
            self.solution_path.append(node)
            node = node.parent

        self.solution_path = self.solution_path[::-1]

    def print_solution(self):
        for state in self.solution_path:
            print(state)
            print()

    def solve(self):
        frontier = []
