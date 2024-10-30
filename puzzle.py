from queue import PriorityQueue
from time import time

from node import Node


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

        self.solvable = self.solve()

    def get_initial_state(self) -> Node:
        return self.initial_state

    def get_goal_state(self) -> Node:
        return self.goal_state

    def print_stats(self):
        print(f"The search algorithm expanded a total of {self.nodes_expanded} nodes")
        print(f"Max nodes in queue at any given time: {self.max_queue_length}")
        print(f"Time taken to solve: " + str(self.time_taken))

    def backtrack(self, node: Node) -> None:
        self.solution_path.clear()
        while node is not None:
            self.solution_path.append(node)
            node = node.parent

        self.solution_path.reverse()

    def print_solution(self) -> None:
        if not self.solvable:
            print("No solution possible!")
            print()
            self.print_stats()
            return

        for state in self.solution_path:
            print(
                f"Best state to expand with g(n) = {state.depth} and h(n) = {state.heuristic_score} is:"
            )
            print(state)
            print("Expanding...")
            print()

        self.print_stats()

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
                    curr_state.depth + 1,
                    self.cutoff,
                    move_state,
                    self.heuristic,
                    curr_state,
                )
                if child_node not in frontier_set and child_node not in visited:
                    frontier.put(child_node)
                    frontier_set.add(child_node)

        if frontier.empty():
            self.time_taken = time() - start
            return False
