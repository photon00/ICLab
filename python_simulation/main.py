from init import *
from mod1 import *
import sys



def main():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()
    #array = [[O for i in range(32)] for j in range(16)] #32*16 array
    wire = [0,0,2,0,0,1,[],[12,12],[12,12],[1,1,1],[1,1,1]]
    #start/switch/player_now/wind_now/atkmode/pow/bullet_pos/HP1/HP2/skill_remain1/skill_remain2
    data1 = [12,[1,1,1]] #HP/skill_remain
    data2 = [12,[1,1,1]]

    init(wire)
    module1(wire,data1,data2)

main()
