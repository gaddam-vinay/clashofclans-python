from re import L
from string import *
from click import style
from colorama import *
from pyrsistent import b


class building:
    def __init__(self, health, x, y):
        self.health = health
        self.x = x
        self.y = y
        self.dead = 0


class hut(building):
    hutno = 0
    maxhealth = 0

    def __init__(self, health, x, y, building_cordinates):
        super().__init__(health, x, y)
        hut.hutno = hut.hutno+1
        self.num = hut.hutno
        hut.maxhealth = health
        print(Back.BLACK+"\033[%s;%sH" % (y, 2*x)+"  ")
        building_cordinates[y][x] = self.num
        building_cordinates[y-1][x] = -self.num
        building_cordinates[y][x-1] = -self.num
        print(Back.BLACK+"\033[%s;%sH" % (y+1, 2*x+2)+"  ")
        building_cordinates[y+1][x+1] = self.num
        building_cordinates[y+2][x+1] = -self.num
        building_cordinates[y+1][x+2] = -self.num
        print(Back.BLACK+"\033[%s;%sH" % (y+1, 2*x)+"  ")
        building_cordinates[y+1][x] = self.num
        building_cordinates[y+2][x] = -self.num
        building_cordinates[y+1][x-1] = -self.num
        print(Back.BLACK+"\033[%s;%sH" % (y, 2*x+2)+"  ")
        building_cordinates[y][x+1] = self.num
        building_cordinates[y][x+2] = -self.num
        building_cordinates[y-1][x+1] = -self.num

    def change_health(self, damage, building_cordinates):
        self.health = self.health-damage
        if(self.health < 0):
            self.dead = 1
            print(Back.GREEN+"\033[%s;%sH" % (self.y, 2*self.x)+"  ")
            building_cordinates[self.y][self.x] = 0
            building_cordinates[self.y-1][self.x] = 0
            building_cordinates[self.y][self.x-1] = 0
            print(Back.GREEN+"\033[%s;%sH" % (self.y+1, 2*self.x+2)+"  ")
            building_cordinates[self.y+1][self.x+1] = 0
            building_cordinates[self.y+2][self.x] = 0
            building_cordinates[self.y][self.x+2] = 0
            print(Back.GREEN+"\033[%s;%sH" % (self.y+1, 2*self.x)+"  ")
            building_cordinates[self.y+1][self.x] = 0
            building_cordinates[self.y+2][self.x] = 0
            building_cordinates[self.y][self.x-1] = 0
            print(Back.GREEN+"\033[%s;%sH" % (self.y, 2*self.x+2)+"  ")
            building_cordinates[self.y][self.x+1] = 0
            building_cordinates[self.y][self.x+2] = 0
            building_cordinates[self.y-1][self.x] = 0
        elif(self.health <= hut.maxhealth/2 and self.health > hut.maxhealth/5):
            print(Back.RED+"\033[%s;%sH" % (self.y, 2*self.x)+"  ")
            print(Back.RED+"\033[%s;%sH" % (self.y, 2*self.x+2)+"  ")
            print(Back.RED+"\033[%s;%sH" % (self.y+1, 2*self.x)+"  ")
            print(Back.RED+"\033[%s;%sH" % (self.y+1, 2*self.x+2)+"  ")
        elif(self.health <= hut.maxhealth/5):
            print(Back.CYAN+"\033[%s;%sH" % (self.y, 2*self.x)+"  ")
            print(Back.CYAN+"\033[%s;%sH" % (self.y, 2*self.x+2)+"  ")
            print(Back.CYAN+"\033[%s;%sH" % (self.y+1, 2*self.x)+"  ")
            print(Back.CYAN+"\033[%s;%sH" % (self.y+1, 2*self.x+2)+"  ")
        else:
            print(Back.BLACK+"\033[%s;%sH" % (self.y, 2*self.x)+"  ")
            print(Back.BLACK+"\033[%s;%sH" % (self.y, 2*self.x+2)+"  ")
            print(Back.BLACK+"\033[%s;%sH" % (self.y+1, 2*self.x)+"  ")
            print(Back.BLACK+"\033[%s;%sH" % (self.y+1, 2*self.x+2)+"  ")


