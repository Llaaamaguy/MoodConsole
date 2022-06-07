from tkinter import *
from tkinter import simpledialog
from utils import enumerate_row_column


class NumPad(simpledialog.Dialog):
    def __init__(self, master=None, textVariable=None, textHandler=None):
        self.top = Toplevel(master=master)
        self.top.protocol("WM_DELETE_WINDOW", self.ok)
        self.createWidgets()
        self.textHandler = textHandler
        self.master = master

    def createWidgets(self):
        btn_list = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0', 'Send', 'Del']
        # create and position all buttons with a for-loop
        btn = []
        # Use custom generator to give us row/column positions
        for r, c, label in enumerate_row_column(btn_list, 3):
            # partial takes care of function and argument
            cmd = lambda x=label: self.click(x)
            # create the button
            cur = Button(self.top, text=label, width=10, height=5, command=cmd)
            # position the button
            cur.grid(row=r, column=c)
            btn.append(cur)

    def click(self, label):
        if label == 'Del':
            currentText = self.master.get()
            self.master.delete(0, END)
            self.master.insert(0, currentText[:-1])
        elif label == 'Send':
            self.ok()
            endText = self.master.get()
            #send_data(endText)
            self.textHandler.text = endText
            self._root().destroy()
        else:
            currentText = self.master.get()
            self.master.delete(0, END)
            self.master.insert(0, currentText + label)

    def ok(self):
        self.top.destroy()
        self.top.master.focus()
