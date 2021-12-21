import tkinter as tk

win = tk.Tk()


win.title("io sono un titolo")
win.geometry("600x600")
win.resizable(False,False)
win.config(background="white")
def first_command():
    text = "Hello World!"
    text_out = tk.Label(win, text=text, fg="red", font=("Hevetica",10))
    text_out.grid(row=0,column=1,sticky="W")

    second_button = tk.Button(text="Presenta", command=second_command)
    second_button.grid(row=1,column=0, sticky="W")


def second_command():
    text = "Mi chiamo ambrogio"
    text_out = tk.Label(win, text=text, fg="green", font=("Hevetica",10))
    text_out.grid(row=1,column=1,sticky="W")

first_button = tk.Button(text="saluta", command=first_command)
first_button.grid(row=0,column=0, sticky="W")




#gatto







if __name__ == "__main__":
    win.mainloop()

