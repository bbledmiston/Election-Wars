import tkinter
import twoelectionwars


class Controller:

    def __init__(self):
        self.__mainWindow = tkinter.Tk()
        self.__mainWindow.title ('Kakistrocracy')
        self.__mainWindow.geometry('700x300')
        self.__mainWindow.configure(bg='gray')
        self.top_frame = tkinter.Frame(self.__mainWindow)
        self.mid_frame = tkinter.Frame(self.__mainWindow)
        self.bottom_frame = tkinter.Frame(self.__mainWindow)
        #List of questions that cycles through with each button press
        self.questionList = ["You are the nominee of your party! What is the first thing you do?",
                            "The parents of a fallen soldier express concern about your proposed policies. Do you: ",
                            "You are asked about your stance regarding alleged authoritarian leaders. You: ",
                            "You are asked to release your tax returns. Do you: ",
                            "You have been emphatically endorsed by white supremacist \ngroups such as the KKK. How do you respond?",
                            "You accuse your opponent of wanting to abolish the second amendment. Do you: ",
                            "You are being sued for fraudulent business practices. It's not going your way. Do you: ",
                            "A video was leaked in which you appear \nto be bragging about sexual assault. You: ",
                            "You are asked during a debate if you will \naccept the election results if they do not go in your favor. You: ",
                            "Women voters are concerned about their rights to an abortion. Your position is: ",
                            "You are concerned about 'voter rigging', your response is to: ",
                            "Many Americans fear that their jobs are being taken away. What is your response?",
                            "You are being criticized by your opponent during a debate. How do you respond?",
                            "You are asked about your stance on immigration. Your response is:",
                            "In regards to undocumented immigrants from Mexico, you declare:",
                            "In response to concerns about climate change, your position is:",
                            "You have never held a public office. \nDo you feel you are completely qualified to be the president of the United States?",
                            "Would you vote for yourself?",
                            "Congratulations! You are the President of the United States! Good Luck."




                            ]
        #List of possible choices that cycles along with the questions through each button press
        self.choiceList = ["A. Give a heartfelt, thankful speech \nB. Go on a Twitter rant",
                        "A. Relieve the concerns or offer explanations\nB. Make assumptions that the mother was not allowed to speak because they are muslim",
                        "A. Denounce their actions and their crimes against their people\nB. Praise Putin",
                        "A. Go the traditional route and release them\nB. Refuse to release them",
                        "A. Immediately disavow the KKK\nB. Dawdle and THEN disavow the KKK",
                        "A. 'Jokingly' incite violence against your opponent\nB. Just trash your opponent",
                        "A. Vehemently deny the allegations\nB. Vaguely threaten to deport the judge presiding over the case",
                        "A. Apologize for your comments\nB. Dismiss it as locker room talk",
                        "A. Say you will graciously accept the election results\nB. Say that you'll only accept them in the event that you win",
                        "A. Propogate falsehoods about late term abortions\nB. Address those concerns and explain your beliefs",
                        "A. Tell your supporters to engage in voter intimidation\nB. Express your concerns to the media",
                        "A. Tell your supporters that you will create new jobs\nB. Fearmonger and tell your supporters you will create new jobs",
                        "A. Appropriately respond to the criticism\nB. Call your opponent a 'nasty woman'",
                        "A. Claim you will build a wall around the border to keep Mexicans from crossing it\nB. Have a sane, rational response",
                        "A. That they are 'bad hombres' you will be banning from the country\nB. That you will create a better immigration policy",
                        "A. You are also concerned about the environment and climate change\nB. That global warming is a hoax because we still have cold weather",
                        "A. Yes\nB. No",
                        "A. Yes\nB. No",
                        "Thanks for playing!"
                        ]
        #List of response values that will affect polling rating based on which button is pressed
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
                                [-1,1],
                                [1,-1],
                                [1,-1],
                                [-1,1],
                                [-1,1],
                                [0,0],
                                [0,0],
                                [0,0]
                                    ]

        self.buttonpressed = False
        self.rating = 50
        self.a_value = 0
        self.b_value = 0
        self.index = 0
        #indexes through each item of the question and choice lists, allows text to switch while remaining in same window
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
                                                )


        self.top_frame.pack(padx=60, pady=40)
        self.mid_frame.pack()
        self.bottom_frame.pack(padx=60, pady=40)


        self.__label.pack()
        self.__label2.pack()
        self.__button1.pack(side="left")
        self.__button2.pack(side="right")


        tkinter.mainloop()

    #returns calculated value whenever button is pressed
    def ratingcalc(self):
        self.index += 1
        self.index = self.index
        self.buttonpressed = True
        if self.index < len(self.questionList):
            self.__label.config(text=self.questionList[self.index])
            self.__label2.config(text=self.choiceList[self.index])
            self.a_value = self.response_values[self.index][0]
            self.b_value = self.response_values[self.index][1]

    #increase or decrease rating based on respone value when buttonA is pressed
    def buttonA(self):
        self.rating += self.a_value
        self.ratingcalc()

    #increase or decrease rating based on respone value when buttonB is pressed
    def buttonB(self):
        self.rating += self.b_value
        self.ratingcalc()


    def response(self):
        self.buttonB()

    #Would have shown a new window based on election results, unable to be completed
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

    #Play again function - Marleah
    # playagain = 'yes'
    # c = Controller()
    # while playagain == 'yes':
    #     Controller()
    #     print('Do you want to play again? (yes or no)')
    #     playagain = input()

main()
