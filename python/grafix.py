from Tkinter import *


def about():
    a = Toplevel()
    a.geometry('600x600')
    a['bg'] = 'gray'
    a.overrideredirect(True)
    Label(a, text="This is a visualiser for lem in by a cghael && ksemele!").pack(expand=1)
    a.after(7000, lambda: a.destroy())  # autokill window after 1000 ms


def init_window():
    root = Tk()
    root.geometry('600x600')
    root.title("lemin visualiser v 0.1")

    Button(text="Button", width=20).pack()
    Label(text="Label", width=20, height=3).pack()
    Button(text="About", width=20, command=about).pack()

    root.mainloop()
