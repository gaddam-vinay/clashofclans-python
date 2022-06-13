
from colorama import *
from pyrsistent import b
from objects import *


def controlking(input, building_cordinates, king1, huts, townhall1, barbarian_cordinates, archer_cordinates, baloon_cordinates, canons, wizards, kingdamage):
    if(input == 'w' or input == 'W'):
        if(king1.y-1 <= 0):
            return
        if(building_cordinates[king1.y-1][king1.x] == 0 or building_cordinates[king1.y-1][king1.x] < 0):
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
            king1.y = king1.y-1
            print(Back.BLUE+Fore.RED+Style.BRIGHT +
                  "\033[%s;%sH" % (king1.y, 2*king1.x)+"KI")
    elif(input == 's' or input == 'S'):
        if(king1.y+1 > 40):
            return
        if(building_cordinates[king1.y+1][king1.x] == 0 or building_cordinates[king1.y+1][king1.x] < 0):
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
            king1.y = king1.y+1
            print(Back.BLUE+Fore.RED+Style.BRIGHT +
                  "\033[%s;%sH" % (king1.y, 2*king1.x)+"KI")
    elif(input == 'a' or input == 'A'):
        if(king1.x-1 <= 0):
            return
        if(building_cordinates[king1.y][king1.x-1] == 0 or building_cordinates[king1.y][king1.x-1] < 0):
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
            king1.x = king1.x-1
            print(Back.BLUE+Fore.RED+Style.BRIGHT +
                  "\033[%s;%sH" % (king1.y, 2*king1.x)+"KI")
    elif(input == 'd' or input == 'D'):
        if(king1.x+1 > 40):
            return
        if(building_cordinates[king1.y][king1.x+1] == 0 or building_cordinates[king1.y][king1.x+1] < 0):
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
            king1.x = king1.x+1
            print(Back.BLUE+Fore.RED+Style.BRIGHT +
                  "\033[%s;%sH" % (king1.y, 2*king1.x)+"KI")
    elif(input == " "):
        if(building_cordinates[king1.y][king1.x] < 0 and building_cordinates[king1.y][king1.x] > -100):
            huts[-building_cordinates[king1.y][king1.x] -
                 1].change_health(kingdamage, building_cordinates)
        elif(building_cordinates[king1.y][king1.x] == -101):
            townhall1.change_health(kingdamage, building_cordinates)
        elif(building_cordinates[king1.y][king1.x] <= -10000 and building_cordinates[king1.y][king1.x] > -100000):
            canons[-building_cordinates[king1.y][king1.x] -
                   10001].change_health(kingdamage, building_cordinates)
        elif(building_cordinates[king1.y][king1.x] <= -100000):
            wizards[-building_cordinates[king1.y][king1.x] -
                    100001].change_health(kingdamage, building_cordinates)
        elif(building_cordinates[king1.y][king1.x+1] >= 1000 and building_cordinates[king1.y][king1.x+1] < 10000):
            if(building_cordinates[king1.y][king1.x+1] == 1000):
                print(Back.GREEN +
                      "\033[%s;%sH" % (king1.y, 2*king1.x+2)+"  ")
                building_cordinates[king1.y][king1.x+1] = 0
            else:
                building_cordinates[king1.y][king1.x +
                                             1] = building_cordinates[king1.y][king1.x+1]-1
        elif(building_cordinates[king1.y+1][king1.x] >= 1000 and building_cordinates[king1.y+1][king1.x] < 10000):
            if(building_cordinates[king1.y+1][king1.x] == 1000):
                print(Back.GREEN +
                      "\033[%s;%sH" % (king1.y+1, 2*king1.x)+"  ")
                building_cordinates[king1.y+1][king1.x] = 0
            else:
                building_cordinates[king1.y +
                                    1][king1.x] = building_cordinates[king1.y+1][king1.x]-1
        elif(building_cordinates[king1.y-1][king1.x] >= 1000 and building_cordinates[king1.y-1][king1.x] < 10000):
            if(building_cordinates[king1.y-1][king1.x] == 1000):
                print(Back.GREEN +
                      "\033[%s;%sH" % (king1.y-1, 2*king1.x)+"  ")
                building_cordinates[king1.y-1][king1.x] = 0
            else:
                building_cordinates[king1.y -
                                    1][king1.x] = building_cordinates[king1.y-1][king1.x]-1
        elif(building_cordinates[king1.y][king1.x-1] >= 1000 and building_cordinates[king1.y][king1.x-1] < 10000):
            if(building_cordinates[king1.y][king1.x-1] == 1000):
                print(Back.GREEN +
                      "\033[%s;%sH" % (king1.y, 2*king1.x-2)+"  ")
                building_cordinates[king1.y][king1.x-1] = 0
            else:
                building_cordinates[king1.y][king1.x -
                                             1] = building_cordinates[king1.y][king1.x-1]-1
    elif(input == "x" or input == "X"):
        s = {0}
        s.remove(0)
        xk = king1.x-5
        yk = king1.y-5
        for i in range(10):
            for j in range(10):
                if(xk+i > 0 and xk+i < 40 and yk+j > 0 and yk+j < 40):
                    s.add(building_cordinates[yk+j][xk+i])
                    if(building_cordinates[yk+j][xk+i] >= 1000 and building_cordinates[yk+j][xk+i] < 10000):
                        if(building_cordinates[yk+j][xk+i] == 1000):
                            print(Back.GREEN +
                                  "\033[%s;%sH" % (yk+j, 2*(xk+i))+"  ")
                            building_cordinates[yk+j][xk+i] = 0
                        else:
                            building_cordinates[yk+j][xk +
                                                      i] = building_cordinates[yk+j][xk+i]-1
        for i in s:
            if(i > 0):

                if(i > 0 and i < 100):
                    huts[i -
                         1].change_health(kingdamage, building_cordinates)
                elif(i == 101):
                    townhall1.change_health(kingdamage, building_cordinates)
                elif(i > 10000 and i < 100000):
                    canons[i -
                           10001].change_health(kingdamage, building_cordinates)
                elif(i > 100000):
                    wizards[i -
                            100001].change_health(kingdamage, building_cordinates)


