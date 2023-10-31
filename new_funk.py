from paint_isk_ris import *
# from input_enter import *
from paint_output import *
import math

def teleport(current_point: list,x: int,y: int,mass: list):    
    folloy_x = x
    folloy_y = y
    folloy_symbol = coord_isk([folloy_x, folloy_y], mass)
    folloy_point = [folloy_symbol, folloy_x, folloy_y]
    coord_ris([current_point[0],folloy_x,folloy_y], mass)
    coord_ris([folloy_symbol,current_point[1],current_point[2]], mass)
    current_point = folloy_point
    return current_point


def sokoban_hod(command: str,character_game: str,mass: list,px: list,bonus: str,walk: str):
    cur_point = px[0]
    x = int(px[1])
    y = int(px[2])
    xx = x
    yy = y

    command.lower()
    if command == 'l':
        x-=1
        xx-=2
    elif command == 'r':
        x+=1
        xx+=2
    elif command == 'd':
        y+=1
        yy+=2
    elif command == 'u':
        y-=1
        yy-=2
    else:
        pass

    ns = coord_isk([x, y], mass)
    

    if ns == bonus:
        nsxy = coord_isk([xx,yy], mass)
        if nsxy == walk:
            nsxy = ' '
            if command == 'l':
                x+=1
            elif command == 'r':
                x-=1
            elif command == 'd':
                y-=1
            elif command == 'u':
                y+=1
        else:
            if command == 'l':
                teleport([ns,x,y], x-1, y, mass)
                teleport([character_game,x+1,y],x,y,mass)
            elif command == 'r':
                teleport([ns,x,y], x+1, y, mass)
                coord_ris(px, mass)
                teleport([character_game,x-1,y], x, y, mass)
            elif command == 'd':
                teleport([ns,x,y], x, y+1, mass)
                coord_ris(px, mass)
                teleport([character_game,x,y-1], x, y, mass)
            elif command == 'u':
                teleport([ns,x,y], x, y-1, mass)
                coord_ris(px, mass)
                teleport([character_game,x,y+1], x, y, mass)
    elif ns == walk:
        ns = ' '
        if command == 'l':
            x+=1
        elif command == 'r':
            x-=1
        elif command == 'd':
            y-=1
        elif command == 'u':
            y+=1
    else:
         
        teleport(px, x, y, mass)


    return [cur_point,x,y]


def sokoban_game(x: int,y: int,character_game: str,mass: list,bonus: str,walk: str,bonuscords: list, wins: list):
    bones_kol = len(bonuscords)
    # bonuxx = 
    # bonuxy = 
    smb = character_game
    # coord_ris([bonus,bonuxx,bonuxy], mass)
    nol1 = 0
    while nol1 < bones_kol:
        bonuxx = bonuscords[nol1]
        bonuxy = bonuscords[nol1+1]
        # smb = ' '
        coord_ris([bonus,bonuxx,bonuxy], mass)
        nol1+=2
    nol = 0
    nol1 = 0
    wine = 0

    
    while nol == 0:
        print('u - вверх')
        print('d - вниз')
        print('l - влево')
        print('r - вправо')
        command = input('move ')
        
        px = [smb,x,y]
        xy = sokoban_hod(command,character_game,mass,px,bonus,walk)
        x = xy[1]
        y = xy[2]
        smb = xy[0]
        output_old(mass)
        win_kol = len(wins)
        # nol1 = 0
        if coord_isk([wins[nol1],wins[nol1+1]], mass) == bonus:
            nol1+=2
            # print('You WIN!!!')
            wine+=1
        if wine == win_kol/2:
            nol = 1
            
    # clear_screen()
    print('You WIN!!!')
        # if coord_isk([2,2], mass) == '#' :
        #     print('You WIN!!!')
        #     print('Ctrl + C - quit')
        #     while True:
        #         time.sleep(1)
            # nol = 1
            



