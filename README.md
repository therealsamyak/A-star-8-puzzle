# A-star-8-puzzle

## Instructions

Clone this repository and navigate to its directory in the terminal.

The driver is in `main.py`, so the program can be executed by doing:

```
python3 main.py
```

## Output

Sample output is shown for _Easy Puzzle_, and _A\* search with the Euclidean distance heuristic_.

```
Welcome to Ram and Samyak 8 puzzle solver.
Type '1' to use a default puzzle, or '2' to enter your own puzzle.

Enter choice (1 for default, 2 for custom): 1

Select a puzzle:
1: Trivial Puzzle
2: Very Easy Puzzle
3: Easy Puzzle
4: Doable Puzzle
5: Oh Boy Puzzle
6: Impossible Puzzle
Enter your choice (1-6): 3

Using Easy Puzzle:

Enter the search algorithm you would like to use:
1: Uniform Cost Search
2: A* with the Misplaced Tile heuristic
3: A* with the Euclidean distance heuristic
Enter your choice (1-3): 3

Using A\* with the Euclidean distance heuristic.

Solution:
Best state to expand with g(n) = 0 and h(n) = 2.0 is:
1 2 0
4 5 3
7 8 6
Expanding...

Best state to expand with g(n) = 1 and h(n) = 1.0 is:
1 2 3
4 5 0
7 8 6
Expanding...

Best state to expand with g(n) = 2 and h(n) = 0.0 is:
1 2 3
4 5 6
7 8 0
Expanding...

To solve this problem, the search algorithm expanded a total of 4 nodes
Max nodes in queue at any given time: 3
Time taken to solve: 0.0010085105895996094
```
