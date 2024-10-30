from default_puzzles import *
from puzzle import Problem
from util import euclidean_distance, misplaced_tile, uniform_cost

puzzle_type = 8

def get_puzzle_input() -> list:
    puzzle = []
    print("\nEnter your puzzle, use a zero to represent the blank")
    for i in range(1, int((puzzle_type + 1)**(0.5)) + 1):
        row = input(f"Enter row {i}, use space or tabs between numbers: ")
        puzzle.extend([int(x) for x in row.split()])
    return puzzle


def main() -> None:
    puzzle = []
    algorithm = None

    print(f"Welcome to Ram and Samyak 8 puzzle solver.")
    print("Type '1' to use a default puzzle, or '2' to enter your own puzzle.\n")

    choice = input("Enter choice (1 for default, 2 for custom): ")

    if choice == "1":
        print("\nSelect a puzzle:")
        print("1: Trivial Puzzle")
        print("2: Very Easy Puzzle")
        print("3: Easy Puzzle")
        print("4: Doable Puzzle")
        print("5: Oh Boy Puzzle")
        print("6: Impossible Puzzle")
        print("7: 15-puzzle (MAKE SURE PUZZLE_TYPE CHANGED)")

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
        elif puzzle_choice == "7":
            puzzle = fifteen_puzzle
            print("\nUsing 15-puzzle:")
        else:
            print("Invalid choice for puzzle!")
            return

    elif choice == "2":
        puzzle = get_puzzle_input()
    else:
        print("Invalid choice!")
        return

    print("\nEnter the search algorithm you would like to use:")
    print("1: Uniform Cost Search")
    print("2: A* with the Misplaced Tile heuristic")
    print("3: A* with the Euclidean distance heuristic")

    algo_choice = input("Enter your choice (1-3): ")
    if algo_choice == "1":
        algorithm = uniform_cost
        print("\nUsing Uniform Cost Search.")
    elif algo_choice == "2":
        algorithm = misplaced_tile
        print("\nUsing A* with the Misplaced Tile heuristic.")
    elif algo_choice == "3":
        algorithm = euclidean_distance
        print("\nUsing A* with the Euclidean distance heuristic.")
    else:
        print("Invalid choice for algorithm!")
        return

    problem = Problem(puzzle_type, puzzle, algorithm)

    print("\nSolution: ")
    print()
    problem.print_solution()


if __name__ == "__main__":
    main()
