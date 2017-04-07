import random

def createDoors():
    to_return = [0,0,1]
    random.shuffle(to_return);
    
    return to_return;

def indexWinning(doors):
    for x in range(0,len(doors)):
        if doors[x] == 1:
            return x
    
    return

    

def runSimSwitch(num):
    """Runs the simulation num number of games, switching doors everytime"""
    
    print("SWITCH")
    win = 0
    lose = 0
    count = 0
    while count < num:
        
        game_doors = createDoors()
        #print(game_doors)
         
        choices = {0,1,2}
        choice = random.randint(0,2)
        choices.discard(choice)
         
        switch_index = 0
        
        if game_doors[choice] == 1:
            switch_index = random.sample(choices,1)[0]
        else:
            switch_index = indexWinning(game_doors)
        
        if(game_doors[switch_index] == 1):
            win += 1
        else:
            lose += 1
        
        count += 1
    
    
    print("W: {}".format(win))
    print("L: {}".format(lose))
    
    print("%: {}".format((float(win)/num) * 100))
    print("-------------------------------")
    
def runSimNoSwitch(num):
    """Runs the simulation num number of games, never switching doors"""
    
    print("NO SWITCHING")
    win = 0
    lose = 0
    count = 0
    while count < num:
        
        game_doors = createDoors()
        
        choice = random.randint(0,2)         
        
        if(game_doors[choice] == 1):
            win += 1
        else:
            lose += 1
        
        count += 1
    
    
    print("W: {}".format(win))
    print("L: {}".format(lose))
    
    print("%: {}".format((float(win)/num) * 100))
    
    print("-------------------------------")
    

if __name__ == "__main__":
    
    runSimSwitch(100000)
    runSimNoSwitch(100000)
        
            
         
        
        
            
        
        
                
        
    
    
    
    
