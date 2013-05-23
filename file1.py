import time

def displayIntro():
    print ('choose')
    
def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print ('choose? (1 or 2)')
        cave = raw_input()
    return cave

def checkCave(chosenCave):
    print ('You Choose')
   
    if chosenCave == "1":
        print ('You choose 1.1')
        chosenCave = raw_input()
        if chosenCave == "1":
            print ('you choose 2.1')
            chosenCave = raw_input()
            if chosenCave == "1":
                print ('you choose 3.1')
            elif chosenCave == "2":
                print ('you choose3.2')
        elif chosenCave == "2":
            print ('you choose2.2')
            chosenCave = raw_input()
            if chosenCave == "1":
                print ('you choose 3.3')
            elif chosenCave == "2":
                print ('you choose 3.4')
                
    elif chosenCave == "2":
        print('you choose 1.2')
        chosenCave = raw_input()
        if chosenCave == "1":
            print ('you choose 2.3')
            chosenCave = raw_input()
            if chosenCave == "1":
                print ('you choose 3.5')
            elif chosenCave == "2":
                print ('you choose 3.6')
        elif chosenCave == "2":
            print ('you choose 2.4')
            chosenCave = raw_input()
            if chosenCave == "1":
                print ('you choose 3.7')
            elif chosenCave == "2":
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