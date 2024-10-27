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
            raise ValueError(f"No solution possible.")

        self.parent = parent
        self.state = state

        self.depth = depth
        self.heuristic_score = score_func(state)
        self.cutoff = cutoff
        self.max_len = len(state)
        self.score = depth + score_func(state)

    # need to override operators so they are compatible with set() and PriorityQueue()
    def __lt__(self, other: "Node") -> bool:
        return self.score < other.score

    def __eq__(self, other: "Node") -> bool:
        return self.state == other.state

    def __hash__(self) -> int:
        return hash(self.state)

    # state comparison
    def isGoal(self, goal_state: "Node") -> bool:
        return self.state == goal_state.get_state()

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
            self.cutoff,
            [(i + 1) % (self.cutoff**2) for i in range(self.cutoff**2)],
            heuristic,
        )

        # solution
        self.solution_path = []
        self.nodes_expanded = 0
        self.time_taken = 0
        self.max_queue_length = 0

    def get_initial_state(self) -> Node:
        return self.initial_state

    def get_goal_state(self) -> Node:
        return self.goal_state

    def ValidMoves(self, node: Node) -> list:
        # Find the empty tile's (0) position in the state array
        zero_index = node.state.index(0)

    def backtrack(self, node: Node) -> None:
        self.solution_path.clear()
        while node.parent != None:
            self.solution_path.append(node)
            node = node.parent

        self.solution_path = self.solution_path[::-1]

    def print_solution(self) -> None:
        for state in self.solution_path:
            print(state)
            print()

    def solve(self) -> bool:
        pass

        start = time()
        frontier = PriorityQueue([self.initial_state])
        visited = set()
        depth = 0

        while not frontier.empty():
            curr_state: Node = frontier.get()

            # save solution path if solution found & leave
            if curr_state.isGoal(self.goal_state):
                self.time_taken = time() - start
                self.backtrack(curr_state)
                return True

            visited.add(curr_state)

            # GENERATE CHILDREN AND ADD THEM TO FRONTIER IF NOT IN FRONTIER OR EXPLORABLE SET ALREADY

        if frontier.empty():
            return False
