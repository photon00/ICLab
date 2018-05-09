import time, copy, sys

def output(wire):
    """
        wire[0]  = start:        0 -> initial, 1 -> play
        wire[1]  = switch:       0 -> module1, 1 -> module2
        wire[2]  = play_now:     1 -> player right, 2 -> player left
        wire[3]  = wind_now:     3~-3 ex. +3 -> left 3, -2 right 2
        wire[4]  = atkmode:      0 -> normal, 1 -> double, 2 -> big, 3 -> heal
        wire[5]  = power:        1~4
        wire[6]  = bullet_pos:   shape = (7,2) 7 pos, (x,y)
        wire[7]  = HP1:          shape = (2,) 0~12
        wire[8]  = HP2:          shape = (2,) 0~12
        wire[9]  = skills1:      shape = (3,) 1 or 0
        wire[10] = skills2:      shape = (3,) 1 or 0
    """
    start, switch, play_now, wind_now, atkmode, power, bullet_pos, HP1, HP2, skills1, skills2 = wire
    bullet_pos1 = bullet_pos
    bullet_pos2 = [(31-p[0], p[1]) for p in bullet_pos]
    array = [['.' for i in range(32)] for j in range(16)]
    
    if start == 0:
        initial_output(array)
        print_array(array)
        return

    update_state(array, HP1[0], HP2[0], wind_now, skills1, skills2)
    if switch == 0:
        module1_update(array, play_now, atkmode, power)
        print_array(array)

    else:
        module2_display(array, atkmode, eval('bullet_pos{}'.format(play_now)), HP1[1], HP2[1])


def initial_output(array):
    # write 'F'
    for y in range(4,13):
        array[y][3] = '#'
    for x in range(4,7):
        array[4][x] = '#'
        array[8][x] = '#'

    # write 'U'
    for y in range(4,12):
        array[y][9] = '#'
        array[y][13] = '#'
    for x in range(10,13):
        array[12][x] = '#'

    # write 'C'
    for y in range(5,12):
        array[y][16] = '#'
    for x in range(17,21):
        array[4][x] = '#'
        array[12][x] = '#'

    # write 'K'
    for y in range(4,13):
        array[y][23] = '#'
    for i in range(4):
        array[i+4][27-i] = '#'
        array[i+8][24+i] = '#'
    array[12][28] = '#'


def update_state(array, hp1, hp2, wind_now, skills1, skills2):
    # write HP
    for x in range(2, hp2+2):
        array[0][x] = '#'
    for x in range(30-hp1, 30):
        array[0][x] = '#'

    # write wind
    for i in range(abs(wind_now)):
        if wind_now > 0: array[2][15-i] = '#'
        else: array[2][16+i] = '#'

    # write skill
    for i, x in enumerate([2,4,6]):
        if skills2[i] == 1: array[2][x] = '#' 
    for i, x in enumerate([29,27,25]):
        if skills1[i] == 1: array[2][x] = '#'

    # write people
    for x,y in [(3,12), (2,13), (3,13), (4,13), (3,14), (2,15), (4,15)]:
        array[y][x] = '#'
    for x,y in [(28,12), (27,13), (28,13), (29,13), (28,14), (27,15), (29,15)]:
        array[y][x] = '#'

    # write wall
    for y in range(9,16):
        array[y][15] = '#'
        array[y][16] = '#'


def module1_update(array, play_now, atkmode, power):
    # write atkmode
    if atkmode != 0:
        if play_now == 1:
            array[2][31-2*atkmode] = '@'
        else:
            array[2][0+2*atkmode] = '@'

    # write power
    if play_now == 1:
        for i in range(power):
            array[9][31-i] = '#'
    else:
        for i in range(power):
            array[9][i] = '#'


def module2_display(array, atkmode, bullet_pos, hp1, hp2):
    if atkmode == 0:
        for i in range(7):
            tmp_array = copy.deepcopy(array)
            tmp_array[bullet_pos[i][1]][bullet_pos[i][0]] = '%'
            print_array(tmp_array)
            time.sleep(0.5)
    elif atkmode == 1:
        for _ in range(2):
            for i in range(7):
                tmp_array = copy.deepcopy(array)
                tmp_array[bullet_pos[i][1]][bullet_pos[i][0]] = '%'
                print_array(tmp_array)
                time.sleep(0.5)
    elif atkmode == 2:
        for i in range(7):
            tmp_array = copy.deepcopy(array)
            x, y = bullet_pos[i][0], bullet_pos[i][1]
            tmp_array[y][x] = '%'
            if bullet_pos[0][0] > 16:
               tmp_array[y-1][x] = '%'
               tmp_array[y][max(x-1,0)] = '%'
               tmp_array[y-1][max(x-1,0)] = '%'
            else:
               tmp_array[y-1][x] = '%'
               tmp_array[y][min(x+1,31)] = '%'
               tmp_array[y-1][min(x+1,31)] = '%'

            print_array(tmp_array)
            time.sleep(0.5)
    update_HP(array, hp1, hp2)
    
        
def update_HP(array, hp1, hp2):
    for i, _ in enumerate(array[0]):
        array[0][i] = '.'
    for x in range(2, hp2+2):
        array[0][x] = '#'
    for x in range(30-hp1, 30):
        array[0][x] = '#'
    print_array(array)


def print_array(array):
    print("\033[H")
    for line in array:
        for char in line:
            print(' {}'.format(char), end='')
        print()

if __name__ == '__main__':
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()
    bul_pos = [(27,11),(21,7),(16,4),(11,5),(8,7),(6,9),(4,11)]
    skills1 = [1,1,1]
    skills2 = [0,1,1]
    wire = [1, 1, 2, 3, 1, 2, bul_pos, [6,6], [11,2], skills1, skills2]
    output(wire)
    












