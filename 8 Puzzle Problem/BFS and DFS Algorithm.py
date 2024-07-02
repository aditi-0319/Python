import copy
from collections import deque
import time


class Puzzle(object):
    def __init__(self, my_list, goal_list):
        self.curr_state = my_list
        self.goal_state = goal_list
        self.empty_state = []
        self.move_sym = 0
        self.m = len(self.curr_state)

    def up(self):
        index_mov_sym = self.curr_state.index(self.move_sym)
        if index_mov_sym - 3 >= 0:
            up_sym = self.curr_state[index_mov_sym - 3]
            index_up_sym = self.curr_state.index(up_sym)
            new_index_mov_sym = index_up_sym
            new_index_up_sym = index_mov_sym

            self.curr_state[new_index_mov_sym] = self.move_sym
            self.curr_state[new_index_up_sym] = up_sym
            return True
        else:
            return False

    def down(self):
        index_mov_sym = self.curr_state.index(self.move_sym)
        if index_mov_sym + 3 <= self.m - 1:
            down_sym = self.curr_state[index_mov_sym + 3]
            index_down_sym = self.curr_state.index(down_sym)
            new_index_mov_sym = index_down_sym
            new_index_down_sym = index_mov_sym

            self.curr_state[new_index_mov_sym] = self.move_sym
            self.curr_state[new_index_down_sym] = down_sym
            return True
        else:
            return False

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

                self.curr_state[new_index_mov_sym] = self.move_sym
                self.curr_state[index_mov_sym] = right_sym
                return True

        return False

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

                self.curr_state[new_index_mov_sym] = self.move_sym
                self.curr_state[index_mov_sym] = left_sym
                return True

        return False

    def display_puzzle(self):
        for i in range(0, 8, 3):
            print(f"{self.curr_state[i:i + 3]}")


def bfs_algorithm(puzzle):
    queue = deque()
    visited = set()
    queue.append(puzzle)
    start_time = time.time()
    while queue:
        current_puzzle = queue.popleft()
        visited.add(tuple(current_puzzle.curr_state))

        if current_puzzle.curr_state == goal_list:
            print("\nBFS Algorithm\nThe final state is reached.")
            current_puzzle.display_puzzle()
            end_time = time.time()
            t = end_time - start_time
            print(f"Time taken: {t} seconds")
            return

        new_puzzles = []

        if current_puzzle.left():
            new_puzzles.append(copy.deepcopy(current_puzzle))
            current_puzzle.right()

        if current_puzzle.up():
            new_puzzles.append(copy.deepcopy(current_puzzle))
            current_puzzle.down()

        if current_puzzle.right():
            new_puzzles.append(copy.deepcopy(current_puzzle))
            current_puzzle.left()

        if current_puzzle.down():
            new_puzzles.append(copy.deepcopy(current_puzzle))
            current_puzzle.up()

        for new_puzzle in new_puzzles:
            state_tuple = tuple(new_puzzle.curr_state)
            if state_tuple not in visited:
                queue.append(new_puzzle)
                visited.add(state_tuple)

    print("No path found to reach the final state using BFS.")


def dfs_algorithm(puzzle):
    stack = []
    visited = set()
    stack.append(puzzle)
    start_time = time.time()
    while stack:
        current_puzzle = stack.pop()
        visited.add(tuple(current_puzzle.curr_state))

        if current_puzzle.curr_state == goal_list:
            print("\nDFS Algorithm\nThe final state is reached.")
            current_puzzle.display_puzzle()
            end_time = time.time()
            t = end_time - start_time
            print(f"Time taken: {t} seconds")
            return

        new_puzzles = []

        if current_puzzle.left():
            new_puzzles.append(copy.deepcopy(current_puzzle))
            current_puzzle.right()

        if current_puzzle.up():
            new_puzzles.append(copy.deepcopy(current_puzzle))
            current_puzzle.down()

        if current_puzzle.right():
            new_puzzles.append(copy.deepcopy(current_puzzle))
            current_puzzle.left()

        if current_puzzle.down():
            new_puzzles.append(copy.deepcopy(current_puzzle))
            current_puzzle.up()

        for new_puzzle in new_puzzles:
            state_tuple = tuple(new_puzzle.curr_state)
            if state_tuple not in visited:
                stack.append(new_puzzle)
                visited.add(state_tuple)

    print("No path found to reach the final state using DFS.")


my_list = [2, 8, 1, 0, 4, 3, 7, 6, 5]
goal_list = [1, 2, 3, 8, 0, 4, 7, 6, 5]

p = Puzzle(my_list, goal_list)

print("Initial Puzzle")
p.display_puzzle()
bfs_algorithm(p)
dfs_algorithm(p)
