class WaterJugProblem:
    def __init__(self):
        self.jug1_capacity = 3
        self.jug2_capacity = 4
        self.jug1_current = 0
        self.jug2_current = 0

    def fill_jug1(self):
        if self.jug1_current <= self.jug1_capacity:
            remaining_capacity = self.jug1_capacity - self.jug1_current
            self.jug1_current += remaining_capacity
            print(f"New capacity of Jug 1 (3L): {self.jug1_current}  |  Capacity of Jug 2 (4L): {self.jug2_current}\n")
        else:
            print("Capacity of Jug 1 if full!\n")

    def fill_jug2(self):
        if self.jug2_current <= self.jug2_capacity:
            remaining_capacity = self.jug2_capacity - self.jug2_current
            self.jug2_current += remaining_capacity
            print(f"Capacity of Jug 1 (3L): {self.jug1_current}  |  New capacity of Jug 2 (4L): {self.jug2_current}\n")
        else:
            print("Capacity of Jug 2 (4L) if full!\n")

    def empty_jug1(self):
        if self.jug1_current > 0:
            self.jug1_current -= self.jug1_current
            print(f"New capacity of Jug 1 (3L): {self.jug1_current}  |  Capacity of Jug 2: {self.jug2_current}\n")
        else:
            print("Jug 1 (3L) is empty!\n")

    def empty_jug2(self):
        if self.jug2_current > 0:
            self.jug2_current -= self.jug2_current
            print(f"Capacity of Jug 1 (3L): {self.jug1_current}  |  New capacity of Jug 2 (4L): {self.jug2_current}\n")
        else:
            print("Jug 2 (4L) is empty!\n")

    def water_from_jug1_to_jug2(self):
        if self.jug2_current < self.jug2_capacity and self.jug1_current > 0:
            remaining_capacity_2 = self.jug2_capacity - self.jug2_current
            poured_amount = min(self.jug1_current, remaining_capacity_2)

            self.jug2_current += poured_amount
            self.jug1_current -= poured_amount

            print(f"Capacity of Jug 1 (3L): {self.jug1_current} | New capacity of Jug 2 (4L): {self.jug2_current}\n")
        elif self.jug2_current >= self.jug2_capacity:
            print("Capacity of Jug 2 (4L) is full!\n")
        elif self.jug1_current <= 0:
            print("Jug 1 (3L) is empty!\n")

    def water_from_jug2_to_jug1(self):
        if self.jug1_current < self.jug1_capacity and self.jug2_current > 0:
            remaining_capacity_1 = self.jug1_capacity - self.jug1_current
            poured_amount = min(self.jug2_current, remaining_capacity_1)

            self.jug1_current += poured_amount
            self.jug2_current -= poured_amount

            print(f"New capacity of Jug 1 (3L): {self.jug1_current} | Capacity of Jug 2 (4L): {self.jug2_current}\n")
        elif self.jug1_current >= self.jug1_capacity:
            print("Capacity of Jug 1 (3L) is full!\n")
        elif self.jug2_current <= 0:
            print("Jug 2 (4L) is empty!\n")


w = WaterJugProblem()
w.fill_jug1()
w.water_from_jug1_to_jug2()
w.fill_jug1()
w.water_from_jug1_to_jug2()
w.empty_jug2()
w.water_from_jug1_to_jug2()
