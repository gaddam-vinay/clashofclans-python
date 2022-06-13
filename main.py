from distutils.command.build import build
import string
from colorama import *
import colorama
from matplotlib.pyplot import flag
from nbformat import write
import numpy as np
from input import *
from objects import *
from control import *
import time
import os
init(autoreset=True)
starttime = time.time()
building_cordinates = np.full((51, 51), 0, dtype=int)
barbarian_cordinates = np.full((51, 51), 0, dtype=int)
archer_cordinates = np.full((51, 51), 0, dtype=int)
baloon_cordinates = np.full((51, 51), 0, dtype=int)
# 1-100 huts   101 =townhall  1001=wall  10001=canon
level = 1
hutx = [10, 30, 8, 23, 30]
huty = [10, 10, 27, 30, 23]
canonx = [9, 28]
canony = [21, 17]
wizardx = [15, 23]
wizardy = [15, 22]
canons = []
wizards = []
healthhut = 100
townhallhealth = 300
canonhealth = 100
townx = 18
towny = 18
huts = []
buildings = []
defencebuildings = []
barbarians = []
archers = []
baloons = []
barbarianscount = []
archerscount = []
baloonscount = []
canonrange = 6
wizardrange = 6
archerrange = 7
barbarianhealth = 100
archerhealth = 100
baloonhealth = 100
kinghealth = 1000
kingdamage = 10
queendamage = 10
barbariandamage = 10
canondamage = 20
wizarddamage = 20
archerdamage = 5
baloondamage = 10
timeinterval = 0.3
totalnumberofbarbarians = 10
numberofbarbariansgenerated = 0
totalnumberofarchers = 3
totalnumberofbaloons = 4
numberofarchersgenerated = 0
numberofbaloonsgenerated = 0
minbar = [0, 9]
prevstep = 'a'
gaddam = 0
queenattacktime = []


def spawningbarbs(x):
    if(numberofbarbariansgenerated < totalnumberofbarbarians):
        if(x == 1):
            x = barbarian(20, 3, barbarianhealth)
            barbarians.append(x)
            barbarianscount.append(x)
            barbarian_cordinates[3][20] = barbarian_cordinates[3][20]+1
        if(x == 2):
            x = barbarian(37, 15, barbarianhealth)
            barbarians.append(x)
            barbarianscount.append(x)
            barbarian_cordinates[15][37] = barbarian_cordinates[15][37]+1
        if(x == 3):
            x = barbarian(18, 35, barbarianhealth)
            barbarians.append(x)
            barbarianscount.append(x)
            barbarian_cordinates[35][18] = barbarian_cordinates[35][18]+1


def spawningarchers(x):
    if(numberofarchersgenerated < totalnumberofarchers):
        if(x == 1):
            x = archer(19, 3, archerhealth)
            archers.append(x)
            archerscount.append(x)
            archer_cordinates[3][19] = archer_cordinates[3][19]+1
        if(x == 2):
            x = archer(36, 16, archerhealth)
            archers.append(x)
            archerscount.append(x)
            archer_cordinates[16][36] = archer_cordinates[16][36]+1
        if(x == 3):
            x = archer(17, 35, archerhealth)
            archers.append(x)
            archerscount.append(x)
            archer_cordinates[35][17] = archer_cordinates[35][17]+1


def spawningbaloons(x):
    if(numberofbaloonsgenerated < totalnumberofbaloons):
        if(x == 1):
            x = baloon(21, 3, baloonhealth)
            baloons.append(x)
            baloonscount.append(x)
            baloon_cordinates[3][21] = baloon_cordinates[3][21]+1
        if(x == 2):
            x = baloon(37, 14, baloonhealth)
            baloons.append(x)
            baloonscount.append(x)
            baloon_cordinates[14][37] = baloon_cordinates[14][37]+1
        if(x == 3):
            x = baloon(16, 35, baloonhealth)
            baloons.append(x)
            baloonscount.append(x)
            baloon_cordinates[35][16] = baloon_cordinates[35][16]+1


