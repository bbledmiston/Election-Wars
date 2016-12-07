import tkinter
# import "tkinter" messagebox
# import twoelectionwars
from twoelectionwars import *


class Controller:

    def __init__(self):
        self.__mainWindow = tkinter.Tk()
        self.__mainWindow.title ('Controller')
        self.top_frame = tkinter.Frame(self.__mainWindow)
        self.bottom_frame = tkinter.Frame(self.__mainWindow)
        self.__label = tkinter.Label(self.top_frame, text="Label")

        self.__label2 = tkinter.Label(self.bottom_frame, text="I am also a label")

        self.__button1 = tkinter.Button(self.__mainWindow, \
                                            text="A", \
                                            command=self.doSomething)
        self.__button2 = tkinter.Button(self.__mainWindow, \
                                            text="B", \
                                            command=self.doSomething)


        #packing automatically stacks based on order
        self.top_frame.pack() #frames have to be packed first
        self.bottom_frame.pack()
        self.__label.pack()
        self.__label2.pack()
        self.__button1.pack(side="left")
        self.__button2.pack(side="right")

        # tk = tkinter.Tk()

        tkinter.mainloop()

    # def createWidgets(self):
    #     errythang = Events.present()

    def doSomething(self):
        tkinter.messagebox.showinfo("stop it", "please don't do that")

#string vars - tkinter
def main():
    c = Controller()
    e = Events.present()
    print(e)
main()
