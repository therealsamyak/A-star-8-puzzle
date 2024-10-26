#file

#imports here
from puzzle import *
from util import *

def welcome_message():
    print(f"Welcome to Ram and Samyak 8 puzzle solver.")
    print("Type '1' to use a default puzzle, or '2' to enter your own puzzle.\n")

def get_puzzle_input():
    puzzle = []
    print("\nEnter your puzzle, use a zero to represent the blank")
    for i in range(1, 4):
        row = input(f"Enter row {i}, use space or tabs between numbers: ")
        puzzle.extend([int(x) for x in row.split()])
    return puzzle

def main():
    puzzle = []

    welcome_message()
    
    choice = input("Enter choice (1 for default, 2 for custom): ")
    if choice == '1':
        puzzle = [1, 2, 3, 4, 8, 0, 7, 6, 5]  # default puzzle
        print("\nUsing default puzzle:")
    elif choice == '2':
        puzzle = get_puzzle_input()
    else:
        print("Invalid choice!")
        return

    problem = Problem(3, puzzle, uniform_cost_heuristic)

    print("\nInitial State:")
    print(problem.get_initial_state())
    
    print("\nGoal State:")
    print(problem.get_goal_state())

if __name__ == "__main__":
    main()