def controlbar(input, building_cordinates, barbarian, huts, townhall1, barbarian_cordinates, archer_cordinates, baloon_cordinates, canons, king1, wizards, takein, barbariandamage):
    if(input == 'w' or input == 'W'):
        if(barbarian.y-1 <= 0):
            return
        if(building_cordinates[barbarian.y-1][barbarian.x] == 0 or building_cordinates[barbarian.y-1][barbarian.x] < 0):
            if(barbarian_cordinates[barbarian.y][barbarian.x] != 1):
                print(Back.MAGENTA+Fore.RED+Style.BRIGHT +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"BR")
            elif(king1.x == barbarian.x and king1.y == barbarian.y):
                if(takein == 'king'):
                    print(Back.BLUE+Fore.RED+Style.BRIGHT +
                          "\033[%s;%sH" % (king1.y, 2*king1.x)+"KI")
                else:
                    print(Back.RED+Fore.WHITE+Style.BRIGHT +
                          "\033[%s;%sH" % (king1.y, 2*king1.x)+"QU")
            elif(archer_cordinates[barbarian.y][barbarian.x] != 0):
                print(Back.LIGHTYELLOW_EX+Fore.RED+Style.BRIGHT +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"AR")
            elif(baloon_cordinates[barbarian.y][barbarian.x] != 0):
                print(Back.LIGHTWHITE_EX+Fore.BLUE+Style.BRIGHT +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"BL")
            else:
                print(Back.GREEN +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"  ")
            barbarian_cordinates[barbarian.y][barbarian.x] = barbarian_cordinates[barbarian.y][barbarian.x]-1
            barbarian.y = barbarian.y-1
            barbarian_cordinates[barbarian.y][barbarian.x] = barbarian_cordinates[barbarian.y][barbarian.x]+1
            if(king1.x != barbarian.x or king1.y != barbarian.y):
                print(Back.MAGENTA+Fore.RED+Style.BRIGHT +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"BR")
    elif(input == 's' or input == 'S'):
        if(barbarian.y+1 > 40):
            return
        if(building_cordinates[barbarian.y+1][barbarian.x] == 0 or building_cordinates[barbarian.y+1][barbarian.x] < 0):
            if(barbarian_cordinates[barbarian.y][barbarian.x] != 1):
                print(Back.MAGENTA+Fore.RED+Style.BRIGHT +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"BR")
            elif(king1.x == barbarian.x and king1.y == barbarian.y):
                if(takein == 'king'):
                    print(Back.BLUE+Fore.RED+Style.BRIGHT +
                          "\033[%s;%sH" % (king1.y, 2*king1.x)+"KI")
                else:
                    print(Back.RED+Fore.WHITE+Style.BRIGHT +
                          "\033[%s;%sH" % (king1.y, 2*king1.x)+"QU")
            elif(archer_cordinates[barbarian.y][barbarian.x] != 0):
                print(Back.LIGHTYELLOW_EX+Fore.RED+Style.BRIGHT +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"AR")
            elif(baloon_cordinates[barbarian.y][barbarian.x] != 0):
                print(Back.LIGHTWHITE_EX+Fore.BLUE+Style.BRIGHT +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"BL")
            else:
                print(Back.GREEN +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"  ")
            barbarian_cordinates[barbarian.y][barbarian.x] = barbarian_cordinates[barbarian.y][barbarian.x]-1
            barbarian.y = barbarian.y+1
            barbarian_cordinates[barbarian.y][barbarian.x] = barbarian_cordinates[barbarian.y][barbarian.x]+1
            if(king1.x != barbarian.x or king1.y != barbarian.y):
                print(Back.MAGENTA+Fore.RED+Style.BRIGHT +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"BR")
    elif(input == 'a' or input == 'A'):
        if(barbarian.x-1 <= 0):
            return
        if(building_cordinates[barbarian.y][barbarian.x-1] == 0 or building_cordinates[barbarian.y][barbarian.x-1] < 0):
            if(barbarian_cordinates[barbarian.y][barbarian.x] != 1):
                print(Back.MAGENTA+Fore.RED+Style.BRIGHT +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"BR")
            elif(king1.x == barbarian.x and king1.y == barbarian.y):
                if(takein == 'king'):
                    print(Back.RED+Fore.WHITE+Style.BRIGHT +
                          "\033[%s;%sH" % (king1.y, 2*king1.x)+"KI")
                else:
                    print(Back.RED+Fore.WHITE+Style.BRIGHT +
                          "\033[%s;%sH" % (king1.y, 2*king1.x)+"QU")
            elif(archer_cordinates[barbarian.y][barbarian.x] != 0):
                print(Back.LIGHTYELLOW_EX+Fore.RED+Style.BRIGHT +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"AR")
            elif(baloon_cordinates[barbarian.y][barbarian.x] != 0):
                print(Back.LIGHTWHITE_EX+Fore.BLUE+Style.BRIGHT +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"BL")
            else:
                print(Back.GREEN +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"  ")
            barbarian_cordinates[barbarian.y][barbarian.x] = barbarian_cordinates[barbarian.y][barbarian.x]-1
            barbarian.x = barbarian.x-1
            barbarian_cordinates[barbarian.y][barbarian.x] = barbarian_cordinates[barbarian.y][barbarian.x]+1
            if(king1.x != barbarian.x or king1.y != barbarian.y):
                print(Back.MAGENTA+Fore.RED+Style.BRIGHT +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"BR")
    elif(input == 'd' or input == 'D'):
        if(barbarian.x+1 > 40):
            return
        if(building_cordinates[barbarian.y][barbarian.x+1] == 0 or building_cordinates[barbarian.y][barbarian.x+1] < 0):
            if(barbarian_cordinates[barbarian.y][barbarian.x] != 1):
                print(Back.MAGENTA+Fore.RED+Style.BRIGHT +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"BR")
            elif(king1.x == barbarian.x and king1.y == barbarian.y):
                if(takein == 'king'):
                    print(Back.BLUE+Fore.RED+Style.BRIGHT +
                          "\033[%s;%sH" % (king1.y, 2*king1.x)+"KI")
                else:
                    print(Back.RED+Fore.WHITE+Style.BRIGHT +
                          "\033[%s;%sH" % (king1.y, 2*king1.x)+"QU")
            elif(archer_cordinates[barbarian.y][barbarian.x] != 0):
                print(Back.LIGHTYELLOW_EX+Fore.RED+Style.BRIGHT +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"AR")
            elif(baloon_cordinates[barbarian.y][barbarian.x] != 0):
                print(Back.LIGHTWHITE_EX+Fore.BLUE+Style.BRIGHT +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"BL")
            else:
                print(Back.GREEN +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"  ")
            barbarian_cordinates[barbarian.y][barbarian.x] = barbarian_cordinates[barbarian.y][barbarian.x]-1
            barbarian.x = barbarian.x+1
            barbarian_cordinates[barbarian.y][barbarian.x] = barbarian_cordinates[barbarian.y][barbarian.x]+1
            if(king1.x != barbarian.x or king1.y != barbarian.y):
                print(Back.MAGENTA+Fore.RED+Style.BRIGHT +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"BR")
    elif(input == " "):
        if(building_cordinates[barbarian.y][barbarian.x] < 0 and building_cordinates[barbarian.y][barbarian.x] > -100):
            huts[-building_cordinates[barbarian.y][barbarian.x] -
                 1].change_health(barbariandamage, building_cordinates)
        elif(building_cordinates[barbarian.y][barbarian.x] == -101):
            townhall1.change_health(barbariandamage, building_cordinates)
        elif(building_cordinates[barbarian.y][barbarian.x] <= -10000 and building_cordinates[barbarian.y][barbarian.x] > -100000):
            canons[-building_cordinates[barbarian.y][barbarian.x] -
                   10001].change_health(barbariandamage, building_cordinates)
        elif(building_cordinates[barbarian.y][barbarian.x] <= -100000):
            wizards[-building_cordinates[barbarian.y][barbarian.x] -
                    100001].change_health(barbariandamage, building_cordinates)
        elif(building_cordinates[barbarian.y][barbarian.x+1] >= 1000 and building_cordinates[barbarian.y][barbarian.x+1] < 10000):
            if(building_cordinates[barbarian.y][barbarian.x+1] == 1000):
                print(Back.GREEN +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x+2)+"  ")
                building_cordinates[barbarian.y][barbarian.x+1] = 0
            else:
                building_cordinates[barbarian.y][barbarian.x +
                                                 1] = building_cordinates[barbarian.y][barbarian.x+1]-1
        elif(building_cordinates[barbarian.y+1][barbarian.x] >= 1000 and building_cordinates[barbarian.y+1][barbarian.x] < 10000):
            if(building_cordinates[barbarian.y+1][barbarian.x] == 1000):
                print(Back.GREEN +
                      "\033[%s;%sH" % (barbarian.y+1, 2*barbarian.x)+"  ")
                building_cordinates[barbarian.y+1][barbarian.x] = 0
            else:
                building_cordinates[barbarian.y +
                                    1][barbarian.x] = building_cordinates[barbarian.y+1][barbarian.x]-1
        elif(building_cordinates[barbarian.y-1][barbarian.x] >= 1000 and building_cordinates[barbarian.y-1][barbarian.x] < 10000):
            if(building_cordinates[barbarian.y-1][barbarian.x] == 1000):
                print(Back.GREEN +
                      "\033[%s;%sH" % (barbarian.y-1, 2*barbarian.x)+"  ")
                building_cordinates[barbarian.y-1][barbarian.x] = 0
            else:
                building_cordinates[barbarian.y -
                                    1][barbarian.x] = building_cordinates[barbarian.y-1][barbarian.x]-1
        elif(building_cordinates[barbarian.y][barbarian.x-1] >= 1000 and building_cordinates[barbarian.y][barbarian.x-1] < 10000):
            if(building_cordinates[barbarian.y][barbarian.x-1] == 1000):
                print(Back.GREEN +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x-2)+"  ")
                building_cordinates[barbarian.y][barbarian.x-1] = 0
            else:
                building_cordinates[barbarian.y][barbarian.x -
                                                 1] = building_cordinates[barbarian.y][barbarian.x-1]-1


