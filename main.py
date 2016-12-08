import tkinter
import twoelectionwars

class Controller:

    def __init__(self):
        self.__mainWindow = tkinter.Tk()
        self.__mainWindow.title ('Controller')
        self.__mainWindow.configure(bg='gray')
        self.top_frame = tkinter.Frame(self.__mainWindow)
        self.bottom_frame = tkinter.Frame(self.__mainWindow)
        self.questionList = ["You are the nominee of your party! What is the first thing you do?",
                            "The parents of a fallen soldier express concern about your proposed policies. Do you: ",
                            "You are asked about your stance regarding alleged authoritarian leaders. You: ",
                            "You are asked to release your tax returns. Do you: ",
                            "You have been emphatically endorsed by white supremacist groups such as the KKK. How do you respond?",
                            "You accuse your opponent of wanting to abolish the second amendment. Do you: ",
                            "You are being sued for fraudulent business practices. It's not going your way. Do you: ",
                            "A video was leaked in which you appear to be bragging about sexual assault. You: "
                            ]
        self.choiceList = ["A. Give a heartfelt, thankful speech \nB. Go on a Twitter rant",
                        "A. Relieve the concerns or offer explanations\nB. Make assumptions that the mother was not allowed to speak because they are muslim",
                        "A. Denounce their actions and their crimes against their people\nB. Praise Putin",
                        "A. Go the traditional route and release them\nB. Refuse to release them",
                        "A. Immediately disavow the KKK\nB. Dawdle and THEN disavow the KKK",
                        "A. 'Jokingly' incite violence against your opponent\nB. Just trash your opponent",
                        "A. Vehemently deny the allegations\nB. Vaguely threaten to deport the judge presiding over the case",
                        "A. Apologize for your comments\nB. Dismiss it as locker room talk"
                        ]
        self.response_values = [[1, -1], [-1, 2], [3, 5], [4, -9], [1, 6], [-5, 2], [4,-5], [-3, 2]]
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
        self.bottom_frame.pack(padx=60, pady=40)
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
        self.index += 1
        self.index = self.index % 8
        self.buttonpressed = True
        self.__label.config(text=self.questionList[self.index])
        self.__label2.config(text=self.choiceList[self.index])
        self.a_value = self.response_values[self.index][0]
        self.b_value = self.response_values[self.index][1]
        print(self.index)
        print(self.buttonpressed)
        print(self.a_value)
        print(self.b_value)
        # if self.__button1 == buttonpressed:
        #     print("1")
        # elif buttonpressed == self.__button2:
        #     print("-1")
        # self.returnRating()
        # print(returnRating)

        # return self.index
    def buttonB(self):
        self.rating += self.b_value
        self.ratingcalc()
        print(self.rating)

    def buttonA(self):
        self.rating += self.a_value
        self.ratingcalc()
        print(self.rating)


    # def callboth(self):
    #     self.ratingcalc()
    #     self.buttonB()


    # def returnRatingA(self):
    #     self.
    #         self.__q1 = twoelectionwars.twoelectionwars(0,self.question,"a. Nah","b. I don't think so",1,-1)
    #         self.__q2 = twoelectionwars.twoelectionwars(1,self.question,"a. Yes","b. No",2,-2)




def main():
    c = Controller()
    # print(c.ratingcalc())
main()
