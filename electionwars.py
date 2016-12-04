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
"""

class Controller:
    def __init__(self):
        self.player = Player()



class Player:
    def __init__(self,name,rating):
        self.name = name
        self.rating = rating



class Events:
    def __init__(self):
        self.july = {
                'You have emerged the champion of your party! Are you respectful in your acceptance of the nomination?':
                ('\na. Yes\nb. No\n', 1,-1),
                'Test question':
                ('\na. +1\nb. -1\n', 1,-1)
                }
        self.august = {

        }

        self.september = {
        'appeal to minority voters?':('\na. Yes\nb. No\n', 1,-1)

        }

        self.october = {

        }

        self.november = {
        'would you vote for you?':('\na. Yes\nb. No\n',0,0)
        }
    def ask_question(questions):
        item = random.choice(list(questions.items()))
        question = item[0]
        print(question)
        (possibilities, positive, negative) = item[1]
        print(possibilities)
        attempt = input('\nEnter \'a\' or \'b\' for your answer\n')
        return (attempt, outcomeA, outcomeB)

    def rating():
        polling = 0
        attempt, outcomeA, outcomeB = ask_question(questions)
        if attempt == outcomeA:
            polling+=outcomeA
        elif attempt == outcomeB:
            polling+=outcomeB
        else:
            print("invalid")

def main():
    numQuestions = len(list(questions.keys()))
    for i in range(numQuestions):
        attempt, outcomeA, outcomeB = ask_question(questions)
        if attempt not in {'a', 'b'}:
            print('invalid input')
        elif attempt == 'a':
            print(outcomeA)
        elif attempt == 'b':
            print(outcomeB)

main()