def controlarcher(input, building_cordinates, barbarian, huts, townhall1, barbarian_cordinates, archer_cordinates, baloon_cordinates, canons, king1, wizards, takein):
    if(input == 'w' or input == 'W'):
        if(barbarian.y-1 <= 0):
            return
        if(building_cordinates[barbarian.y-1][barbarian.x] == 0 or building_cordinates[barbarian.y-1][barbarian.x] < 0):
            if(barbarian_cordinates[barbarian.y][barbarian.x] != 0):
                print(Back.MAGENTA+Fore.RED+Style.BRIGHT +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"BR")
            elif(king1.x == barbarian.x and king1.y == barbarian.y):
                if(takein == 'king'):
                    print(Back.BLUE+Fore.RED+Style.BRIGHT +
                          "\033[%s;%sH" % (king1.y, 2*king1.x)+"KI")
                else:
                    print(Back.RED+Fore.WHITE+Style.BRIGHT +
                          "\033[%s;%sH" % (king1.y, 2*king1.x)+"QU")
            elif(archer_cordinates[barbarian.y][barbarian.x] != 1):
                print(Back.LIGHTYELLOW_EX+Fore.RED+Style.BRIGHT +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"AR")
            elif(baloon_cordinates[barbarian.y][barbarian.x] != 0):
                print(Back.LIGHTWHITE_EX+Fore.BLUE+Style.BRIGHT +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"BL")
            else:
                print(Back.GREEN +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"  ")
            archer_cordinates[barbarian.y][barbarian.x] = archer_cordinates[barbarian.y][barbarian.x]-1
            barbarian.y = barbarian.y-1
            archer_cordinates[barbarian.y][barbarian.x] = archer_cordinates[barbarian.y][barbarian.x]+1
            if(king1.x != barbarian.x or king1.y != barbarian.y):
                print(Back.LIGHTYELLOW_EX+Fore.RED+Style.BRIGHT +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"AR")
    elif(input == 's' or input == 'S'):
        if(barbarian.y+1 > 40):
            return
        if(building_cordinates[barbarian.y+1][barbarian.x] == 0 or building_cordinates[barbarian.y+1][barbarian.x] < 0):
            if(barbarian_cordinates[barbarian.y][barbarian.x] != 0):
                print(Back.MAGENTA+Fore.RED+Style.BRIGHT +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"BR")
            elif(king1.x == barbarian.x and king1.y == barbarian.y):
                if(takein == 'king'):
                    print(Back.BLUE+Fore.RED+Style.BRIGHT +
                          "\033[%s;%sH" % (king1.y, 2*king1.x)+"KI")
                else:
                    print(Back.RED+Fore.WHITE+Style.BRIGHT +
                          "\033[%s;%sH" % (king1.y, 2*king1.x)+"QU")
            elif(archer_cordinates[barbarian.y][barbarian.x] != 1):
                print(Back.LIGHTYELLOW_EX+Fore.RED+Style.BRIGHT +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"AR")
            elif(baloon_cordinates[barbarian.y][barbarian.x] != 0):
                print(Back.LIGHTWHITE_EX+Fore.BLUE+Style.BRIGHT +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"BL")
            else:
                print(Back.GREEN +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"  ")
            archer_cordinates[barbarian.y][barbarian.x] = archer_cordinates[barbarian.y][barbarian.x]-1
            barbarian.y = barbarian.y+1
            archer_cordinates[barbarian.y][barbarian.x] = archer_cordinates[barbarian.y][barbarian.x]+1
            if(king1.x != barbarian.x or king1.y != barbarian.y):
                print(Back.LIGHTYELLOW_EX+Fore.RED+Style.BRIGHT +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"AR")
    elif(input == 'a' or input == 'A'):
        if(barbarian.x-1 <= 0):
            return
        if(building_cordinates[barbarian.y][barbarian.x-1] == 0 or building_cordinates[barbarian.y][barbarian.x-1] < 0):
            if(barbarian_cordinates[barbarian.y][barbarian.x] != 0):
                print(Back.MAGENTA+Fore.RED+Style.BRIGHT +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"BR")
            elif(king1.x == barbarian.x and king1.y == barbarian.y):
                if(takein == 'king'):
                    print(Back.BLUE+Fore.RED+Style.BRIGHT +
                          "\033[%s;%sH" % (king1.y, 2*king1.x)+"KI")
                else:
                    print(Back.RED+Fore.WHITE+Style.BRIGHT +
                          "\033[%s;%sH" % (king1.y, 2*king1.x)+"QU")
            elif(archer_cordinates[barbarian.y][barbarian.x] != 1):
                print(Back.LIGHTYELLOW_EX+Fore.RED+Style.BRIGHT +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"AR")
            elif(baloon_cordinates[barbarian.y][barbarian.x] != 0):
                print(Back.LIGHTWHITE_EX+Fore.BLUE+Style.BRIGHT +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"BL")
            else:
                print(Back.GREEN +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"  ")
            archer_cordinates[barbarian.y][barbarian.x] = archer_cordinates[barbarian.y][barbarian.x]-1
            barbarian.x = barbarian.x-1
            archer_cordinates[barbarian.y][barbarian.x] = archer_cordinates[barbarian.y][barbarian.x]+1
            if(king1.x != barbarian.x or king1.y != barbarian.y):
                print(Back.LIGHTYELLOW_EX+Fore.RED+Style.BRIGHT +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"AR")
    elif(input == 'd' or input == 'D'):
        if(barbarian.x+1 > 40):
            return
        if(building_cordinates[barbarian.y][barbarian.x+1] == 0 or building_cordinates[barbarian.y][barbarian.x+1] < 0):
            if(barbarian_cordinates[barbarian.y][barbarian.x] != 0):
                print(Back.MAGENTA+Fore.RED+Style.BRIGHT +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"BR")
            elif(king1.x == barbarian.x and king1.y == barbarian.y):
                if(takein == 'king'):
                    print(Back.BLUE+Fore.RED+Style.BRIGHT +
                          "\033[%s;%sH" % (king1.y, 2*king1.x)+"KI")
                else:
                    print(Back.RED+Fore.WHITE+Style.BRIGHT +
                          "\033[%s;%sH" % (king1.y, 2*king1.x)+"QU")
            elif(archer_cordinates[barbarian.y][barbarian.x] != 1):
                print(Back.LIGHTYELLOW_EX+Fore.RED+Style.BRIGHT +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"AR")
            elif(baloon_cordinates[barbarian.y][barbarian.x] != 0):
                print(Back.LIGHTWHITE_EX+Fore.BLUE+Style.BRIGHT +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"BL")
            else:
                print(Back.GREEN +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"  ")
            archer_cordinates[barbarian.y][barbarian.x] = archer_cordinates[barbarian.y][barbarian.x]-1
            barbarian.x = barbarian.x+1
            archer_cordinates[barbarian.y][barbarian.x] = archer_cordinates[barbarian.y][barbarian.x]+1
            if(king1.x != barbarian.x or king1.y != barbarian.y):
                print(Back.LIGHTYELLOW_EX+Fore.RED+Style.BRIGHT +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"AR")
    elif(input == " "):

        if(building_cordinates[barbarian.y][barbarian.x+1] >= 1000 and building_cordinates[barbarian.y][barbarian.x+1] < 10000):
            if(building_cordinates[barbarian.y][barbarian.x+1] == 1000):
                print(Back.GREEN +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x+2)+"  ")
                building_cordinates[barbarian.y][barbarian.x+1] = 0
            else:
                building_cordinates[barbarian.y][barbarian.x +
                                                 1] = building_cordinates[barbarian.y][barbarian.x+1]-1
        elif(building_cordinates[barbarian.y+1][barbarian.x] >= 1000 and building_cordinates[barbarian.y+1][barbarian.x] < 10000):
            if(building_cordinates[barbarian.y+1][barbarian.x] == 1000):
                print(Back.GREEN +
                      "\033[%s;%sH" % (barbarian.y+1, 2*barbarian.x)+"  ")
                building_cordinates[barbarian.y+1][barbarian.x] = 0
            else:
                building_cordinates[barbarian.y +
                                    1][barbarian.x] = building_cordinates[barbarian.y+1][barbarian.x]-1
        elif(building_cordinates[barbarian.y-1][barbarian.x] >= 1000 and building_cordinates[barbarian.y-1][barbarian.x] < 10000):
            if(building_cordinates[barbarian.y-1][barbarian.x] == 1000):
                print(Back.GREEN +
                      "\033[%s;%sH" % (barbarian.y-1, 2*barbarian.x)+"  ")
                building_cordinates[barbarian.y-1][barbarian.x] = 0
            else:
                building_cordinates[barbarian.y -
                                    1][barbarian.x] = building_cordinates[barbarian.y-1][barbarian.x]-1
        elif(building_cordinates[barbarian.y][barbarian.x-1] >= 1000 and building_cordinates[barbarian.y][barbarian.x-1] < 10000):
            if(building_cordinates[barbarian.y][barbarian.x-1] == 1000):
                print(Back.GREEN +
                      "\033[%s;%sH" % (barbarian.y, 2*barbarian.x-2)+"  ")
                building_cordinates[barbarian.y][barbarian.x-1] = 0
            else:
                building_cordinates[barbarian.y][barbarian.x -
                                                 1] = building_cordinates[barbarian.y][barbarian.x-1]-1


