import time

def displayIntro():
    print ('You awake in a dark forest with no memory of how you got there nor where you are going.')
    
def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print ('Do you start traveling North or south? (1 or 2)')
        cave = raw_input()
    return cave

def checkCave(chosenCave):
    print ('You begin walking')
   
    if chosenCave == "1":
        print ('You come to some thick Brush do you walk through it or around')
        chosenCave = raw_input()
        if chosenCave == "through":
            print ('You see a rabbit do you follow it or catch it for food')
            chosenCave = raw_input()
            if chosenCave == "catch":
                print ('The rabbit king jumps out of nowhere and crushes you')
            elif chosenCave == "around":
                print ('gvkj')
        elif chosenCave == "around":
            print ('you can continue walking or sit for a rest')
            chosenCave = raw_input()
            if chosenCave == "sit":
                print ('You hear your mothers voice, she calls you back into the house for dinner, all this adventuring for nothing!')
            elif chosenCave == "2":
                print ('you choose 3.4')
                
    elif chosenCave == "2":
        print('You come to a fallen tree do you use it for shelter or continue')
        chosenCave = raw_input()
        if chosenCave == "shelter":
            print ('you choose 2.3')
            chosenCave = raw_input()
            if chosenCave == "jump":
                print ('you choose 3.5')
            elif chosenCave == "bridge":
                print ('you choose 3.6')
        elif chosenCave == "continue":
            print ('you choose 2.4')
            chosenCave = raw_input()
            if chosenCave == "run":
                print ('you choose 3.7')
            elif chosenCave == "talk":
                print ('you choose 3.8')

def main():
    
    
    playAgain = 'yes'
    while playAgain == 'yes' or playAgain == 'y':
        displayIntro()
        caveNumber = chooseCave()
        checkCave(caveNumber)
    
        print ('Do you want to play again? (yes or no)')
        playAgain = raw_input()


if __name__ == "__main__": main()