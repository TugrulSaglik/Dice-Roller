import tkinter as tk
import random

main = tk.Tk()

custom_font = ("Times New Roman", 15)

def roll_dice():
    random1 = random.randint(1, 6)
    random2 = random.randint(1, 6)
    total = random1 + random2
    if random1 == random2:
        cik = "çift"
    else:
        cik = "tek"
    label2.config(text = f"Zarın değeri {total} ve zar {cik}.")
    return

label1 = tk.Label(
    text = "Zar atmak için alttaki butona basın. Size toplam değeri ve tek mi çift mi olduğunu söyleyecek. ",
    font = custom_font
    )

button = tk.Button(
   text = "Zar at!",
   command = roll_dice
)

label2 = tk.Label(
    text = "",
    font = custom_font
)

label1.pack()
button.pack()
label2.pack()

main.mainloop()