class townhall(building):
    maxhealth = 0

    def __init__(self, health, x, y, building_cordinates):
        townhall.maxhealth = health
        super().__init__(health, x, y)
        for i in range(3):
            for j in range(4):
                print(Back.BLACK+"\033[%s;%sH" % (y+i, 2*x+2*j)+"  ")
                building_cordinates[y+i][x+j] = 101
                if(i == 0):
                    building_cordinates[y+i-1][x+j] = -101
                if(i == 2):
                    building_cordinates[y+i+1][x+j] = -101
                if(j == 0):
                    building_cordinates[y+i][x+j-1] = -101
                if(j == 3):
                    building_cordinates[y+i][x+j+1] = -101

    def change_health(self, damage, building_cordinates):
        self.health = self.health-damage
        if(self.health < 0):
            self.dead = 1
            for i in range(3):
                for j in range(4):
                    print(Back.GREEN+"\033[%s;%sH" %
                          (self.y+i, 2*self.x+2*j)+"  ")
                    building_cordinates[self.y+i][self.x+j] = 0
                    if(i == 0):
                        building_cordinates[self.y+i-1][self.x+j] = 0
                    if(i == 2):
                        building_cordinates[self.y+i+1][self.x+j] = 0
                    if(j == 0):
                        building_cordinates[self.y+i][self.x+j-1] = 0
                    if(j == 3):
                        building_cordinates[self.y+i][self.x+j+1] = 0

        elif(self.health <= townhall.maxhealth/2 and self.health > townhall.maxhealth/5):
            for i in range(3):
                for j in range(4):
                    print(Back.RED+"\033[%s;%sH" %
                          (self.y+i, 2*self.x+2*j)+"  ")
        elif(self.health <= townhall.maxhealth/5):
            for i in range(3):
                for j in range(4):
                    print(Back.CYAN+"\033[%s;%sH" %
                          (self.y+i, 2*self.x+2*j)+"  ")
        else:
            for i in range(3):
                for j in range(4):
                    print(Back.BLACK+"\033[%s;%sH" %
                          (self.y+i, 2*self.x+2*j)+"  ")


class canon(building):
    canonno = 10000
    maxhealth = 0

    def __init__(self, health, x, y, building_cordinates):
        super().__init__(health, x, y)
        canon.canonno = canon.canonno+1
        self.num = canon.canonno
        canon.maxhealth = health
        print(Back.LIGHTBLACK_EX+Fore.RED +
              Style.BRIGHT+"\033[%s;%sH" % (y, 2*x)+"cc")
        building_cordinates[y][x] = self.num
        building_cordinates[y-1][x] = -self.num
        building_cordinates[y][x-1] = -self.num
        building_cordinates[y][x+1] = -self.num
        print(Back.LIGHTBLACK_EX+Fore.RED +
              Style.BRIGHT+"\033[%s;%sH" % (y+1, 2*x)+"cc")
        building_cordinates[y+1][x] = self.num
        building_cordinates[y+2][x] = -self.num
        building_cordinates[y+1][x-1] = -self.num
        building_cordinates[y+1][x+1] = -self.num

    def change_health(self, damage, building_cordinates):
        self.health = self.health-damage
        if(self.health < 0):
            self.dead = 1
            print(Back.GREEN+"\033[%s;%sH" % (self.y, 2*self.x)+"  ")
            building_cordinates[self.y][self.x] = 0
            building_cordinates[self.y-1][self.x] = 0
            building_cordinates[self.y][self.x-1] = 0
            building_cordinates[self.y][self.x+1] = 0
            print(Back.GREEN+"\033[%s;%sH" % (self.y+1, 2*self.x)+"  ")
            building_cordinates[self.y+1][self.x] = 0
            building_cordinates[self.y+2][self.x] = 0
            building_cordinates[self.y+1][self.x-1] = 0
            building_cordinates[self.y+1][self.x+1] = 0
        elif(self.health <= canon.maxhealth and self.health > canon.maxhealth/2):
            print(Back.LIGHTBLACK_EX+Fore.RED +
                  Style.BRIGHT+"\033[%s;%sH" % (self.y, 2*self.x)+"cc")
            print(Back.LIGHTBLACK_EX+Fore.RED +
                  Style.BRIGHT+"\033[%s;%sH" % (self.y+1, 2*self.x)+"cc")
        elif(self.health <= canon.maxhealth/2 and self.health > canon.maxhealth/5):
            print(Back.LIGHTRED_EX+Fore.RED+Style.BRIGHT +
                  "\033[%s;%sH" % (self.y, 2*self.x)+"cc")
            print(Back.LIGHTRED_EX+Fore.RED+Style.BRIGHT +
                  "\033[%s;%sH" % (self.y+1, 2*self.x)+"cc")
        elif(self.health <= canon.maxhealth/5):
            print(Back.LIGHTCYAN_EX+Fore.RED+Style.BRIGHT +
                  "\033[%s;%sH" % (self.y, 2*self.x)+"cc")
            print(Back.LIGHTCYAN_EX+Fore.RED+Style.BRIGHT +
                  "\033[%s;%sH" % (self.y+1, 2*self.x)+"cc")

    def attackcolor(self):
        if(self.health <= canon.maxhealth and self.health > canon.maxhealth/2):
            print(Back.LIGHTBLACK_EX+Fore.YELLOW +
                  Style.BRIGHT+"\033[%s;%sH" % (self.y, 2*self.x)+"cc")
            print(Back.LIGHTBLACK_EX+Fore.YELLOW +
                  Style.BRIGHT+"\033[%s;%sH" % (self.y+1, 2*self.x)+"cc")
        elif(self.health <= canon.maxhealth/2 and self.health > canon.maxhealth/5):
            print(Back.LIGHTRED_EX+Fore.YELLOW+Style.BRIGHT +
                  "\033[%s;%sH" % (self.y, 2*self.x)+"cc")
            print(Back.LIGHTRED_EX+Fore.YELLOW+Style.BRIGHT +
                  "\033[%s;%sH" % (self.y+1, 2*self.x)+"cc")
        elif(self.health <= canon.maxhealth/5):
            print(Back.LIGHTCYAN_EX+Fore.YELLOW+Style.BRIGHT +
                  "\033[%s;%sH" % (self.y, 2*self.x)+"cc")
            print(Back.LIGHTCYAN_EX+Fore.YELLOW+Style.BRIGHT +
                  "\033[%s;%sH" % (self.y+1, 2*self.x)+"cc")