def buildvillage1():
    for i in range(1, 41):
        for j in range(1, 41):
            print(Back.GREEN+"\033[%s;%sH" % (i, 2*j)+"  ")
        # hut 1

    for i in range(len(hutx)):
        huttttt = hut(healthhut, hutx[i], huty[i], building_cordinates)
        huts.append(huttttt)
        buildings.append(huttttt)
    # hut1 = hut(healthhut, hutx[0], huty[0], building_cordinates)
    # huts.append(hut1)
    # buildings.append(hut1)
    # # hut 2
    # hut2 = hut(healthhut, hutx[1], huty[1], building_cordinates)
    # huts.append(hut2)
    # buildings.append(hut2)
    # # hut 3
    # hut3 = hut(healthhut, hutx[2], huty[2], building_cordinates)
    # huts.append(hut3)
    # buildings.append(hut3)
    # # hut 4
    # hut4 = hut(healthhut, hutx[3], huty[3], building_cordinates)
    # huts.append(hut4)
    # buildings.append(hut4)
    # # hut 5
    # hut5 = hut(healthhut, hutx[4], huty[4], building_cordinates)
    # huts.append(hut5)
    # buildings.append(hut5)
    # town hall
    townhall1 = townhall(townhallhealth, townx, towny, building_cordinates)
    buildings.append(townhall1)
    # canon
    for i in range(len(canonx)):
        huttttt = canon(canonhealth, canonx[i], canony[i], building_cordinates)
        canons.append(huttttt)
        buildings.append(huttttt)
        defencebuildings.append(huttttt)
    # canon1 = canon(canonhealth, canonx[0], canony[0], building_cordinates)
    # canons.append(canon1)
    # buildings.append(canon1)
    # canon2 = canon(canonhealth, canonx[1], canony[1], building_cordinates)
    # canons.append(canon2)
    # buildings.append(canon2)
    for i in range(len(wizardx)):
        huttttt = wizard(
            canonhealth, wizardx[i], wizardy[i], building_cordinates)
        wizards.append(huttttt)
        buildings.append(huttttt)
        defencebuildings.append(huttttt)
    # wall
    for i in range(14):
        print(Back.BLACK+"\033[%s;%sH" % (13, 2*13+2*i)+"  ")
        building_cordinates[13][13+i] = 1005
        print(Back.BLACK+"\033[%s;%sH" % (25, 2*13 + 2*i)+"  ")
        building_cordinates[25][13+i] = 1005

    for i in range(13):
        print(Back.BLACK+"\033[%s;%sH" % (13+i, 2*13)+"  ")
        building_cordinates[13+i][13] = 1005
        print(Back.BLACK+"\033[%s;%sH" % (13+i, 2*26)+"  ")
        building_cordinates[13+i][26] = 1005
    return townhall1


