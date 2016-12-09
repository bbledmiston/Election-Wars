import tkinter
import json
# import controller

class EnterScreen:

    def __init__(self):
        self.__mainWindow = tkinter.Tk()
        self.__mainWindow.title("test")
        self.frame = tkinter.Frame(self.__mainWindow)
        self.__userlabel = tkinter.Label(self.frame, text = "Enter your username: ")
        # self.__username = tkinter.StringVar()
        self.__usernameentry = tkinter.Entry(self.frame)
        # self.__usernameentry.grid(row=0, column=10)

        self.__enterbutton = tkinter.Button(self.frame,\
                                    text="Submit",\
                                    command=self.createUser())

        # self.__enterbutton.bind('<Return>', get)
        self.__enterbutton.pack()
        self.__userlabel.pack(side="left")
        self.__usernameentry.pack()
        self.frame.pack(padx = 60, pady = 60, side="left")

        # print(self.__username.get())

        # tkinter.mainloop()

    def createUser(self):
        print(self.__usernameentry.get())
        infile = open("username.json","a")
        json.dump(self.__username.get(), infile)
        infile.close()




def main():
    e = EnterScreen()
    tkinter.mainloop()
main()