class wizard(building):
    wizardno = 100000
    maxhealth = 0

    def __init__(self, health, x, y, building_cordinates):
        super().__init__(health, x, y)
        wizard.wizardno = wizard.wizardno+1
        self.num = wizard.wizardno
        wizard.maxhealth = health
        print(Back.LIGHTBLUE_EX+Fore.RED +
              Style.BRIGHT+"\033[%s;%sH" % (y, 2*x)+"WW")
        building_cordinates[y][x] = self.num
        building_cordinates[y-1][x] = -self.num
        building_cordinates[y][x-1] = -self.num
        print(Back.LIGHTBLUE_EX+Fore.RED +
              Style.BRIGHT+"\033[%s;%sH" % (y+1, 2*x)+"WW")
        building_cordinates[y+1][x] = self.num
        building_cordinates[y+2][x] = -self.num
        building_cordinates[y+1][x-1] = -self.num
        print(Back.LIGHTBLUE_EX+Fore.RED +
              Style.BRIGHT+"\033[%s;%sH" % (y+1, 2*x+2)+"WW")
        building_cordinates[y+1][x+1] = self.num
        building_cordinates[y+2][x+1] = -self.num
        building_cordinates[y+1][x+2] = -self.num
        print(Back.LIGHTBLUE_EX+Fore.RED +
              Style.BRIGHT+"\033[%s;%sH" % (y, 2*x+2)+"WW")
        building_cordinates[y][x+1] = self.num
        building_cordinates[y-1][x+1] = -self.num
        building_cordinates[y][x+2] = -self.num

    def change_health(self, damage, building_cordinates):
        self.health = self.health-damage
        if(self.health < 0):
            self.dead = 1
            print(Back.GREEN+"\033[%s;%sH" % (self.y, 2*self.x)+"  ")
            building_cordinates[self.y][self.x] = 0
            building_cordinates[self.y-1][self.x] = 0
            building_cordinates[self.y][self.x-1] = 0
            print(Back.GREEN+"\033[%s;%sH" % (self.y+1, 2*self.x)+"  ")
            building_cordinates[self.y+1][self.x] = 0
            building_cordinates[self.y+2][self.x] = 0
            building_cordinates[self.y+1][self.x-1] = 0
            print(Back.GREEN+"\033[%s;%sH" % (self.y+1, 2*self.x+2)+"  ")
            building_cordinates[self.y+1][self.x+1] = 0
            building_cordinates[self.y+2][self.x+1] = 0
            building_cordinates[self.y+1][self.x+2] = 0
            print(Back.GREEN+"\033[%s;%sH" % (self.y, 2*self.x+2)+"  ")
            building_cordinates[self.y][self.x+1] = 0
            building_cordinates[self.y-1][self.x+1] = 0
            building_cordinates[self.y][self.x+2] = 0
        elif(self.health <= wizard.maxhealth and self.health > wizard.maxhealth/2):
            print(Back.LIGHTBLUE_EX+Fore.RED +
                  Style.BRIGHT+"\033[%s;%sH" % (self.y, 2*self.x)+"WW")
            print(Back.LIGHTBLUE_EX+Fore.RED +
                  Style.BRIGHT+"\033[%s;%sH" % (self.y+1, 2*self.x)+"WW")
            print(Back.LIGHTBLUE_EX+Fore.RED +
                  Style.BRIGHT+"\033[%s;%sH" % (self.y+1, 2*self.x+2)+"WW")
            print(Back.LIGHTBLUE_EX+Fore.RED +
                  Style.BRIGHT+"\033[%s;%sH" % (self.y, 2*self.x+2)+"WW")
        elif(self.health <= wizard.maxhealth/2 and self.health > wizard.maxhealth/5):
            print(Back.LIGHTRED_EX+Fore.RED +
                  Style.BRIGHT+"\033[%s;%sH" % (self.y, 2*self.x)+"WW")
            print(Back.LIGHTRED_EX+Fore.RED +
                  Style.BRIGHT+"\033[%s;%sH" % (self.y+1, 2*self.x)+"WW")
            print(Back.LIGHTRED_EX+Fore.RED +
                  Style.BRIGHT+"\033[%s;%sH" % (self.y+1, 2*self.x+2)+"WW")
            print(Back.LIGHTRED_EX+Fore.RED +
                  Style.BRIGHT+"\033[%s;%sH" % (self.y, 2*self.x+2)+"WW")
        elif(self.health <= wizard.maxhealth/5):
            print(Back.LIGHTCYAN_EX+Fore.RED +
                  Style.BRIGHT+"\033[%s;%sH" % (self.y, 2*self.x)+"WW")
            print(Back.LIGHTCYAN_EX+Fore.RED +
                  Style.BRIGHT+"\033[%s;%sH" % (self.y+1, 2*self.x)+"WW")
            print(Back.LIGHTCYAN_EX+Fore.RED +
                  Style.BRIGHT+"\033[%s;%sH" % (self.y+1, 2*self.x+2)+"WW")
            print(Back.LIGHTCYAN_EX+Fore.RED +
                  Style.BRIGHT+"\033[%s;%sH" % (self.y, 2*self.x+2)+"WW")

    def attackcolor(self):
        if(self.health <= wizard.maxhealth and self.health > wizard.maxhealth/2):
            print(Back.LIGHTBLUE_EX+Fore.LIGHTWHITE_EX +
                  Style.BRIGHT+"\033[%s;%sH" % (self.y, 2*self.x)+"WW")
            print(Back.LIGHTBLUE_EX+Fore.LIGHTWHITE_EX +
                  Style.BRIGHT+"\033[%s;%sH" % (self.y+1, 2*self.x)+"WW")
            print(Back.LIGHTBLUE_EX+Fore.LIGHTWHITE_EX +
                  Style.BRIGHT+"\033[%s;%sH" % (self.y+1, 2*self.x+2)+"WW")
            print(Back.LIGHTBLUE_EX+Fore.LIGHTWHITE_EX +
                  Style.BRIGHT+"\033[%s;%sH" % (self.y, 2*self.x+2)+"WW")
        elif(self.health <= wizard.maxhealth/2 and self.health > wizard.maxhealth/5):
            print(Back.LIGHTRED_EX+Fore.LIGHTWHITE_EX +
                  Style.BRIGHT+"\033[%s;%sH" % (self.y, 2*self.x)+"WW")
            print(Back.LIGHTRED_EX+Fore.LIGHTWHITE_EX +
                  Style.BRIGHT+"\033[%s;%sH" % (self.y+1, 2*self.x)+"WW")
            print(Back.LIGHTRED_EX+Fore.LIGHTWHITE_EX +
                  Style.BRIGHT+"\033[%s;%sH" % (self.y+1, 2*self.x+2)+"WW")
            print(Back.LIGHTRED_EX+Fore.LIGHTWHITE_EX +
                  Style.BRIGHT+"\033[%s;%sH" % (self.y, 2*self.x+2)+"WW")
        elif(self.health <= wizard.maxhealth/5):
            print(Back.LIGHTCYAN_EX+Fore.LIGHTWHITE_EX +
                  Style.BRIGHT+"\033[%s;%sH" % (self.y, 2*self.x)+"WW")
            print(Back.LIGHTCYAN_EX+Fore.LIGHTWHITE_EX +
                  Style.BRIGHT+"\033[%s;%sH" % (self.y+1, 2*self.x)+"WW")
            print(Back.LIGHTCYAN_EX+Fore.LIGHTWHITE_EX +
                  Style.BRIGHT+"\033[%s;%sH" % (self.y+1, 2*self.x+2)+"WW")
            print(Back.LIGHTCYAN_EX+Fore.LIGHTWHITE_EX +
                  Style.BRIGHT+"\033[%s;%sH" % (self.y, 2*self.x+2)+"WW")


