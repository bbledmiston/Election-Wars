import tkinter

class twoelectionwars:
    def __init__(self, qNumber, question, answer1, answer2, rating1, rating2):
        self.qNumber = qNumber
        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.rating1 = rating1
        self.rating2 = rating2

    def returnRating(self):
        if button == self.answer1:
            adjust = rating1
        elif button == self.answer2:
            adjust = rating2
        return adjust

    # def __str__(self):
    #     return str(self.qNumber) + str(self.question) + str(self.answer1) + str(self.answer2) + str(self.rating1) + str(self.rating2)

    def questions(self):
        return self.question

# def main():
#
# # questions =  {0: ['assuage the fears of minority voters?','\na. Nah\nb. I don\'t think so \n', -1,-1],
# #     1: ['test question', '\na. Yes\nb. No\n', 1,-1]
# #     }
#
#     # q0 = Events(0,"assuage the fears of minority voters?","a. Nah","b. I don't think so",1,-1)
#     # print(q0)
#
#     # for i in range(39):
#         # Player.rating += questions[i].present()
# main()
