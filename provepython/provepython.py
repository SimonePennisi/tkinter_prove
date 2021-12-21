import tkinter as tk

win = tk.Tk()


win.title("io sono un titolo")
win.geometry("600x600")
win.resizable(False,False)
win.config(background="white")
def first_command():
    text = "Hello World!"
    text_out = tk.Label(win, text=text, fg="red", font=("Hevetica",20))
    text_out.grid(row=0,column=1)

    first_button = tk.Button(text="Ok, sei strano", command=second_command)
    first_button.grid(row=1,column=0)


def second_command():
    text = "Mi chiamo ambrogio"
    text_out = tk.Label(win, text=text, fg="green", font=("Hevetica",20))
    text_out.grid(row=0,column=1,padx=100)

first_button = tk.Button(text="saluta", command=first_command)
first_button.grid(row=0,column=0)












if __name__ == "__main__":
    win.mainloop()