class barbarian:
    maxhealth = 0

    def __init__(self, x1, y1, health):
        self.y = y1
        self.x = x1
        barbarian.maxhealth = health
        self.health = health
        self.target = 0
        print(Back.MAGENTA+Fore.RED+Style.BRIGHT +
              "\033[%s;%sH" % (y1, 2*x1)+"BR")
        self.dead = 0

    def change_health(self, damage):
        self.health = self.health-damage
        if(self.health < 0):
            self.dead = 1

    def increase_health(self):
        if((3/2)*(self.health) > barbarian.maxhealth):
            self.health = barbarian.maxhealth
        else:
            self.health = self.health*(3/2)


class archer:
    maxhealth = 0

    def __init__(self, x1, y1, health):
        self.y = y1
        self.x = x1
        archer.maxhealth = health
        self.health = health
        self.target = 0
        print(Back.LIGHTYELLOW_EX+Fore.RED+Style.BRIGHT +
              "\033[%s;%sH" % (y1, 2*x1)+"AR")
        self.dead = 0

    def change_health(self, damage):
        self.health = self.health-damage
        if(self.health < 0):
            self.dead = 1

    def increase_health(self):
        if((3/2)*(self.health) > archer.maxhealth):
            self.health = archer.maxhealth
        else:
            self.health = self.health*(3/2)


