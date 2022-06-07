from tkinter import *
from NumPad import NumPad


class NumpadEntry(Entry):
    def __init__(self, parent=None, textHandler=None, **kw):
        Entry.__init__(self, parent, **kw)
        self.bind('<FocusIn>', self.numpadEntry)
        self.bind('<FocusOut>', self.numpadExit)
        self.edited = False
        self.textHandler = textHandler

    def numpadEntry(self, event):
        if self.edited == False:
            # OnClick event
            self['bg'] = '#ffffcc'
            self.edited = True
            new = NumPad(self, textHandler=self.textHandler)
        else:
            self.edited = False

    def numpadExit(self, event):
        self['bg'] = '#ffffff'
