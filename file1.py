#Assignment1.py/File1.py
#Version 1.5
#Author Charles Doolittle
#Last revision Charles Doolittle at 9:00 may 23, 2013
#Purpose a spooky text adventure game


def displayIntro():
    print ('You awake in a dark forest with no memory of how you got there nor where you are going.')
    
def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print ('Do you start traveling North or south? (1 or 2)')
        cave = raw_input()
    return cave
#initial choice
def checkCave(chosenCave):
    print ('You begin walking')
#1st decision tree   
    if chosenCave == "1":
        print ('You come to some thick Brush do you walk through (1) it or around(2) ')
        chosenCave = raw_input()
        if chosenCave == "1":
            print ('You see a rabbit do you follow(2) it or catch it for food(1)')
            chosenCave = raw_input()
            if chosenCave == "1":
                print ('The rabbit king jumps out of nowhere and crushes you')
            elif chosenCave == "2":
                print ('You follow the rabbit into a trap!')
        elif chosenCave == "2":
            print ('you can continue walking(2) or sit for a rest(1)')
            chosenCave = raw_input()
            if chosenCave == "1":
                print ('You hear your mothers voice, she calls you back into the house for dinner, all this adventuring for nothing!')
            elif chosenCave == "2":
                print ('You fall into a pit, trapped there forever')
 #2nd division tree               
    elif chosenCave == "2":
        print('You come to a fallen tree do you use it for shelter(1) or continue')
        chosenCave = raw_input()
        if chosenCave == "1":
            print ('Dou you light a fire(1) or sleep through the cold(2)?')
            chosenCave = raw_input()
            if chosenCave == "1":
                print ('A bear uses the fire to find you and east you!')
            elif chosenCave == "2":
                print ('You freeze to death oovernight.')
        elif chosenCave == "2":
            print ('You continue on and hear voices in the distance, do you go talk to them(1) or run away.')
            chosenCave = raw_input()
            if chosenCave == "1":
                print ('They are wandering cannibals and eat you alive.')
            elif chosenCave == "2":
                print ('You run into slender man and he steals your soul.')

def main():
    
#Option to restart    
    playAgain = 'yes'
    while playAgain == 'yes' or playAgain == 'y':
        displayIntro()
        caveNumber = chooseCave()
        checkCave(caveNumber)
    
        print ('Do you want to play again? (yes or no)')
        playAgain = raw_input()


if __name__ == "__main__": main()