def controlbaloon(input, building_cordinates, barbarian, huts, townhall1, barbarian_cordinates, archer_cordinates, baloon_cordinates, canons, king1, wizards, takein):
    if(input == 'w' or input == 'W'):
        if(barbarian.y-1 <= 0):
            return

        if(barbarian_cordinates[barbarian.y][barbarian.x] != 0):
            print(Back.MAGENTA+Fore.RED+Style.BRIGHT +
                  "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"BR")
        elif(king1.x == barbarian.x and king1.y == barbarian.y):
            if(takein == 'king'):
                print(Back.BLUE+Fore.RED+Style.BRIGHT +
                      "\033[%s;%sH" % (king1.y, 2*king1.x)+"KI")
            else:
                print(Back.RED+Fore.WHITE+Style.BRIGHT +
                      "\033[%s;%sH" % (king1.y, 2*king1.x)+"QU")
        elif(archer_cordinates[barbarian.y][barbarian.x] != 0):
            print(Back.LIGHTYELLOW_EX+Fore.RED+Style.BRIGHT +
                  "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"AR")
        elif(baloon_cordinates[barbarian.y][barbarian.x] != 1):
            print(Back.LIGHTWHITE_EX+Fore.BLUE+Style.BRIGHT +
                  "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"BL")
        elif(building_cordinates[barbarian.y][barbarian.x] > 0):
            if(building_cordinates[barbarian.y][barbarian.x] > 0 and building_cordinates[barbarian.y][barbarian.x] < 100):
                huts[building_cordinates[barbarian.y][barbarian.x] -
                     1].change_health(0, building_cordinates)
            elif(building_cordinates[barbarian.y][barbarian.x] == 101):
                townhall1.change_health(0, building_cordinates)
            elif(building_cordinates[barbarian.y][barbarian.x] >= 10000 and building_cordinates[barbarian.y][barbarian.x] < 100000):
                canons[building_cordinates[barbarian.y][barbarian.x] -
                       10001].change_health(0, building_cordinates)
            elif(building_cordinates[barbarian.y][barbarian.x] >= 100000):
                wizards[building_cordinates[barbarian.y][barbarian.x] -
                        100001].change_health(0, building_cordinates)
            elif(building_cordinates[barbarian.y][barbarian.x] > 1000):
                print(Back.BLACK+"\033[%s;%sH" %
                      (barbarian.y, 2*barbarian.x)+"  ")

        else:
            print(Back.GREEN +
                  "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"  ")
        baloon_cordinates[barbarian.y][barbarian.x] = baloon_cordinates[barbarian.y][barbarian.x]-1
        barbarian.y = barbarian.y-1
        baloon_cordinates[barbarian.y][barbarian.x] = baloon_cordinates[barbarian.y][barbarian.x]+1
        if(king1.x != barbarian.x or king1.y != barbarian.y):
            print(Back.LIGHTWHITE_EX+Fore.BLUE+Style.BRIGHT +
                  "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"BL")
    elif(input == 's' or input == 'S'):
        if(barbarian.y+1 > 40):
            return

        if(barbarian_cordinates[barbarian.y][barbarian.x] != 0):
            print(Back.MAGENTA+Fore.RED+Style.BRIGHT +
                  "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"BR")
        elif(king1.x == barbarian.x and king1.y == barbarian.y):
            if(takein == 'king'):
                print(Back.BLUE+Fore.RED+Style.BRIGHT +
                      "\033[%s;%sH" % (king1.y, 2*king1.x)+"KI")
            else:
                print(Back.RED+Fore.WHITE+Style.BRIGHT +
                      "\033[%s;%sH" % (king1.y, 2*king1.x)+"QU")
        elif(archer_cordinates[barbarian.y][barbarian.x] != 0):
            print(Back.LIGHTYELLOW_EX+Fore.RED+Style.BRIGHT +
                  "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"AR")
        elif(baloon_cordinates[barbarian.y][barbarian.x] != 1):
            print(Back.LIGHTWHITE_EX+Fore.BLUE+Style.BRIGHT +
                  "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"BL")
        elif(building_cordinates[barbarian.y][barbarian.x] > 0):
            if(building_cordinates[barbarian.y][barbarian.x] > 0 and building_cordinates[barbarian.y][barbarian.x] < 100):
                huts[building_cordinates[barbarian.y][barbarian.x] -
                     1].change_health(0, building_cordinates)
            elif(building_cordinates[barbarian.y][barbarian.x] == 101):
                townhall1.change_health(0, building_cordinates)
            elif(building_cordinates[barbarian.y][barbarian.x] >= 10000 and building_cordinates[barbarian.y][barbarian.x] < 100000):
                canons[building_cordinates[barbarian.y][barbarian.x] -
                       10001].change_health(0, building_cordinates)
            elif(building_cordinates[barbarian.y][barbarian.x] >= 100000):
                wizards[building_cordinates[barbarian.y][barbarian.x] -
                        100001].change_health(0, building_cordinates)
            elif(building_cordinates[barbarian.y][barbarian.x] > 1000):
                print(Back.BLACK+"\033[%s;%sH" %
                      (barbarian.y, 2*barbarian.x)+"  ")
        else:
            print(Back.GREEN +
                  "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"  ")
        baloon_cordinates[barbarian.y][barbarian.x] = baloon_cordinates[barbarian.y][barbarian.x]-1
        barbarian.y = barbarian.y+1
        baloon_cordinates[barbarian.y][barbarian.x] = baloon_cordinates[barbarian.y][barbarian.x]+1
        if(king1.x != barbarian.x or king1.y != barbarian.y):
            print(Back.LIGHTWHITE_EX+Fore.BLUE+Style.BRIGHT +
                  "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"BL")
    elif(input == 'a' or input == 'A'):
        if(barbarian.x-1 <= 0):
            return

        if(barbarian_cordinates[barbarian.y][barbarian.x] != 0):
            print(Back.MAGENTA+Fore.RED+Style.BRIGHT +
                  "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"BR")
        elif(king1.x == barbarian.x and king1.y == barbarian.y):
            if(takein == 'king'):
                print(Back.BLUE+Fore.RED+Style.BRIGHT +
                      "\033[%s;%sH" % (king1.y, 2*king1.x)+"KI")
            else:
                print(Back.RED+Fore.WHITE+Style.BRIGHT +
                      "\033[%s;%sH" % (king1.y, 2*king1.x)+"QU")
        elif(archer_cordinates[barbarian.y][barbarian.x] != 0):
            print(Back.LIGHTYELLOW_EX+Fore.RED+Style.BRIGHT +
                  "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"AR")
        elif(baloon_cordinates[barbarian.y][barbarian.x] != 1):
            print(Back.LIGHTWHITE_EX+Fore.BLUE+Style.BRIGHT +
                  "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"BL")
        elif(building_cordinates[barbarian.y][barbarian.x] > 0):
            if(building_cordinates[barbarian.y][barbarian.x] > 0 and building_cordinates[barbarian.y][barbarian.x] < 100):
                huts[building_cordinates[barbarian.y][barbarian.x] -
                     1].change_health(0, building_cordinates)
            elif(building_cordinates[barbarian.y][barbarian.x] == 101):
                townhall1.change_health(0, building_cordinates)
            elif(building_cordinates[barbarian.y][barbarian.x] >= 10000 and building_cordinates[barbarian.y][barbarian.x] < 100000):
                canons[building_cordinates[barbarian.y][barbarian.x] -
                       10001].change_health(0, building_cordinates)
            elif(building_cordinates[barbarian.y][barbarian.x] >= 100000):
                wizards[building_cordinates[barbarian.y][barbarian.x] -
                        100001].change_health(0, building_cordinates)
            elif(building_cordinates[barbarian.y][barbarian.x] > 1000):
                print(Back.BLACK+"\033[%s;%sH" %
                      (barbarian.y, 2*barbarian.x)+"  ")
        else:
            print(Back.GREEN +
                  "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"  ")
        baloon_cordinates[barbarian.y][barbarian.x] = baloon_cordinates[barbarian.y][barbarian.x]-1
        barbarian.x = barbarian.x-1
        baloon_cordinates[barbarian.y][barbarian.x] = baloon_cordinates[barbarian.y][barbarian.x]+1
        if(king1.x != barbarian.x or king1.y != barbarian.y):
            print(Back.LIGHTWHITE_EX+Fore.BLUE+Style.BRIGHT +
                  "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"BL")
    elif(input == 'd' or input == 'D'):
        if(barbarian.x+1 > 40):
            return

        if(barbarian_cordinates[barbarian.y][barbarian.x] != 0):
            print(Back.MAGENTA+Fore.RED+Style.BRIGHT +
                  "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"BR")
        elif(king1.x == barbarian.x and king1.y == barbarian.y):
            if(takein == 'king'):
                print(Back.BLUE+Fore.RED+Style.BRIGHT +
                      "\033[%s;%sH" % (king1.y, 2*king1.x)+"KI")
            else:
                print(Back.RED+Fore.WHITE+Style.BRIGHT +
                      "\033[%s;%sH" % (king1.y, 2*king1.x)+"QU")
        elif(archer_cordinates[barbarian.y][barbarian.x] != 0):
            print(Back.LIGHTYELLOW_EX+Fore.RED+Style.BRIGHT +
                  "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"AR")
        elif(baloon_cordinates[barbarian.y][barbarian.x] != 1):
            print(Back.LIGHTWHITE_EX+Fore.BLUE+Style.BRIGHT +
                  "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"BL")
        elif(building_cordinates[barbarian.y][barbarian.x] > 0):
            if(building_cordinates[barbarian.y][barbarian.x] > 0 and building_cordinates[barbarian.y][barbarian.x] < 100):
                huts[building_cordinates[barbarian.y][barbarian.x] -
                     1].change_health(0, building_cordinates)
            elif(building_cordinates[barbarian.y][barbarian.x] == 101):
                townhall1.change_health(0, building_cordinates)
            elif(building_cordinates[barbarian.y][barbarian.x] >= 10000 and building_cordinates[barbarian.y][barbarian.x] < 100000):
                canons[building_cordinates[barbarian.y][barbarian.x] -
                       10001].change_health(0, building_cordinates)
            elif(building_cordinates[barbarian.y][barbarian.x] >= 100000):
                wizards[building_cordinates[barbarian.y][barbarian.x] -
                        100001].change_health(0, building_cordinates)
            elif(building_cordinates[barbarian.y][barbarian.x] > 1000):
                print(Back.BLACK+"\033[%s;%sH" %
                      (barbarian.y, 2*barbarian.x)+"  ")
        else:
            print(Back.GREEN +
                  "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"  ")
        baloon_cordinates[barbarian.y][barbarian.x] = baloon_cordinates[barbarian.y][barbarian.x]-1
        barbarian.x = barbarian.x+1
        baloon_cordinates[barbarian.y][barbarian.x] = baloon_cordinates[barbarian.y][barbarian.x]+1
        if(king1.x != barbarian.x or king1.y != barbarian.y):
            print(Back.LIGHTWHITE_EX+Fore.BLUE+Style.BRIGHT +
                  "\033[%s;%sH" % (barbarian.y, 2*barbarian.x)+"BL")


def controlqueen(input, building_cordinates, king1, huts, townhall1, barbarian_cordinates, archer_cordinates, baloon_cordinates, canons, wizards, prevstep, queendamage):
    if(input == 'w' or input == 'W'):
        if(king1.y-1 <= 0):
            return
        if(building_cordinates[king1.y-1][king1.x] == 0 or building_cordinates[king1.y-1][king1.x] < 0):
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
            king1.y = king1.y-1
            print(Back.RED+Fore.WHITE+Style.BRIGHT +
                  "\033[%s;%sH" % (king1.y, 2*king1.x)+"QU")
    elif(input == 's' or input == 'S'):
        if(king1.y+1 > 40):
            return
        if(building_cordinates[king1.y+1][king1.x] == 0 or building_cordinates[king1.y+1][king1.x] < 0):
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
            king1.y = king1.y+1
            print(Back.RED+Fore.WHITE+Style.BRIGHT +
                  "\033[%s;%sH" % (king1.y, 2*king1.x)+"QU")
    elif(input == 'a' or input == 'A'):
        if(king1.x-1 <= 0):
            return
        if(building_cordinates[king1.y][king1.x-1] == 0 or building_cordinates[king1.y][king1.x-1] < 0):
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
            king1.x = king1.x-1
            print(Back.RED+Fore.WHITE+Style.BRIGHT +
                  "\033[%s;%sH" % (king1.y, 2*king1.x)+"QU")
    elif(input == 'd' or input == 'D'):
        if(king1.x+1 > 40):
            return
        if(building_cordinates[king1.y][king1.x+1] == 0 or building_cordinates[king1.y][king1.x+1] < 0):
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
            king1.x = king1.x+1
            print(Back.RED+Fore.WHITE+Style.BRIGHT +
                  "\033[%s;%sH" % (king1.y, 2*king1.x)+"QU")
    elif(input == " "):
        s = {0}
        s.remove(0)
        if(prevstep == 'w' or prevstep == 'W'):
            xk = king1.x-2
            yk = king1.y-2-8
        elif(prevstep == 's' or prevstep == 'S'):
            xk = king1.x-2
            yk = king1.y-2+8
        elif(prevstep == 'a' or prevstep == 'A'):
            xk = king1.x-2-8
            yk = king1.y-2
        elif(prevstep == 'd' or prevstep == 'D'):
            xk = king1.x-2+8
            yk = king1.y-2

        for i in range(5):
            for j in range(5):
                if(xk+i > 0 and xk+i < 40 and yk+j > 0 and yk+j < 40):
                    s.add(building_cordinates[yk+j][xk+i])
                    if(building_cordinates[yk+j][xk+i] >= 1000 and building_cordinates[yk+j][xk+i] < 10000):
                        if(building_cordinates[yk+j][xk+i] == 1000):
                            print(Back.GREEN +
                                  "\033[%s;%sH" % (yk+j, 2*(xk+i))+"  ")
                            building_cordinates[yk+j][xk+i] = 0
                        else:
                            building_cordinates[yk+j][xk +
                                                      i] = building_cordinates[yk+j][xk+i]-1
        for i in s:
            if(i > 0):

                if(i > 0 and i < 100):
                    huts[i -
                         1].change_health(queendamage, building_cordinates)
                elif(i == 101):
                    townhall1.change_health(queendamage, building_cordinates)
                elif(i > 10000 and i < 100000):
                    canons[i -
                           10001].change_health(queendamage, building_cordinates)
                elif(i > 100000):
                    wizards[i -
                            100001].change_health(queendamage, building_cordinates)
    elif(input == "x"):
        s = {0}
        s.remove(0)
        if(prevstep == 'w' or prevstep == 'W'):
            xk = king1.x-4
            yk = king1.y-4-16
        elif(prevstep == 's' or prevstep == 'S'):
            xk = king1.x-4
            yk = king1.y-4+16
        elif(prevstep == 'a' or prevstep == 'A'):
            xk = king1.x-4-16
            yk = king1.y-4
        elif(prevstep == 'd' or prevstep == 'D'):
            xk = king1.x-4+16
            yk = king1.y-4

        for i in range(9):
            for j in range(9):
                if(xk+i > 0 and xk+i < 40 and yk+j > 0 and yk+j < 40):
                    s.add(building_cordinates[yk+j][xk+i])
                    if(building_cordinates[yk+j][xk+i] >= 1000 and building_cordinates[yk+j][xk+i] < 10000):
                        if(building_cordinates[yk+j][xk+i] == 1000):
                            print(Back.GREEN +
                                  "\033[%s;%sH" % (yk+j, 2*(xk+i))+"  ")
                            building_cordinates[yk+j][xk+i] = 0
                        else:
                            building_cordinates[yk+j][xk +
                                                      i] = building_cordinates[yk+j][xk+i]-1
        for i in s:
            if(i > 0):

                if(i > 0 and i < 100):
                    huts[i -
                         1].change_health(queendamage, building_cordinates)
                elif(i == 101):
                    townhall1.change_health(queendamage, building_cordinates)
                elif(i > 10000 and i < 100000):
                    canons[i -
                           10001].change_health(queendamage, building_cordinates)
                elif(i > 100000):
                    wizards[i -
                            100001].change_health(queendamage, building_cordinates)


def settarget(buildings, barbarian):
    min1 = 10000
    for i in range(len(buildings)):
        if(min1 > abs(buildings[i].x-barbarian.x)+abs(buildings[i].y-barbarian.y)):
            min1 = abs(buildings[i].x-barbarian.x) + \
                abs(buildings[i].y-barbarian.y)
            barbarian.target = buildings[i]
