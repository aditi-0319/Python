import time
import copy

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

            new_state = copy.deepcopy(self.curr_state)
            new_state[new_index_mov_sym] = self.move_sym
            new_state[new_index_up_sym] = up_sym

            return Puzzle(new_state, self.goal_state)
        else:
            print("\nNo space! Cannot move up.")
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
            print("\nNo space! Cannot move down.")
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

        print("\nNo space! Cannot move right.")
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

        print("\nNo space! Cannot move left.")
        return None

    def display_puzzle(self):
        for i in range(0, 8, 3):
            print(f"{self.curr_state[i:i + 3]}")

    def heuristic_estimate(self):
        c = 0
        for i in range(len(self.curr_state)):
            if self.curr_state[i] != self.goal_state[i]:
                c += 1
        return c

    def heuristic_cost(self):
        c = 0
        for i in range(len(self.curr_state)):
            if self.curr_state[i] != my_list[i]:
                c += 1
        return c


def display_puzzle_heuristic(puzzle):
    print("Puzzle:", puzzle.curr_state, "  Heuristic Estimate:", puzzle.heuristic_estimate(), "  Heuristic Cost:", puzzle.heuristic_cost(), "\n")


def a_star_algorithm(puzzle):
    start_time = time.time()
    heap = [puzzle]
    visited = set()

    while heap:
        current_puzzle = heap.pop(0)
        visited.add(tuple(current_puzzle.curr_state))

        if tuple(current_puzzle.curr_state) == tuple(goal_list):
            print("\nA* Algorithm\nThe final state is reached.")
            current_puzzle.display_puzzle()
            end_time = time.time()
            t = end_time - start_time
            print(f"\nTime taken: {t} seconds")
            return True

        neighbors = [
            current_puzzle.up(),
            current_puzzle.down(),
            current_puzzle.left(),
            current_puzzle.right()
        ]

        valid_neighbors = [neighbor for neighbor in neighbors
                           if neighbor is not None and tuple(neighbor.curr_state) not in visited]

        for neighbor in valid_neighbors:
            heap.append(neighbor)

        heap.sort(key=lambda x: x.heuristic_cost() + x.heuristic_estimate())

    print("No path found to reach the final state using A* Algorithm.")


my_list = [2, 8, 1, 0, 4, 3, 7, 6, 5]
goal_list = [1, 2, 3, 8, 0, 4, 7, 6, 5]

p = Puzzle(copy.deepcopy(my_list), copy.deepcopy(goal_list))

print("Initial Puzzle State")
p.display_puzzle()
a_star_algorithm(p)
