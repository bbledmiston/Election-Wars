import json
def save():
    data= input('Please enter your name:')
    with open('save.json', 'w') as x:
        json.dump(data, x)
        x.close()
def load():
    with open('save.json', 'r') as y:
        data= json.load(y)
        y.close

#import savedata from the main and call savedata.save or savedata.load to save and load