class baloon:
    maxhealth = 0

    def __init__(self, x1, y1, health):
        self.y = y1
        self.x = x1
        baloon.maxhealth = health
        self.health = health
        self.target = 0
        print(Back.WHITE+Fore.BLUE+Style.BRIGHT +
              "\033[%s;%sH" % (y1, 2*x1)+"BL")
        self.dead = 0

    def change_health(self, damage):
        self.health = self.health-damage
        if(self.health < 0):
            self.dead = 1

    def increase_health(self):
        if((3/2)*(self.health) > baloon.maxhealth):
            self.health = baloon.maxhealth
        else:
            self.health = self.health*(3/2)


class king:
    maxhealth = 0

    def __init__(self, health):
        print(Back.BLUE+Fore.RED+Style.BRIGHT +
              "\033[%s;%sH" % (33, 2*17)+"KI")
        king.maxhealth = health
        self.health = health
        self.x = 17
        self.y = 33
        self.dead = 0

    def change_health(self, damage):
        self.health = self.health-damage
        i = 0
        k = ""
        p = ""
        while(i < (self.health/king.maxhealth)*20):
            k = k+" "
            i = i+1
        j = i
        while(i < 20):
            i = i+1
            p = p+" "
        print(Fore.YELLOW+Style.BRIGHT +
              "\033[%s;%sH" % (2, 2*45)+"KING HEALTH")
        print(Back.MAGENTA +
              "\033[%s;%sH" % (4, 2*45)+k)
        print(
            "\033[%s;%sH" % (4, 2*45+j)+p)
        if(self.health < 0):
            self.dead = 1

    def increase_health(self):
        if((3/2)*(self.health) > king.maxhealth):
            self.health = king.maxhealth
        else:
            self.health = self.health*(3/2)


class archerqueen:
    maxhealth = 0

    def __init__(self, health):
        print(Back.RED+Fore.WHITE+Style.BRIGHT +
              "\033[%s;%sH" % (33, 2*17)+"QU")
        archerqueen.maxhealth = health
        self.health = health
        self.x = 17
        self.y = 33
        self.dead = 0

    def change_health(self, damage):
        self.health = self.health-damage
        i = 0
        k = ""
        p = ""
        while(i < (self.health/archerqueen.maxhealth)*20):
            k = k+" "
            i = i+1
        j = i
        while(i < 20):
            i = i+1
            p = p+" "
        print(Fore.YELLOW+Style.BRIGHT +
              "\033[%s;%sH" % (2, 2*45)+"queen health")
        print(Back.MAGENTA +
              "\033[%s;%sH" % (4, 2*45)+k)
        print(
            "\033[%s;%sH" % (4, 2*45+j)+p)
        if(self.health < 0):
            self.dead = 1

    def increase_health(self):
        if((3/2)*(self.health) > archerqueen.maxhealth):
            self.health = archerqueen.maxhealth
        else:
            self.health = self.health*(3/2)
