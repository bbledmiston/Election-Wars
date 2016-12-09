import tkinter
import twoelectionwars


class Controller:

    def __init__(self):
        self.__mainWindow = tkinter.Tk()
        self.__mainWindow.title ('Kakistrocracy')
        self.__mainWindow.geometry('700x300')
        self.__mainWindow.configure(bg='gray')
        # self.__mainWindow.resizable(width=False, height=False)
        self.top_frame = tkinter.Frame(self.__mainWindow)
        self.mid_frame = tkinter.Frame(self.__mainWindow)
        self.bottom_frame = tkinter.Frame(self.__mainWindow)

        self.questionList = ["You are the nominee of your party! What is the first thing you do?",
                            "The parents of a fallen soldier express concern about your proposed policies. Do you: ",
                            "You are asked about your stance regarding alleged authoritarian leaders. You: ",
                            "You are asked to release your tax returns. Do you: ",
                            "You have been emphatically endorsed by white supremacist groups such as the KKK. How do you respond?",
                            "You accuse your opponent of wanting to abolish the second amendment. Do you: ",
                            "You are being sued for fraudulent business practices. It's not going your way. Do you: ",
                            "A video was leaked in which you appear to be bragging about sexual assault. You: "
                            "You are asked during a debate if you will accept the election results if they do not go in your favor. You: ",
                            "Women voters are concerned about their rights to an abortion. Your position is: ",
                            "You are concerned about 'voter rigging', your response is to: ",
                            ]
        self.choiceList = ["A. Give a heartfelt, thankful speech \nB. Go on a Twitter rant",
                        "A. Relieve the concerns or offer explanations\nB. Make assumptions that the mother was not allowed to speak because they are muslim",
                        "A. Denounce their actions and their crimes against their people\nB. Praise Putin",
                        "A. Go the traditional route and release them\nB. Refuse to release them",
                        "A. Immediately disavow the KKK\nB. Dawdle and THEN disavow the KKK",
                        "A. 'Jokingly' incite violence against your opponent\nB. Just trash your opponent",
                        "A. Vehemently deny the allegations\nB. Vaguely threaten to deport the judge presiding over the case",
                        "A. Apologize for your comments\nB. Dismiss it as locker room talk"
                        "A. Say you will graciously accept the election results\nB. Say that you'll only accept them in the event that you win",
                        "A. Propogate falsehoods about late term abortions\nB. Address those concerns and explain your beliefs",
                        "A."

                        ]
        self.response_values = [[1, -1],
                                [1, -1],
                                [-1, 1],
                                [1, -1],
                                [1, -1],
                                [-1, 1],
                                [1,-1],
                                [1, -1],
                                [1,-1],
                                [-1,1],
                                    ]
        # self.questions = []
        # self.questions.append(twoelectionwars.twoelectionwars(question, [responses], [ratings]))
        self.buttonpressed = False
        self.rating = 50
        self.a_value = 0
        self.b_value = 0

        self.index = 0
        for i in range(len(self.questionList)):
            self.question = self.questionList[self.index]
            self.choice = self.choiceList[self.index]
            self.__label = tkinter.Label(self.top_frame, text=self.question)
            self.__label2 = tkinter.Label(self.bottom_frame, text=self.choice)
            # self.__ratinglabel = tkinter.Label(self.top_frame, text="Your current rating is: " + str(self.rating))


            self.__button1 = tkinter.Button(self.__mainWindow, \
                                                text="A", \
                                                command=self.buttonA
                                                )
            self.__button2 = tkinter.Button(self.__mainWindow, \
                                                text="B", \
                                                command = self.buttonB
                                                # command = self.buttonB
                                                )


        self.top_frame.pack(padx=60, pady=40) #frames have to be packed first
        self.mid_frame.pack()
        self.bottom_frame.pack(padx=60, pady=40)


        self.__label.pack()
        self.__label2.pack()
        self.__button1.pack(side="left")
        self.__button2.pack(side="right")

        # self.__ratinglabel.pack()


        tkinter.mainloop()

    def ratingcalc(self):
        self.index += 1
        self.index = self.index
        self.buttonpressed = True
        if self.index < len(self.questionList):
            self.__label.config(text=self.questionList[self.index])
            self.__label2.config(text=self.choiceList[self.index])
            self.a_value = self.response_values[self.index][0]
            self.b_value = self.response_values[self.index][1]
        return self.rating
        # print(self.index)
        # print(self.buttonpressed)


    def buttonA(self):
        self.rating += self.a_value
        self.ratingcalc()


    def buttonB(self):
        self.rating += self.b_value
        self.ratingcalc()


    def response(self):
        self.buttonB()


    # def showResults(self):
    #     self.__resultwin = tkinter.Frame(self.__mainWindow)
    #     self.__winlabel = tkinter.Label(self.__resultwin, text="You are the President of the United States!")
    #     self.__resultButton = tkinter.Button(self.__resultwin,\
    #                                         text="See Results",\
    #                                         command = self.showResults)
    #     self.__resultwin.pack()
    #     self.__winlabel.pack()
    #     self.__resultButton.pack()
    #     self.resultwin.lift()


def main():
    c = Controller()
    print(response())
main()
