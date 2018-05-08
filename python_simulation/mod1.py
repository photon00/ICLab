import random
#from mod2 import module2
from screen_output import *

def module1(wire,data1,data2):
    wire[1] = 0 #reset switch
    wire[2] = 3 - wire[2] #switch player
    wire[3] = random.choice([-3,-2,-1,0,1,2,3]) #wind
    wire[4] = 0 #reset atkmode
    wire[5] = 1 #reset power
    wire[7] = [data1[0],data1[0]] #update hp1
    wire[8] = [data2[0],data2[0]] #update hp2
    output(wire)
    
    if (wire[2] == 1):#player1
        key_input(wire)
        if (wire[4] != 0):#check if skill remain
            if (data1[1][wire[4]-1] == 1): #remain
                data1[1][wire[4]-1] = 0
                wire[9] = data1[1] #update skill remain
            else:
                wire[4] = 0
        output(wire)
        module2(wire,data1,data2)
        
    else:
        key_input(wire)
        if (wire[4] != 0):#check if skill remain
            if (data2[1][wire[4]-1] == 1): #remain
                data2[1][wire[4]-1] = 0
                wire[10] = data2[1] #update skill remain
            else:
                wire[4] = 0
        module2(wire,data2,data1)      

    
def key_input(wire):
    key = int(input("1:atkmode 2:power 3:attack : "))
    if (key == 1):
        if (wire[4] == 3):
            wire[4] = 0
        else:
            wire[4] += 1
        output(wire)
        key_input(wire)

    elif (key == 2):
        if (wire[5] == 4):
            wire[5] = 1;
        else:
            wire[5] += 1;
        output(wire)
        key_input(wire)

    elif (key == 3):
        return
    else:
        key_input(wire)
        

def module2(wire,data1,data2):#data1:attacker  data2:attacked   
    wire[1] = 1 #set switch 1
    wind = wire[3]
    atk_mode = wire[4]
    power = wire[5]
    wire[6] = []#reset bullet_pos
    win = 0 # 1:player1 win
    
    if (wire[2] == 1):#player1 attack
        wire[7][0] = data1[0] #updata health before attack
        wire[8][0] = data2[0]
        atk_var = power + wind
        #print (atk_var)
        if (atk_var == -2):
            wire[6] = [(26,11),(25,10),(24,10),(23,11),(22,12),(21,14),(21,15)]
            
        elif (atk_var == -1):
            wire[6] = [(26,11),(24,9),(22,9),(20,11),(19,13),(18,15),(17,14)]
            
        elif (atk_var == 0):
            wire[6] = [(25,10),(23,9),(21,9),(18,10),(17,11),(18,13),(19,15)]
            
        elif (atk_var == 1):
            wire[6] = [(25,9),(23,7),(20,6),(16,7),(14,9),(13,11),(12,15)]
            
        elif (atk_var == 2):
            wire[6] = [(25,10),(23,8),(20,6),(16,6),(12,8),(10,11),(8,15)]
            
        elif (atk_var == 3):
            wire[6] = [(24,9),(20,6),(15,6),(11,8),(8,11),(6,15),(5,13)]
            if (atk_mode == 0):
                data2[0] -= 2
            elif (atk_mode == 1):
                data2[0] -= 4
            elif (atk_mode == 2):
                data2[0] -= 5
            
        elif (atk_var == 4):
            wire[6] = [(25,9),(22,6),(18,5),(13,5),(9,6),(6,8),(3,11)]
            if (atk_mode == 0):
                data2[0] -= 3
            elif (atk_mode == 1):
                data2[0] -= 6
            elif (atk_mode == 2):
                data2[0] -= 6
                
        elif (atk_var == 5):
            wire[6] = [(25,8),(22,5),(17,4),(11,4),(7,5),(3,8),(0,12)]
            
        elif (atk_var == 6):
            wire[6] = [(26,9),(23,5),(18,3),(13,3),(8,4),(4,6),(0,9)]
            
        else:
            wire[6] = [(26,9),(24,6),(21,4),(17,2),(11,1),(5,2),(0,4)]

        if (atk_mode == 3):
            data1[0] += 6
            if (data1[0] > 12):
                data1[0] = 12
                
        wire[7][1] = data1[0]
        if (data2[0] <= 0):
            data2[0] = 0
            win = 1
        wire[8][1] = data2[0]
        
    else:#player2
        wire[7][0] = data2[0]
        wire[8][0] = data1[0]
        atk_var = power - wind
        if (atk_var == -2):
            wire[6] = [(26,11),(25,10),(24,10),(23,11),(22,12),(21,14),(21,15)]
            
        elif (atk_var == -1):
            wire[6] = [(26,11),(24,9),(22,9),(20,11),(19,13),(18,15),(17,14)]
            
        elif (atk_var == 0):
            wire[6] = [(25,10),(23,9),(21,9),(18,10),(17,11),(18,13),(19,15)]
            
        elif (atk_var == 1):
            wire[6] = [(25,9),(23,7),(20,6),(16,7),(14,9),(13,11),(12,15)]
            
        elif (atk_var == 2):
            wire[6] = [(25,10),(23,8),(20,6),(16,6),(12,8),(10,11),(8,15)]
            
        elif (atk_var == 3):
            wire[6] = [(24,9),(20,6),(15,6),(11,8),(8,11),(6,15),(5,13)]
            if (atk_mode == 0):
                data2[0] -= 2
            elif (atk_mode == 1):
                data2[0] -= 4
            elif (atk_mode == 2):
                data2[0] -= 5
            
        elif (atk_var == 4):
            wire[6] = [(25,9),(22,6),(18,5),(13,5),(9,6),(6,8),(3,11)]
            if (atk_mode == 0):
                data2[0] -= 3
            elif (atk_mode == 1):
                data2[0] -= 6
            elif (atk_mode == 2):
                data2[0] -= 6
                
        elif (atk_var == 5):
            wire[6] = [(25,8),(22,5),(17,4),(11,4),(7,5),(3,8),(0,12)]
            
        elif (atk_var == 6):
            wire[6] = [(26,9),(23,5),(18,3),(13,3),(8,4),(4,6),(0,9)]
            
        else:
            wire[6] = [(26,9),(24,6),(21,4),(17,2),(11,1),(5,2),(0,4)]

        if (atk_mode == 3):
            data1[0] += 6
            if (data1[0] > 12):
                data1[0] = 12
            
        wire[8][1] = data1[0]
        if (data2[0] <= 0):
            data2[0] = 0
            win = 2
        wire[7][1] = data2[0]
        
    #print(wire)
    output(wire)
    
    if (win == 1):#check if someone lose
        print ("Player1 win !!!")
        return
    if (win == 2):
        print ("Player2 win !!!")
        return

    if (wire[2] == 1):
        module1(wire,data1,data2)
    else:
        module1(wire,data2,data1)
