import random
"""
class events:
    def init self
        def list of questions

    def ask questions

class player
    name
    rating/favorability

    cpu =  true/false

controller - campaign
    keeps track of politicians
    ratings

main
- call campaign
c.run campaign - loops throughg

json file to create login data
active plot graph to update polling data


"""


class Player: #create player object and keep track of rating data
    def __init__(self,name):
        self.name = name
        self.rating = None

    #def create user data?

    def rating(self):
        polling = 0
        attempt, outcomeA, outcomeB = ask_question(questions)
        if attempt == outcomeA:
            polling+=outcomeA
        elif attempt == outcomeB:
            polling+=outcomeB
        else:
            print("Error")
        self.rating = polling
        return self.rating

    def __str__(self):
        return self.name + ", Your rating is: " + str(self.rating)


class Events:
    def __init__(self):
        self.months = {}
        self.months['july'] = {
                'You have emerged the champion of your party!':
                ('\na. Yes\nb. No\n', 1,-1),
                'Test question':
                ('\na. +1\nb. -1\n', 1,-1)
                }
        self.months['august'] = {
                'You accuse your opponent of wanting to abolish guns. Do you make a bad joke that can be interpreted as a call to violence?':
                ('\na. Yes \nb. No\n', -1,1)

        }

        self.months['september'] = {
                'assuage the fears of minority voters?':
                ('\na. Nah\nb. I don\'t think so \n', -1,-1),
                'you\'re attending a congregation at a black church. you are asked to not give a political speech. do you...':
                ('\n a. comply\nb. give the speech anyway',1,-1)
                'You again accuse your opponent of wanting to abolish the second amendment. Do you make another incendiary joke?':
                ('\na. No \nb. Hell yeah\n', 1,-1)

        }

        self.months['october'] = {
                'test question':
                ('\na. Yes\nb. No\n', 1,-1)
        }

        self.months['november'] = {
                'Do you feel you are completely qualified to be the president of the United States of America?':
                ('\na. Yes\nb. No\n',0,0),
                'would you vote for you?':
                ('\na. Yes\nb. No\n',0,0)
        }

    def ask_question(self,questions):
        item = random.choice(list(questions.items()))
        question = item[0]
        print(question)
        (possibilities, positive, negative) = item[1]
        print(possibilities)
        attempt = input('\nEnter \'a\' or \'b\' for your answer\n')
        return (attempt, outcomeA, outcomeB)



def main():
    p = Player("bob")
    print(p)
    # numQuestions = len(list(questions.keys()))
    # for i in range(numQuestions):
    #     attempt, outcomeA, outcomeB = ask_question()
    #     if attempt not in {'a', 'b'}:
    #         print('invalid input')
    #     elif attempt == 'a':
    #         print(outcomeA)
    #     elif attempt == 'b':
    #         print(outcomeB)

main()
