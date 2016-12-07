import tkinter
# import "tkinter" messagebox
# import twoelectionwars
import twoelectionwars

class Controller:

    def __init__(self):
        self.__mainWindow = tkinter.Tk()
        self.__mainWindow.title ('Controller')
        # self.top_frame = tkinter.Frame(self.__mainWindow)
        # self.bottom_frame = tkinter.Frame(self.__mainWindow)
        self.top_frame = tkinter.Frame(self.__mainWindow)
        self.bottom_frame = tkinter.Frame(self.__mainWindow)
        # self.question = tkinter.StringVar()
        self.questionList = ["a","b","c","d"]
        self.question = self.questionList[0]
        self.q1 = self.questionList[0]
        # self.question.set(self.q1)
        self.buttonpressed = False
        self.index = 0
        for i in range(len(self.questionList)):
        # for i in range(len(self.questionList)):


            # i = 0
            # self.index += 1
            # if self.index < len(self.questionList):
            #     print(self.question)
            self.question = self.questionList[self.index]

            # self.question.set(questionList[i])
            self.__test = twoelectionwars.twoelectionwars(0,self.question,"a. Nah","b. I don't think so",1,-1)
            # print(self.__test.rating1)
            self.__label = tkinter.Label(self.top_frame, text=self.question)
            self.__label2 = tkinter.Label(self.bottom_frame, text="I am also a label")

            self.__button1 = tkinter.Button(self.__mainWindow, \
                                                text="A", \
                                                command=self.ratingcalc
                                                )
            self.__button2 = tkinter.Button(self.__mainWindow, \
                                                text="B", \
                                                command=self.ratingcalc
                                                )
            # print(i)
            # if self.ratingcalc() == True:
            #     i += 1


        self.top_frame.pack() #frames have to be packed first
        self.bottom_frame.pack()
        self.__label.pack()
        self.__label2.pack()
        self.__button1.pack(side="left")
        self.__button2.pack(side="right")
            # if self.index == len(self.questionList)-1:
            #     self.buttonpressed = True
            # i += 1
            # self.buttonpressed = True
        print(self.index)
        print(self.buttonpressed)
        # self.__label = tkinter.Label(self.top_frame, text=twoelectionwars.questions())
            #self.index += 1



        #packing automatically stacks based on order
        self.top_frame.pack() #frames have to be packed first
        self.bottom_frame.pack()
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
        print(self.index)
        print(self.buttonpressed)

        # return self.index

#string vars - tkinter
def main():
    c = Controller()
    print(c.ratingcalc())
main()
