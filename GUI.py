import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.label = tk.Label(self)
        self.label.grid(row=0, column=0)

        sv = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=sv)
        self.entry.grid(row=1, column=0)
        sv.trace("w", lambda name, index, mode, sv=sv: self.callback(sv, self.label))

    def callback(self, sv, label):
        try:
            text = eval(sv.get())
        except:
            text = ""
        label.config(text=text)
