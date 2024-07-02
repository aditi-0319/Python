import copy
import heapq
from collections import deque
import time
import random


class Puzzle(object):
    def __init__(self, my_list, goal_list):
        self.curr_state = my_list
        self.goal_state = goal_list
        self.empty_state = []
        self.move_sym = 0
        self.m = len(self.curr_state)

    def __lt__(self, other):
        # Define comparison for heapq
        return self.heuristic_func() < other.heuristic_func()

    def up(self):
        index_mov_sym = self.curr_state.index(self.move_sym)
        if index_mov_sym - 3 >= 0:
            up_sym = self.curr_state[index_mov_sym - 3]
            index_up_sym = self.curr_state.index(up_sym)
            new_index_mov_sym = index_up_sym
            new_index_up_sym = index_mov_sym

            new_state = copy.deepcopy(self.curr_state)
            new_state[new_index_mov_sym] = self.move_sym
            new_state[new_index_up_sym] = up_sym

            return Puzzle(new_state, self.goal_state)
        else:
            return None

    def down(self):
        index_mov_sym = self.curr_state.index(self.move_sym)
        if index_mov_sym + 3 <= self.m - 1:
            down_sym = self.curr_state[index_mov_sym + 3]
            index_down_sym = self.curr_state.index(down_sym)
            new_index_mov_sym = index_down_sym
            new_index_down_sym = index_mov_sym

            new_state = copy.deepcopy(self.curr_state)
            new_state[new_index_mov_sym] = self.move_sym
            new_state[new_index_down_sym] = down_sym

            return Puzzle(new_state, self.goal_state)
        else:
            return None

    def right(self):
        index_mov_sym = self.curr_state.index(self.move_sym)
        left_most_col = []

        for i in range(len(self.curr_state)):
            if i % 3 == 0:
                left_most_col.append(i)

        for i in left_most_col:
            if i <= index_mov_sym < i + 3 - 1 and (index_mov_sym + 1) % 3 != 0:
                right_sym = self.curr_state[index_mov_sym + 1]
                new_index_mov_sym = index_mov_sym + 1

                new_state = copy.deepcopy(self.curr_state)
                new_state[new_index_mov_sym] = self.move_sym
                new_state[index_mov_sym] = right_sym

                return Puzzle(new_state, self.goal_state)

        return None

    def left(self):
        index_mov_sym = self.curr_state.index(self.move_sym)
        right_most_col = []

        for i in range(len(self.curr_state)):
            if i % 3 == 2:
                right_most_col.append(i)

        for i in right_most_col:
            if i >= index_mov_sym > i - 3 + 1 and index_mov_sym % 3 != 0:
                left_sym = self.curr_state[index_mov_sym - 1]
                new_index_mov_sym = index_mov_sym - 1

                new_state = copy.deepcopy(self.curr_state)
                new_state[new_index_mov_sym] = self.move_sym
                new_state[index_mov_sym] = left_sym

                return Puzzle(new_state, self.goal_state)

        return None

    def display_puzzle(self):
        for i in range(0, 8, 3):
            print(f"{self.curr_state[i:i + 3]}")

    def heuristic_func(self):
        c = 0
        for i in range(len(self.curr_state)):
            if self.curr_state[i] != self.goal_state[i]:
                c = c + 1
        return c


def hill_climbing_algorithm(puzzle):
    start_time = time.time()
    iteration = 1

    while True:
        h_value = puzzle.heuristic_func()

        print(f"\nIteration {iteration}")
        print(f"Heuristic Value: {h_value}")
        puzzle.display_puzzle()

        if h_value == 0:
            print("\nHill Climbing Algorithm\nThe final state is reached.")
            puzzle.display_puzzle()
            end_time = time.time()
            t = end_time - start_time
            print(f"Time taken: {t} seconds")
            return

        neighbors = [
            (puzzle.up(), 'Up'),
            (puzzle.down(), 'Down'),
            (puzzle.left(), 'Left'),
            (puzzle.right(), 'Right')
        ]

        valid_neighbors = [(neighbor[0].heuristic_func(), neighbor[0], neighbor[1])
                           for neighbor in neighbors if neighbor[0] is not None]

        valid_neighbors = sorted(valid_neighbors, key=lambda x: x[0])

        if not valid_neighbors or valid_neighbors[0][0] >= h_value:
            print("No path found to reach the final state using Hill Climbing.")
            return

        random.shuffle(valid_neighbors)

        puzzle = valid_neighbors[0][1]
        print(f"Move: {valid_neighbors[0][2]}")
        iteration += 1


def best_first_search_algorithm(puzzle):
    start_time = time.time()
    heap = [puzzle]
    visited = set()

    while heap:
        current_puzzle = heapq.heappop(heap)
        h_value = current_puzzle.heuristic_func()

        visited.add(tuple(current_puzzle.curr_state))

        if h_value == 0:
            print("\nBest First Search Algorithm\nThe final state is reached.")
            current_puzzle.display_puzzle()
            end_time = time.time()
            t = end_time - start_time
            print(f"Time taken: {t} seconds")
            return

        neighbors = [
            current_puzzle.up(),
            current_puzzle.down(),
            current_puzzle.left(),
            current_puzzle.right()
        ]

        valid_neighbors = [neighbor for neighbor in neighbors
                           if neighbor is not None and tuple(neighbor.curr_state) not in visited]

        for neighbor in valid_neighbors:
            heapq.heappush(heap, neighbor)

    print("No path found to reach the final state using Best First Search.")


my_list = [2, 8, 1, 0, 4, 3, 7, 6, 5]
goal_list = [1, 2, 3, 8, 0, 4, 7, 6, 5]

p = Puzzle(my_list, goal_list)

print("Initial Puzzle")
p.display_puzzle()
hill_climbing_algorithm(p)
best_first_search_algorithm(p)
