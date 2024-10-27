from default_puzzles import *
from puzzle import Problem
from util import euclidian_distance, misplaced_tile, uniform_cost


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

    if choice == "1":
        print("\nSelect a puzzle:")
        print("1: Trivial Puzzle")
        print("2: Very Easy Puzzle")
        print("3: Easy Puzzle")
        print("4: Doable Puzzle")
        print("5: Oh Boy Puzzle")
        print("6: Impossible Puzzle")

        puzzle_choice = input("Enter your choice (1-6): ")

        if puzzle_choice == "1":
            puzzle = trivial_puzzle
            print("\nUsing Trivial Puzzle:")
        elif puzzle_choice == "2":
            puzzle = very_easy_puzzle
            print("\nUsing Very Easy Puzzle:")
        elif puzzle_choice == "3":
            puzzle = easy_puzzle
            print("\nUsing Easy Puzzle:")
        elif puzzle_choice == "4":
            puzzle = doable_puzzle
            print("\nUsing Doable Puzzle:")
        elif puzzle_choice == "5":
            puzzle = oh_boy_puzzle
            print("\nUsing Oh Boy Puzzle:")
        elif puzzle_choice == "6":
            puzzle = impossible_puzzle
            print("\nUsing Impossible Puzzle:")
        else:
            print("Invalid choice for puzzle!")
            return

    elif choice == "2":
        puzzle = get_puzzle_input()
    else:
        print("Invalid choice!")
        return

    problem = Problem(8, puzzle, uniform_cost)

    print("\nInitial State:")
    print(problem.get_initial_state())

    print("\nGoal State:")
    print(problem.get_goal_state())

    print("\nSolution")
    problem.print_solution()


if __name__ == "__main__":
    main()
