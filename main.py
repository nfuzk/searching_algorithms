import time

import matplotlib.pyplot as plt
import random


class Timer:
    def __init__(self):
        self.start_time = time.perf_counter_ns()

    def end(self):
        runtime = time.perf_counter_ns() - self.start_time
        print(f"{runtime} ns")
        print(f"{runtime*10**-6:.5f} ms")


class SearchingAlgorithms:

    def __init__(self, y_vals: list):
        self.y_vals = y_vals
        self.x_vals = [i for i in range(len(y_vals))]

    def show_data(self, be_sorted: bool = False):
        plt.figure(num='Adatok')
        if be_sorted:
            plt.bar(self.x_vals, sorted(self.y_vals), color="lightblue")
            plt.title("Adatok rendezve")
        else:
            plt.bar(self.x_vals, self.y_vals, color="lightblue")
            plt.title("Adatok rendezetlenul")
        plt.show()

    def linear_search(self, target: int) -> int:
        timer = Timer()
        for i, n in enumerate(self.y_vals):
            if n == target:
                timer.end()
                return i

    def lienar_search_graph(self, target: int):
        plt.figure(num='Linear Seach')
        b_list = plt.bar(self.x_vals, self.y_vals, color="lightblue")
        plt.title("Linear Search")

        for i, n in enumerate(self.y_vals):
            b_list[i].set_color("green")
            plt.pause(0.1)
            if n == target:
                plt.title(f"A keresett elem indexe: {i}")
                plt.show()
                return

    def binary_search(self, target: int) -> int:
        self.y_vals.sort()

        timer = Timer()
        left_pointer = 0
        right_pointer = len(self.y_vals) - 1

        while left_pointer < right_pointer:
            middle_pointer = (left_pointer + right_pointer) // 2

            if self.y_vals[middle_pointer] == target:
                timer.end()
                return middle_pointer
            if self.y_vals[middle_pointer] > target:
                right_pointer = middle_pointer
            else:
                left_pointer = middle_pointer

    def binary_search_graph(self, target: int):
        self.y_vals.sort()

        left_pointer = 0
        right_pointer = len(self.y_vals) - 1

        while left_pointer < right_pointer:
            middle_pointer = (left_pointer + right_pointer) // 2

            plt.figure(num='Binary Search')
            plt.clf()
            plt.bar(self.x_vals[left_pointer:right_pointer], self.y_vals[left_pointer:right_pointer], color="lightblue")
            plt.locator_params(axis="x", integer=True)
            plt.title("Binary Search")
            plt.pause(1)

            if self.y_vals[middle_pointer] == target:
                plt.clf()
                colors = ["green" if y == target else "lightblue" for y in self.y_vals[left_pointer:right_pointer]]
                plt.bar(self.x_vals[left_pointer:right_pointer], self.y_vals[left_pointer:right_pointer], color=colors)
                plt.locator_params(axis="x", integer=True)
                plt.title(f"A keresett elem indexe: {middle_pointer}")
                plt.show()
                return
            if self.y_vals[middle_pointer] > target:
                right_pointer = middle_pointer
            else:
                left_pointer = middle_pointer


def main():
    y_values = [random.randint(0, 100000) for _ in range(100)]
    dataset = SearchingAlgorithms(y_values)

    while True:
        print("0. Adatok frissitese\n\
1. Adatok megtekintése\n\
2. Linear Search\n\
3. Binary Search\n\
4. Linear Search abrazolasa\n\
5. Binary Search abrazolasa\n\
9. KILEPES")
        desired_option = int(input("valasz:\t"))
        if desired_option == 0:
            y_values = [random.randint(0, 100000) for _ in range(100)]
            dataset = SearchingAlgorithms(y_values)
        elif desired_option == 1:
            be_sorted: bool = input("Rendezve legyenek az adatopk? (y/n)\t") == "y"
            dataset.show_data(be_sorted=be_sorted)
        elif desired_option == 2:
            dataset.linear_search(y_values[86])
        elif desired_option == 3:
            dataset.binary_search(y_values[86])
        elif desired_option == 4:
            dataset.lienar_search_graph(y_values[86])
        elif desired_option == 5:
            dataset.binary_search_graph(y_values[86])
        elif desired_option == 9:
            break


if __name__ == "__main__":
    main()
