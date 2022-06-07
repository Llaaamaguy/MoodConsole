from tkinter import *
from NumpadEntry import NumpadEntry


class App(Frame):
    def __init__(self, parent=None, textHandler=None, **kw):
        Frame.__init__(self, parent, **kw)
        self.textEntryVar1 = StringVar()
        self.e1 = NumpadEntry(self, textvariable=self.textEntryVar1, textHandler=textHandler)
        self.e1.grid()
