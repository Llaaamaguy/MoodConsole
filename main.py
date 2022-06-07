from tkinter import *
from TextHandler import TextHandler
from App import App


def main():
    root = Tk()
    textHandler = TextHandler()
    root.geometry("200x250")
    app = App(root, textHandler=textHandler)
    app.grid()
    root.mainloop()
    print(textHandler.getText())
    return True


if __name__ == "__main__":
    while main(): pass
