import heapq
import time
import math


class Grid(object):
    def __init__(self, initial, goal):
        self.curr_state = initial
        self.goal_state = goal
        self.mov_sym = 'S'
        self.m = len(self.curr_state)
        self.index_0 = self.curr_state.index(self.mov_sym)

    def __lt__(self, other):
        return self.calculate_heuristic(self.curr_state, self.goal_state) < other.calculate_heuristic(other.curr_state, other.goal_state)

    def up(self):
        if self.index_0 - 5 >= 0 and self.curr_state[self.index_0 - 5] != 1:
            up_sym = self.curr_state[self.index_0 - 5]
            new_state = self.curr_state[:]
            new_state[self.index_0 - 5] = self.mov_sym
            new_state[self.index_0] = up_sym
            return Grid(new_state, self.goal_state)
        else:
            return None

    def down(self):
        if self.index_0 + 5 <= self.m - 1 and self.curr_state[self.index_0 + 5] != 1:
            down_sym = self.curr_state[self.index_0 + 5]
            new_state = self.curr_state[:]
            new_state[self.index_0 + 5] = self.mov_sym
            new_state[self.index_0] = down_sym
            return Grid(new_state, self.goal_state)
        else:
            return None

    def left(self):
        if self.index_0 % 5 != 0 and self.curr_state[self.index_0 - 1] != 1:
            left_sym = self.curr_state[self.index_0 - 1]
            new_state = self.curr_state[:]
            new_state[self.index_0 - 1] = self.mov_sym
            new_state[self.index_0] = left_sym
            return Grid(new_state, self.goal_state)
        else:
            return None

    def right(self):
        if self.index_0 % 5 != 4 and self.curr_state[self.index_0 + 1] != 1:
            right_sym = self.curr_state[self.index_0 + 1]
            new_state = self.curr_state[:]
            new_state[self.index_0 + 1] = self.mov_sym
            new_state[self.index_0] = right_sym
            return Grid(new_state, self.goal_state)
        else:
            return None

    def display_puzzle(self):
        for i in range(0, 25, 5):
            print(f"{self.curr_state[i:i + 5]}")

    def calculate_heuristic(self, item1, item2):
        item1_coordinates = (item1.index('S') // 5, item1.index('S') % 5)

        if 'G' in item2:
            item2_coordinates = (item2.index('G') // 5, item2.index('G') % 5)
            distance = math.sqrt((item2_coordinates[0] - item1_coordinates[0]) ** 2 + (item2_coordinates[1] - item1_coordinates[1]) ** 2)
            return distance
        else:
            return float('inf')


def best_first_search(grid):
    start_time = time.time()
    heap = [grid]
    visited = set()

    while heap:
        curr_puzzle = heapq.heappop(heap)
        h_value = curr_puzzle.calculate_heuristic(curr_puzzle.curr_state, curr_puzzle.goal_state)
        visited.add(tuple(curr_puzzle.curr_state))

        if h_value == 0:
            print("\nBest First Search Algorithm\nGoal state is achieved\n")
            end_time = time.time()
            t = end_time - start_time
            print(f"Time taken: {t}")
            return

        neighbors = [
            (curr_puzzle.up()),
            (curr_puzzle.down()),
            (curr_puzzle.left()),
            (curr_puzzle.right())
        ]

        valid_neighbors = [neighbor for neighbor in neighbors if
                           neighbor is not None and tuple(neighbor.curr_state) not in visited]

        for neighbor in valid_neighbors:
            heapq.heappush(heap, neighbor)

    print("\nNo path found to reach the final state using Best First Search.")


my_list = ['S', 1, 0, 0, 'G', 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]
goal_list = [0, 1, 0, 0, 'S', 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]

g = Grid(my_list, goal_list)
print("Initial Puzzle")
g.display_puzzle()
best_first_search(g)

