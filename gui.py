import customtkinter
import random
from main import SearchingAlgorithms


def welcome(name):
    print(f"Hi {name}!")


def main():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")

    root = customtkinter.CTk()
    root.geometry("800x500")
    root.title("Test")
    root.iconbitmap("icon.ico")

    y_values = [random.randint(0, 100000) for _ in range(100)]
    dataset = SearchingAlgorithms(y_values)

    label = customtkinter.CTkLabel(master=root, text="Searching Algorithms", font=("Arial", 25))
    label.pack(pady=50)

    button = customtkinter.CTkButton(master=root, text="Show Data", command=lambda: dataset.show_data(be_sorted=True))
    button.pack(pady=20)

    button = customtkinter.CTkButton(master=root, text="Linear Search Graph",
                                     command=lambda: dataset.lienar_search_graph(y_values[86]))
    button.pack(pady=20)

    button = customtkinter.CTkButton(master=root, text="Binary Search Graph",
                                     command=lambda: dataset.binary_search_graph(y_values[86]))
    button.pack(pady=20)

    button = customtkinter.CTkButton(master=root, text="Show Data", command=lambda: dataset.show_data(be_sorted=True))
    button.pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    main()