while(level <= 3):
    hut.hutno = 0
    canon.canonno = 10000
    wizard.wizardno = 100000
    if(level == 2):
        hutx = [10, 9, 30, 22, 26, 15]
        huty = [10, 20, 15, 8, 28, 29]
        canonx = [16, 16, 30, 22]
        canony = [22, 10, 10, 28]
        wizardx = [10, 23, 30]
        wizardy = [15, 15, 23]
        canons = []
        wizards = []
        townx = 18
        towny = 18
        huts = []
        buildings = []
        defencebuildings = []
        barbarians = []
        archers = []
        baloons = []
        barbarianscount = []
        archerscount = []
        baloonscount = []
        totalnumberofbarbarians = 12
        numberofbarbariansgenerated = 0
        totalnumberofarchers = 4
        totalnumberofbaloons = 8
        numberofarchersgenerated = 0
        numberofbaloonsgenerated = 0
        queenattacktime = []
        for i in range(50):
            for j in range(50):
                building_cordinates[i][j] = 0
                barbarian_cordinates[i][j] = 0
                archer_cordinates[i][j] = 0
                baloon_cordinates[i][j] = 0
    if(level == 3):
        hutx = [14, 22, 9, 9, 25, 29, 15, 26]
        huty = [9, 15, 24, 16, 9, 18, 27, 28]
        canonx = [15, 20, 20, 29, 9]
        canony = [22, 8, 28, 24, 12]
        wizardx = [15, 23, 7, 29, 9]
        wizardy = [15, 22, 20, 13, 28]
        canons = []
        wizards = []
        townx = 18
        towny = 18
        huts = []
        buildings = []
        defencebuildings = []
        barbarians = []
        archers = []
        baloons = []
        barbarianscount = []
        archerscount = []
        baloonscount = []
        totalnumberofbarbarians = 18
        numberofbarbariansgenerated = 0
        totalnumberofarchers = 5
        totalnumberofbaloons = 8
        numberofarchersgenerated = 0
        numberofbaloonsgenerated = 0
        queenattacktime = []
        for i in range(50):
            for j in range(50):
                building_cordinates[i][j] = 0
                barbarian_cordinates[i][j] = 0
                archer_cordinates[i][j] = 0
                baloon_cordinates[i][j] = 0
    takein = input("Enter king/queen to play with king/queen: ")
    if(takein != 'king' and takein != 'queen'):
        print("invalid input")
        exit()
    print(colorama.ansi.clear_screen())
    townhall1 = buildvillage1()
    if(takein == 'king'):
        king1 = king(kinghealth)
    elif(takein == 'queen'):
        king1 = archerqueen(kinghealth)
    time0 = time.time()
    timeee = timeinterval
    loop = 1
    king1.change_health(0)
    # gameloop
    while(1):
        if(len(queenattacktime) > 0):
            if(time.time() > queenattacktime[0]+1):
                queenattacktime.remove(queenattacktime[0])
                input1 = 'x'
                controlqueen(input1, building_cordinates, king1,
                             huts, townhall1, barbarian_cordinates, archer_cordinates, baloon_cordinates, canons, wizards, prevstep, queendamage)
        input1 = input_to(Get().__call__)
        # keep king1.change down of canon.change_health
        for i in canons:
            if(i.dead == 0):
                i.change_health(0, building_cordinates)
        for i in wizards:
            if(i.dead == 0):
                i.change_health(0, building_cordinates)
        king1.change_health(0)
        # print(Back.BLUE+Fore.RED+Style.BRIGHT +
        #       "\033[%s;%sH" % (king1.y, 2*king1.x)+"KI")
        if(input1 == 'I' or input1 == 'i'):
            spawningbarbs(1)
            numberofbarbariansgenerated = numberofbarbariansgenerated+1
        elif(input1 == 'o' or input1 == 'O'):
            spawningbarbs(2)
            numberofbarbariansgenerated = numberofbarbariansgenerated+1
        elif(input1 == 'p' or input1 == 'P'):
            spawningbarbs(3)
            numberofbarbariansgenerated = numberofbarbariansgenerated+1
        elif(input1 == 'j' or input1 == 'J'):
            spawningarchers(1)
            numberofarchersgenerated = numberofarchersgenerated+1
        elif(input1 == 'k' or input1 == 'K'):
            spawningarchers(2)
            numberofarchersgenerated = numberofarchersgenerated+1
        elif(input1 == 'l' or input1 == 'L'):
            spawningarchers(3)
            numberofarchersgenerated = numberofarchersgenerated+1
        elif(input1 == 'b' or input1 == 'B'):
            spawningbaloons(1)
            numberofbaloonsgenerated = numberofbaloonsgenerated+1
        elif(input1 == 'n' or input1 == 'N'):
            spawningbaloons(2)
            numberofbaloonsgenerated = numberofbaloonsgenerated+1
        elif(input1 == 'm' or input1 == 'M'):
            spawningbaloons(3)
            numberofbaloonsgenerated = numberofbaloonsgenerated+1
        elif(input1 == 'h' or input1 == 'H'):
            king1.increase_health()
            for i in barbarians:
                i.increase_health()
            for i in archers:
                i.increase_health()
            for i in baloons:
                i.increase_health()
        elif(input1 == 'R' or input1 == 'r'):
            loop = 2
        else:
            if(king1.dead != 1):
                if(input1 == 'a' or input1 == 'A' or input1 == 'w' or input1 == 'W' or input1 == 's' or input1 == 'S' or input1 == 'd' or input1 == 'D'):
                    prevstep = input1
                if(takein == 'king'):
                    controlking(input1, building_cordinates, king1,
                                huts, townhall1, barbarian_cordinates, archer_cordinates, baloon_cordinates, canons, wizards, kingdamage)
                else:
                    if(input1 == 'x' or input1 == 'X'):
                        queenattacktime.append(time.time())
                    else:
                        controlqueen(input1, building_cordinates, king1,
                                     huts, townhall1, barbarian_cordinates, archer_cordinates, baloon_cordinates, canons, wizards, prevstep, queendamage)
            else:
                if(barbarian_cordinates[king1.y][king1.x] != 0):
                    print(Back.MAGENTA+Fore.RED+Style.BRIGHT +
                          "\033[%s;%sH" % (king1.y, 2*king1.x)+"BR")
                elif(archer_cordinates[king1.y][king1.x] != 0):
                    print(Back.LIGHTYELLOW_EX+Fore.RED+Style.BRIGHT +
                          "\033[%s;%sH" % (king1.y, 2*king1.x)+"AR")
                elif(baloon_cordinates[king1.y][king1.x] != 0):
                    print(Back.LIGHTWHITE_EX+Fore.BLUE+Style.BRIGHT +
                          "\033[%s;%sH" % (king1.y, 2*king1.x)+"BL")
                else:
                    print(Back.GREEN +
                          "\033[%s;%sH" % (king1.y, 2*king1.x)+"  ")
        if(time.time()-time0 > timeee):
            timeee = time.time()-time0+timeinterval
            for i in barbarians:
                if(i.dead == 1):
                    barbarians.remove(i)
                    if(barbarian_cordinates[i.y][i.x] != 1):
                        print(Back.MAGENTA+Fore.RED+Style.BRIGHT +
                              "\033[%s;%sH" % (i.y, 2*i.x)+"BR")
                    elif(king1.x == i.x and king1.y == i.y):
                        if(takein == 'king'):
                            print(Back.BLUE+Fore.RED+Style.BRIGHT +
                                  "\033[%s;%sH" % (king1.y, 2*king1.x)+"KI")
                        else:
                            print(Back.RED+Fore.WHITE+Style.BRIGHT +
                                  "\033[%s;%sH" % (king1.y, 2*king1.x)+"QU")
                    elif(archer_cordinates[i.y][i.x] != 0):
                        print(Back.LIGHTYELLOW_EX+Fore.RED+Style.BRIGHT +
                              "\033[%s;%sH" % (i.y, 2*i.x)+"AR")
                    elif(baloon_cordinates[i.y][i.x] != 0):
                        print(Back.LIGHTWHITE_EX+Fore.BLUE+Style.BRIGHT +
                              "\033[%s;%sH" % (i.y, 2*i.x)+"BL")
                    else:
                        print(Back.GREEN +
                              "\033[%s;%sH" % (i.y, 2*i.x)+"  ")
                    barbarian_cordinates[i.y][i.x] = barbarian_cordinates[i.y][i.x]-1
            for i in archers:
                if(i.dead == 1):
                    archers.remove(i)
                    if(king1.x == i.x and king1.y == i.y):
                        if(takein == 'king'):
                            print(Back.BLUE+Fore.RED+Style.BRIGHT +
                                  "\033[%s;%sH" % (king1.y, 2*king1.x)+"KI")
                        else:
                            print(Back.RED+Fore.WHITE+Style.BRIGHT +
                                  "\033[%s;%sH" % (king1.y, 2*king1.x)+"QU")
                    elif(barbarian_cordinates[i.y][i.x] != 0):
                        print(Back.MAGENTA+Fore.RED+Style.BRIGHT +
                              "\033[%s;%sH" % (i.y, 2*i.x)+"BR")
                    elif(archer_cordinates[i.y][i.x] != 1):
                        print(Back.LIGHTYELLOW_EX+Fore.RED+Style.BRIGHT +
                              "\033[%s;%sH" % (i.y, 2*i.x)+"AR")
                    elif(baloon_cordinates[i.y][i.x] != 0):
                        print(Back.LIGHTWHITE_EX+Fore.BLUE+Style.BRIGHT +
                              "\033[%s;%sH" % (i.y, 2*i.x)+"BL")
                    else:
                        print(Back.GREEN +
                              "\033[%s;%sH" % (i.y, 2*i.x)+"  ")
                    archer_cordinates[i.y][i.x] = archer_cordinates[i.y][i.x]-1
            for i in baloons:
                if(i.dead == 1):
                    baloons.remove(i)
                    if(king1.x == i.x and king1.y == i.y):
                        if(takein == 'king'):
                            print(Back.BLUE+Fore.RED+Style.BRIGHT +
                                  "\033[%s;%sH" % (king1.y, 2*king1.x)+"KI")
                        else:
                            print(Back.RED+Fore.WHITE+Style.BRIGHT +
                                  "\033[%s;%sH" % (king1.y, 2*king1.x)+"QU")
                    elif(barbarian_cordinates[i.y][i.x] != 0):
                        print(Back.MAGENTA+Fore.RED+Style.BRIGHT +
                              "\033[%s;%sH" % (i.y, 2*i.x)+"BR")
                    elif(archer_cordinates[i.y][i.x] != 0):
                        print(Back.LIGHTYELLOW_EX+Fore.RED+Style.BRIGHT +
                              "\033[%s;%sH" % (i.y, 2*i.x)+"AR")
                    elif(baloon_cordinates[i.y][i.x] != 1):
                        print(Back.LIGHTWHITE_EX+Fore.BLUE+Style.BRIGHT +
                              "\033[%s;%sH" % (i.y, 2*i.x)+"BL")
                    else:
                        print(Back.GREEN +
                              "\033[%s;%sH" % (i.y, 2*i.x)+"  ")
                    baloon_cordinates[i.y][i.x] = baloon_cordinates[i.y][i.x]-1
            for i in buildings:
                if(i.dead == 1):
                    buildings.remove(i)
            for i in defencebuildings:
                if(i.dead == 1):
                    defencebuildings.remove(i)
            for i in barbarians:
                if(i.target == 0 or i.target.dead == 1):
                    settarget(buildings, i)
            for i in archers:
                if(i.target == 0 or i.target.dead == 1):
                    settarget(buildings, i)
            for i in baloons:
                if(i.target == 0 or i.target.dead == 1):
                    if(len(defencebuildings) == 0):
                        settarget(buildings, i)
                    else:
                        settarget(defencebuildings, i)

            for j in range(loop):
                if(gaddam == 0):
                    gaddam = 1
                else:
                    gaddam = 0
                    for i in range(len(barbarians)):
                        input1 = " "
                        controlbar(input1, building_cordinates,
                                   barbarians[i], huts, townhall1, barbarian_cordinates, archer_cordinates, baloon_cordinates, canons, king1, wizards, takein, barbariandamage)
                        if(barbarians[i].target.y < barbarians[i].y):
                            input1 = "w"
                            controlbar(input1, building_cordinates,
                                       barbarians[i], huts, townhall1, barbarian_cordinates, archer_cordinates, baloon_cordinates, canons, king1, wizards, takein, barbariandamage)
                        if(barbarians[i].target.y > barbarians[i].y):
                            input1 = "s"
                            controlbar(input1, building_cordinates,
                                       barbarians[i], huts, townhall1, barbarian_cordinates, archer_cordinates, baloon_cordinates, canons, king1, wizards, takein, barbariandamage)
                        if(barbarians[i].target.x > barbarians[i].x):
                            input1 = "d"
                            controlbar(input1, building_cordinates,
                                       barbarians[i], huts, townhall1, barbarian_cordinates, archer_cordinates, baloon_cordinates, canons, king1, wizards, takein, barbariandamage)
                        if(barbarians[i].target.x < barbarians[i].x):
                            input1 = "a"
                            controlbar(input1, building_cordinates,
                                       barbarians[i], huts, townhall1, barbarian_cordinates, archer_cordinates, baloon_cordinates, canons, king1, wizards, takein, barbariandamage)
                for i in range(len(archers)):
                    flag = 0
                    input1 = " "
                    controlarcher(input1, building_cordinates,
                                  archers[i], huts, townhall1, barbarian_cordinates, archer_cordinates, baloon_cordinates, canons, king1, wizards, takein)
                    if(archers[i].target.y+archerrange < archers[i].y):
                        flag = 1
                        input1 = "w"
                        controlarcher(input1, building_cordinates,
                                      archers[i], huts, townhall1, barbarian_cordinates, archer_cordinates, baloon_cordinates, canons, king1, wizards, takein)
                    if(archers[i].target.y > archers[i].y+archerrange):
                        flag = 1
                        input1 = "s"
                        controlarcher(input1, building_cordinates,
                                      archers[i], huts, townhall1, barbarian_cordinates, archer_cordinates, baloon_cordinates, canons, king1, wizards, takein)
                    if(archers[i].target.x > archers[i].x+archerrange):
                        flag = 1
                        input1 = "d"
                        controlarcher(input1, building_cordinates,
                                      archers[i], huts, townhall1, barbarian_cordinates, archer_cordinates, baloon_cordinates, canons, king1, wizards, takein)
                    if(archers[i].target.x+archerrange < archers[i].x):
                        flag = 1
                        input1 = "a"
                        controlarcher(input1, building_cordinates,
                                      archers[i], huts, townhall1, barbarian_cordinates, archer_cordinates, baloon_cordinates, canons, king1, wizards, takein)
                    if(flag == 0):
                        archers[i].target.change_health(
                            archerdamage, building_cordinates)
                for i in range(len(baloons)):
                    flag = 0

                    if(baloons[i].target.y < baloons[i].y):
                        flag = 1
                        input1 = "w"
                        controlbaloon(input1, building_cordinates,
                                      baloons[i], huts, townhall1, barbarian_cordinates, archer_cordinates, baloon_cordinates, canons, king1, wizards, takein)
                    if(baloons[i].target.y > baloons[i].y):
                        flag = 1
                        input1 = "s"
                        controlbaloon(input1, building_cordinates,
                                      baloons[i], huts, townhall1, barbarian_cordinates, archer_cordinates, baloon_cordinates, canons, king1, wizards, takein)
                    if(baloons[i].target.x > baloons[i].x):
                        flag = 1
                        input1 = "d"
                        controlbaloon(input1, building_cordinates,
                                      baloons[i], huts, townhall1, barbarian_cordinates, archer_cordinates, baloon_cordinates, canons, king1, wizards, takein)
                    if(baloons[i].target.x < baloons[i].x):
                        flag = 1
                        input1 = "a"
                        controlbaloon(input1, building_cordinates,
                                      baloons[i], huts, townhall1, barbarian_cordinates, archer_cordinates, baloon_cordinates, canons, king1, wizards, takein)
                    if(flag == 0):
                        baloons[i].target.change_health(
                            baloondamage, building_cordinates)
                        print(Back.LIGHTWHITE_EX+Fore.BLUE+Style.BRIGHT +
                              "\033[%s;%sH" % (baloons[i].y, 2*baloons[i].x)+"BL")
            # canon attackes the nearest one
            # for 1st canon
            arplusbar = archers+barbarians
            for i in range(len(canonx)):
                if(canons[i].dead == 0):
                    flag = 0
                    if((king1.x <= canonx[i]+canonrange and king1.x >= canonx[i]-canonrange) and (king1.y <= canony[i]+canonrange and king1.y >= canony[i]-canonrange) and king1.dead == 0):
                        king1.change_health(canondamage)
                        canons[i].attackcolor()
                    else:
                        for j in arplusbar:
                            min1 = 10000
                            if((j.x <= canonx[i]+canonrange and j.x >= canonx[i]-canonrange) and (j.y <= canony[i]+canonrange and j.y >= canony[i]-canonrange)):
                                flag = 1
                                if(min1 > abs(canonx[i]-j.x)+abs(canony[i]-j.y)):
                                    min1 = abs(canonx[i]-j.x) + \
                                        abs(canony[i]-j.y)
                                    minbar[0] = j
                    if(flag == 1):
                        minbar[0].change_health(canondamage)
                        canons[i].attackcolor()
            # if(canons[0].dead == 0):
            #     flag = 0
            #     minbar = [1, 2]
            #     if((king1.x <= canonx[0]+canonrange and king1.x >= canonx[0]-canonrange) and (king1.y <= canony[0]+canonrange and king1.y >= canony[0]-canonrange) and king1.dead == 0):
            #         king1.change_health(canondamage)
            #         canons[0].attackcolor()
            #     else:
            #         for i in barbarians:
            #             min1 = 10000
            #             if((i.x <= canonx[0]+canonrange and i.x >= canonx[0]-canonrange) and (i.y <= canony[0]+canonrange and i.y >= canony[0]-canonrange)):
            #                 flag = 1
            #                 if(min1 > abs(canonx[0]-i.x)+abs(canony[0]-i.y)):
            #                     min1 = abs(canonx[0]-i.x)+abs(canony[0]-i.y)
            #                     minbar[0] = i
            #     if(flag == 1):
            #         minbar[0].change_health(canondamage)
            #         canons[0].attackcolor()
            # if(canons[1].dead == 0):
            #     flag = 0
            #     if((king1.x <= canonx[1]+canonrange and king1.x >= canonx[1]-canonrange) and (king1.y <= canony[1]+canonrange and king1.y >= canony[1]-canonrange) and king1.dead == 0):
            #         king1.change_health(canondamage)
            #         canons[1].attackcolor()
            #     else:
            #         for i in barbarians:
            #             min1 = 10000
            #             if((i.x <= canonx[1]+canonrange and i.x >= canonx[1]-canonrange) and (i.y <= canony[1]+canonrange and i.y >= canony[1]-canonrange)):
            #                 flag = 1
            #                 if(min1 > abs(canonx[1]-i.x)+abs(canony[1]-i.y)):
            #                     min1 = abs(canonx[1]-i.x)+abs(canony[1]-i.y)
            #                     minbar[1] = i
            #     if(flag == 1):
            #         minbar[1].change_health(canondamage)
            #         canons[1].attackcolor()
            # wizzard attack
            alltroops = archers+barbarians+baloons
            for i in range(len(wizardx)):
                if(wizards[i].dead == 0):
                    flag = 0
                    if((king1.x <= wizardx[i]+wizardrange and king1.x >= wizardx[i]-wizardrange) and (king1.y <= wizardy[i]+wizardrange and king1.y >= wizardy[i]-wizardrange) and king1.dead == 0):
                        king1.change_health(wizarddamage)
                        wizards[i].attackcolor()
                        for ff in alltroops:
                            if(abs(ff.x-king1.x) <= 1 and abs(ff.y-king1.y) <= 1):
                                ff.change_health(wizarddamage)
                    else:
                        for j in alltroops:
                            min1 = 10000
                            if((j.x <= wizardx[i]+wizardrange and j.x >= wizardx[i]-wizardrange) and (j.y <= wizardy[i]+wizardrange and j.y >= wizardy[i]-wizardrange)):
                                flag = 1
                                if(min1 > abs(wizardx[i]-j.x)+abs(wizardy[i]-j.y)):
                                    min1 = abs(wizardx[i]-j.x) + \
                                        abs(wizardy[i]-j.y)
                                    minbar[0] = j
                    if(flag == 1):
                        minbar[0].change_health(wizarddamage)
                        for ff in alltroops:
                            if(abs(ff.x-minbar[0].x) <= 1 and abs(ff.y-minbar[0].y) <= 1):
                                ff.change_health(wizarddamage)
                        wizards[i].attackcolor()

            #victory or defeat
            if(len(buildings) == 0):
                print(colorama.ansi.clear_screen())
                print(Fore.YELLOW+Style.BRIGHT +
                      "\033[%s;%sH" % (3, 2*40)+"VICTORY")
                if(king1.dead == 0):
                    if(takein == 'king'):
                        print(Fore.RED+Style.BRIGHT +
                              "\033[%s;%sH" % (8, 2*10)+"KING ALIVE")
                    else:
                        print(Fore.CYAN+Style.BRIGHT +
                              "\033[%s;%sH" % (8, 2*10)+"QUEEN ALIVE")
                else:
                    if(takein == 'king'):
                        print(Fore.RED+Style.BRIGHT +
                              "\033[%s;%sH" % (8, 2*10)+"KING DEAD")
                    else:
                        print(Fore.CYAN+Style.BRIGHT +
                              "\033[%s;%sH" % (8, 2*10)+"QUEEN DEAD")
                print(Fore.RED+Style.BRIGHT +
                      "\033[%s;%sH" % (10, 2*10)+"Number of Barbarians fought: %s" % (len(barbarianscount)))
                j = 0
                for i in barbarianscount:
                    if(i.dead == 1):
                        j = j+1
                print(Fore.RED+Style.BRIGHT +
                      "\033[%s;%sH" % (12, 2*10)+"Number of Barbarians died: %s" % (j))
                print(Fore.RED+Style.BRIGHT +
                      "\033[%s;%sH" % (14, 2*10)+"Number of archers fought: %s" % (len(archerscount)))
                j = 0
                for i in archerscount:
                    if(i.dead == 1):
                        j = j+1
                print(Fore.RED+Style.BRIGHT +
                      "\033[%s;%sH" % (16, 2*10)+"Number of archers died: %s" % (j))
                print(Fore.RED+Style.BRIGHT +
                      "\033[%s;%sH" % (18, 2*10)+"Number of Baloons fought: %s" % (len(baloonscount)))
                j = 0
                for i in baloonscount:
                    if(i.dead == 1):
                        j = j+1
                print(Fore.RED+Style.BRIGHT +
                      "\033[%s;%sH" % (20, 2*10)+"Number of Baloons died: %s" % (j))
                print()
                print()
                k = input("do you want to play next level of game: (yes/no) = ")
                if(k == 'yes'):
                    level = level+1
                else:
                    exit()
                break
            elif(len(barbarianscount) == totalnumberofbarbarians and king1.dead == 1 and len(barbarians) == 0 and len(baloons) == 0 and len(archers) == 0 and len(baloonscount) == totalnumberofbaloons and len(archerscount) == totalnumberofarchers):
                print(colorama.ansi.clear_screen())
                print(Fore.YELLOW+Style.BRIGHT +
                      "\033[%s;%sH" % (3, 2*40)+"DEFEAT")
                j = 0
                for i in huts:
                    if(i.dead == 1):
                        j = j+1
                print(Fore.RED+Style.BRIGHT +
                      "\033[%s;%sH" % (8, 2*10)+"Number of huts destroyed completely: %s" % (j))
                j = 0
                for i in canons:
                    if(i.dead == 1):
                        j = j+1
                print(Fore.RED+Style.BRIGHT +
                      "\033[%s;%sH" % (10, 2*10)+"Number of canons destroyed: %s" % (j))
                j = 0
                for i in wizards:
                    if(i.dead == 1):
                        j = j+1
                print(Fore.RED+Style.BRIGHT +
                      "\033[%s;%sH" % (12, 2*10)+"Number of wizards destroyed: %s" % (j))
                if(townhall1.dead == 1):
                    print(Fore.RED+Style.BRIGHT +
                          "\033[%s;%sH" % (14, 2*10)+"Townhall destroyed")
                else:
                    print(Fore.RED+Style.BRIGHT +
                          "\033[%s;%sH" % (14, 2*10)+"Townhall not destroyed")
                print()
                print()
                k = input("do you want to play next level of game: (yes/no) = ")
                if(k == 'yes'):
                    level = level+1
                else:
                    exit()
                break
