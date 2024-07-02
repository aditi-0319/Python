class Puzzle(object):
    def __init__(self):
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
        else:
            print("\nNo space! Cannot move up.")

    def down(self):
        index_mov_sym = self.curr_state.index(self.move_sym)
        if index_mov_sym + 3 <= self.m - 1:
            down_sym = self.curr_state[index_mov_sym + 3]
            index_down_sym = self.curr_state.index(down_sym)
            new_index_mov_sym = index_down_sym
            new_index_down_sym = index_mov_sym

            self.curr_state[new_index_mov_sym] = self.move_sym
            self.curr_state[new_index_down_sym] = down_sym
        else:
            print("\nNo space! Cannot move down.")

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
                return

        print("\nNo space! Cannot move right.")

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
                return

        print("\nNo space! Cannot move left.")

    def display_puzzle(self):
        for i in range(0, 8, 3):
            print(f"{self.curr_state[i:i + 3]}")


my_list = [2, 8, 1, 0, 4, 3, 7, 6, 5]
goal_list = [1, 2, 3, 8, 0, 4, 7, 6, 5]

p = Puzzle()
p.display_puzzle()
p.up()
print("\n")
p.display_puzzle()

p.right()
print("\n")
p.display_puzzle()

p.right()
print("\n")
p.display_puzzle()

p.down()
print("\n")
p.display_puzzle()

p.left()
print("\n")
p.display_puzzle()

p.left()
print("\n")
p.display_puzzle()

p.up()
print("\n")
p.display_puzzle()

p.right()
print("\n")
p.display_puzzle()

p.down()
print("\n")
p.display_puzzle()
