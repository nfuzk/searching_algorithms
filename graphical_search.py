"""
A program futtatasahoz a main.py fajlt kell futtatni!
"""

import matplotlib.pyplot as plt
import numpy as np


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

    def lienar_search_graph(self, target: int, be_sorted: bool = False) -> None:

        if be_sorted:
            y_vals = sorted(self.y_vals)
        else:
            y_vals = self.y_vals

        plt.figure(num='Linear Seach')
        b_list = plt.bar(self.x_vals, y_vals, color="lightblue")
        plt.title("Linear Search")

        for i, n in enumerate(y_vals):
            b_list[i].set_color("green")
            plt.pause(0.1)
            if n == target:
                plt.title(f"A keresett elem indexe: {i}")
                plt.show()
                return

    def binary_search_graph(self, target: int) -> None:
        y_vals = sorted(self.y_vals)

        left_pointer = 0
        right_pointer = len(y_vals) - 1

        while left_pointer < right_pointer:
            middle_pointer = (left_pointer + right_pointer) // 2

            plt.figure(num='Binary Search')
            plt.clf()
            plt.bar(self.x_vals[left_pointer:right_pointer], y_vals[left_pointer:right_pointer], color="lightblue")
            plt.locator_params(axis="x", integer=True)
            plt.title("Binary Search")
            plt.pause(1)

            if y_vals[middle_pointer] == target:
                plt.clf()
                colors = ["green" if y == target else "lightblue" for y in y_vals[left_pointer:right_pointer]]
                plt.bar(self.x_vals[left_pointer:right_pointer], y_vals[left_pointer:right_pointer], color=colors)
                plt.locator_params(axis="x", integer=True)
                plt.title(f"A keresett elem indexe: {middle_pointer}")
                plt.show()
                return
            if y_vals[middle_pointer] > target:
                right_pointer = middle_pointer
            else:
                left_pointer = middle_pointer

    @staticmethod
    def show_time_complexity():
        vals = [x for x in range(1, 101)]

        plt.figure(num="Worst-Case Time Complexity")
        plt.title("Worst-Case Time Complexity")
        plt.plot(np.log2(vals))
        plt.plot(vals)
        plt.legend(["O(log(n))", "O(n)"])

        plt.show()
