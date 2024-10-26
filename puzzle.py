class Node:
    def __init__(self, cutoff: int, state: list, score_func: callable, parent: 'Node' = None) -> None:
        self.parent = parent
        self.state = state
        
        self.cutoff = cutoff
        self.score = score_func(state)

    def __lt__(self, other: 'Node'):
        return self.score < other.score
    
    def __repr__(self):
        result = ""
        for tile in range(len(self.state)):
            result += str(self.state[tile]) + " "
            if (tile + 1) % self.cutoff == 0 and tile != len(self.state) - 1:
                result += "\n"
        return result

class Problem:
    def __init__(self, cutoff: int, initial_state: list, heuristic: callable) -> None:
        # row width
        self.cutoff = cutoff
              
        # heuristic function
        self.heuristic = heuristic

        # states
        self.initial_state = Node(cutoff, initial_state, heuristic)
        self.goal_state = Node(cutoff, [(i + 1) % (cutoff**2) for i in range(cutoff**2)], heuristic)
    
    def get_initial_state(self):
        return self.initial_state
    
    def get_goal_state(self):
        return self.goal_state
