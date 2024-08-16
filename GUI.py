from tkinter import *
from tkinter import Button

def calculate_pi(num):
    pi = 0
    for i in range(num):
        pi += (1 / 16**i) * (4 / (8*i + 1) - 2 / (8*i + 4) - 1 / (8*i + 5) - 1 / (8*i + 6))
    return pi

def safe_check():
    x = int(entry1.get())
    if x > 65:
        return disMessage.config(text="Exceeded safety parameters.")
    else:
        pi_value = (calculate_pi(x))
        disMessage.config(text = f"PI to the {x}th digit: {pi_value:.{x}f}")



mainGUI = Tk()

Label(mainGUI, text = 'Enter a Integer').grid(row=0, column=0)
entry1 = Entry(mainGUI)
entry1.grid(row=0,column=1)

button = Button(mainGUI, text = 'Calculate π', command = safe_check)
button.grid(row=1, column=0, columnspan=2)

disMessage = Message(mainGUI, text = "", width=400)
disMessage.config(bg='light green')
disMessage.grid(row=2, column=0, columnspan=2)

mainGUI.mainloop()