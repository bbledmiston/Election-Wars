class Player: #create player object and keep track of rating data
    def __init__(self,name):
        self.name = name
        self.rating = None

    def getUserData(self,lastName,firstName,userName):
        data = open("userdata.json", "w")
        lastName = 
