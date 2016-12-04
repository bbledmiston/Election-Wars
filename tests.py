import marleahwork
import brittneywork

def main():
    candidate= marleahwork.Opponent()
    candidate.name= 'Donald Trump'
    candidate.party= 'Repbulican'
    candidate.pollingData= 55
    candidate.increasePolls(15)
    print(candidate.name, 'Popularity:', candidate.pollingData, candidate.party)
    #debate= marleahwork.PressConference()
    print('The first big debate of the year!')
    #candidate.Publicity= "big"
    candidate.addressDrama('bad')
    print(candidate.name, 'New Popularity:', candidate.pollingData)
    

main()
