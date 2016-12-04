class Opponent:
	def __init__(self):
		name = ""
		party = "" #any party that the candidate is not
		pollingData = "" # any number between 0 and 100

	def increasePolls(candidate, number): # any number between 0 and 100
		candidate.pollingData = candidate.pollingData + number
	def decreasePolls(candidate, number): # any number between 0 and 100
		candidate.pollingData = candidate.pollingData - number

#class PressConference:

	def addressDrama(candidate, effect): # good, bad, none
		Publicity = "big" #big, small
		if Publicity == 'small':
			someNumber = 5
		elif Publicity == 'big':
			someNumber = 15
		if effect == 'good':
			candidate.increasePolls(someNumber)
		elif effect == 'bad':
			candidate.decreasePolls(someNumber)



'''
Possible events
random Opponentis involved in a cheating scandal
- release the information to the Public
- keep the information to yourself

candidates daughter gets sick
- keep campaigning
- take some time off campaigning
- use her sickness to help your campaign

debate question- how do you feel about free college
I love free college
College cannot be free
I will try to help those who cant afford college

debate question- What is your main goal this term?
Make america great again
womans rights
guns guns guns
'''
