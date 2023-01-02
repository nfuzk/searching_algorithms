import matplotlib.pyplot as plt
import random


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
        for i, n in enumerate(self.y_vals):
            if n == target:
                return i

    def lienar_search_graph(self, target: int) -> int:
        plt.figure(num='Linear Seach')
        b_list = plt.bar(self.x_vals, self.y_vals, color="lightblue")
        plt.title("Linear Search")

        for i, n in enumerate(self.y_vals):
            b_list[i].set_color("green")
            plt.pause(0.1)
            if n == target:
                plt.title(f"A keresett elem indexe: {i}")
                plt.show()
                return i

    def binary_search(self, target: int) -> int:
        self.y_vals.sort()

        left_pointer = 0
        right_pointer = len(self.y_vals) - 1

        while left_pointer < right_pointer:
            middle_pointer = (left_pointer + right_pointer) // 2

            if self.y_vals[middle_pointer] == target:
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
                return middle_pointer
            if self.y_vals[middle_pointer] > target:
                right_pointer = middle_pointer
            else:
                left_pointer = middle_pointer


def main():
    y_values = [random.randint(0, 100000) for _ in range(100)]
    dataset = SearchingAlgorithms(y_values)

    dataset.show_data(be_sorted=True)

    dataset.lienar_search_graph(y_values[86])
    dataset.binary_search_graph(y_values[86])


if __name__ == "__main__":
    main()
