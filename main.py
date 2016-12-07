import tkinter
import twoelectionwars

class Controller:

    def __init__(self):
        self.__mainWindow = tkinter.Tk()
        self.__mainWindow.title ('Controller')
        self.top_frame = tkinter.Frame(self.__mainWindow)
        self.bottom_frame = tkinter.Frame(self.__mainWindow)
        self.questionList = ["a","b","c","d"]
        self.choiceList = ["Choice A or Choice B","Choice C or Choice D","Choice A or Choice B","Choice C or Choice D"]
        self.buttonpressed = False
        self.index = 0
        for i in range(len(self.questionList)):
            self.question = self.questionList[self.index]
            self.choice = self.choiceList[self.index]
            self.__test = twoelectionwars.twoelectionwars(0,self.question,"a. Nah","b. I don't think so",1,-1)
            # print(self.__test.rating1)
            self.__label = tkinter.Label(self.top_frame, text=self.question)
            self.__label2 = tkinter.Label(self.bottom_frame, text=self.choice)

            self.__button1 = tkinter.Button(self.__mainWindow, \
                                                text="A", \
                                                command=self.ratingcalc
                                                )
            self.__button2 = tkinter.Button(self.__mainWindow, \
                                                text="B", \
                                                command=self.ratingcalc
                                                )


        self.top_frame.pack() #frames have to be packed first
        self.bottom_frame.pack()
        self.__label.pack()
        self.__label2.pack()
        self.__button1.pack(side="left")
        self.__button2.pack(side="right")


        #packing automatically stacks based on order
        # self.top_frame.pack() #frames have to be packed first
        # self.bottom_frame.pack()
        # # self.__label.pack()
        # self.__label2.pack()
        # self.__button1.pack(side="left")
        # self.__button2.pack(side="right")

        # tk = tkinter.Tk()

        tkinter.mainloop()

    def ratingcalc(self):
        self.index +=  1
        self.index = self.index % 4
        self.buttonpressed = True
        self.__label.config(text=self.questionList[self.index])
        self.__label2.config(text=self.choiceList[self.index])
        print(self.index)
        print(self.buttonpressed)

        # return self.index

def main():
    c = Controller()
    print(c.ratingcalc())
main()
