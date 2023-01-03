"""
Ezt a fajlt kell futtatni a program futtatasahoz.

A program a linear és binary search közötti különbségeket mutattja be grafikusan.
Véletlenszerű adatokkal dolgozik amit a "Create new dataset" gombbal ujra lehet generalni
A "Show Data" gomb segitsegevel megnezhetjuk az adatokat es a mellette levo checkbox-al eldonthetjuk, hogy ezt rendezett
vagy rendezetlen formaban tegyuk.
A "Linear Search" gombbal a linear search algoritmust abrazolja a program, szinten rendezett es rendezetlen formaban
A "Binary Search" gombbal a binary search algoritmust tudjuk abrazolni, itt nem donthetunk az adatok rendezettsegerol,
mivel az algoritmus csak rendezett adatokkal mukodik
A Time Complexity gombbal megtekinthetjuk a worst-case time complexity-et az algoritmusoknak. Ez a linear search eseten
O(n) ez azt jelenti, hogy egy n darab adatot tartalmazo adathalmazban legfeljebb n lepesre van szuksegunk ahhoz, hogy
megtalaljuk a keresett elemet.
A binary search eseten ez O(log(n)), ez azt jelenti hogy egy n nagysagu adathalmaz eseten log(n) lepesre lehet
legrosszabb esetben szuksegunk a keresett elem megtalalasahoz (a logaritmus 2-es alapu)
"""

import customtkinter
import random
from graphical_search import SearchingAlgorithms

global dataset
global rnd_target


def new_data():
    y_vals = [random.randint(0, 100000) for _ in range(100)]
    global dataset
    global rnd_target
    dataset = SearchingAlgorithms(y_vals)
    rnd_target = random.choice(dataset.y_vals)


def main():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")

    root = customtkinter.CTk()
    root.geometry("800x500")
    root.title("Searching Algorithms")
    root.iconbitmap("icon.ico")

    new_data()

    label = customtkinter.CTkLabel(master=root, text="Searching Algorithms", font=("Arial", 25))
    label.pack(pady=50)

    button = customtkinter.CTkButton(master=root, text="Create new dataset",
                                     command=new_data)
    button.pack(pady=20)

    showdata_checkbox = customtkinter.CTkCheckBox(master=root, text="sorted", font=("Arial", 16),
                                                  onvalue=True, offvalue=False)
    showdata_checkbox.place(x=450, y=200)

    button = customtkinter.CTkButton(master=root, text="Show Data",
                                     command=lambda: dataset.show_data(be_sorted=showdata_checkbox.get()))
    button.place(x=250, y=200)

    linearsearch_checkbox = customtkinter.CTkCheckBox(master=root, text="sorted", font=("Arial", 16),
                                                      onvalue=True, offvalue=False)
    linearsearch_checkbox.place(x=450, y=250)

    button = customtkinter.CTkButton(master=root, text="Linear Search",
                                     command=lambda: dataset.lienar_search_graph(rnd_target,
                                                                                 be_sorted=linearsearch_checkbox.get()))
    button.place(x=250, y=250)

    button = customtkinter.CTkButton(master=root, text="Binary Search",
                                     command=lambda: dataset.binary_search_graph(rnd_target))
    button.place(x=330, y=300)

    timecomplexity_button = customtkinter.CTkButton(master=root, text="Time Complexity",
                                                    command=SearchingAlgorithms.show_time_complexity)
    timecomplexity_button.place(x=330, y=350)

    root.mainloop()


if __name__ == "__main__":
    main()
