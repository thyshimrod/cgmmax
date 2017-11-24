import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
class Ship:
    listOfReaper = {}
    myDestroyer = None
    myReaper = None
    myDoof = None
    rage = 0
    point = 0
    pointToGo = [(3500,3500),(3500,-3500),(-3500,-3500),(-3500,3500)]
    reaperMax = 1
    def __init__(self):
        self.id = 0
        self.idPlayer = 0
        self.type = 0
        self.mass = 0
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.extra = 0
        self.extra2 = 0
        self.radius = 0
        
    def findShip(self,typeShip):
        found = None
        for itShip in Ship.listOfReaper:
            instance = Ship.listOfReaper[itShip]
            if instance.type == typeShip and instance.idPlayer not in (1, 0):
                dist1 = calcDistance(self,instance)
                dist2 = calcDistance(Ship.myReaper,instance)
                #print(str(dist1) + " / " + str(dist2),file=sys.stderr)
                if dist1 > 600 and dist1 < 2000 and abs(dist1 - dist2)> 400:
                    return instance
        return None

    def goToRepaerMaxScore(self):
        minDist = -1
        shipTogo = None
        for itShip in Ship.listOfReaper:
            instance = Ship.listOfReaper[itShip]
            # print(str(instance.type) + " " + str(instance.idPlayer),file=sys.stderr)
            if instance.type == 0 and instance.idPlayer == Ship.reaperMax:  # and instance.extra > 2:
                dist = calcDistance(instance, self)
                if minDist == -1 or minDist > dist:
                    minDist = dist
                    shipTogo = instance
        print("###" + str(minDist) + "//" + str(shipTogo), file=sys.stderr)
        if shipTogo is not None:
            print(str(shipTogo.x) + " " + str(shipTogo.y) + " 300")
        else:
            print("WAIT")

    def runReaper(self):
        print("runReaper", file=sys.stderr)
        minDist = -1
        shipTogo = None
        for itShip in Ship.listOfReaper:
            instance = Ship.listOfReaper[itShip]
            if instance.type == 4:  # and instance.extra > 2:
                dist = calcDistance(instance, self)
                if minDist == -1 or minDist > dist:
                    minDist = dist
                    shipTogo = instance

        print("..." + str(minDist) + "//" + str(shipTogo), file=sys.stderr)
        if shipTogo is not None:
            # minDist = minDist - shipTogo.radius // 2
            if minDist < 600:  # and self.vx != 0:
                print(str(shipTogo.x) + " " + str(shipTogo.y) + " 80")
            elif minDist < 1700:  # and self.vx != 0:
                print(str(shipTogo.x) + " " + str(shipTogo.y) + " 180")
            else:
                print(str(shipTogo.x) + " " + str(shipTogo.y) + " 250")
            '''if minDist < 250: # and self.vx != 0:
                print("WAIT")
            elif minDist < 1500 and self.vx != 0:
                print(str(shipTogo.x) + " " + str(shipTogo.y) + " 100")
            elif minDist < 3500 and self.vx != 0:
                print(str(shipTogo.x) + " " + str(shipTogo.y) + " 170")
            else:
                print(str(shipTogo.x) + " " + str(shipTogo.y) + " 250")
            '''
        else:
            if Ship.myDestroyer is not None:
                print(str(Ship.myDestroyer.x) + " " + str(Ship.myDestroyer.y) + " 100")
            else:
                print("WAIT")
                
                

    def runDestroyer(self):
        fire = False
        if Ship.rage > 60:
            tgt = self.findShip(0)
            if tgt is None:
                tgt = self.findShip(1)
                if tgt is None:
                    tgt = self.findShip(2)
            if tgt is not None:
                print("SKILL " + str(tgt.x) + " " + str(tgt.y))
                fire = True
            
        if fire == False:
            print("runDestroyer", file=sys.stderr)
            minDist = -1
            shipTogo = None
            for itShip in Ship.listOfReaper:
                instance = Ship.listOfReaper[itShip]
                if instance.type == 3 and instance.extra > 1:  # (instance.extra2 //2):  # and instance.extra > 2:
                    dist = calcDistance(instance, self)
                    if minDist == -1 or minDist > dist:
                        minDist = dist
                        shipTogo = instance
    
            if shipTogo is not None:
                print(str(shipTogo.x) + " " + str(shipTogo.y) + " 300")
            else:
                # self.goToNearestRepaer()
                #print("WAIT")
                print("0 0 100")

    def runDoof(self):
        self.goToRepaerMaxScore()
        """
        pt = Ship()
        pt.x = Ship.pointToGo[Ship.point][0]
        pt.y = Ship.pointToGo[Ship.point][1]
        print(str(pt.x) + " " + str(pt.y) + " 300")
        dist = calcDistance(self,pt)
        if dist < 600:
            Ship.point += 1
            Ship.point %= 4
        """

    def run(self):
        if self.type == 0:
            self.runReaper()
        elif self.type == 1:
            self.runDestroyer()
        elif self.type == 2:
            self.runDoof()


def calcDistance(ship1, ship2):
    # print(str(ship1) + " " + str(ship2),file=sys.stderr)
    a = ship1.x - ship2.x
    b = ship1.y - ship2.y
    dist = math.sqrt(a * a + b * b)

    return dist


# game loop
while True:
    Ship.listOfReaper = {}
    myRepear = None
    my_score = int(input())
    enemy_score_1 = int(input())
    enemy_score_2 = int(input())
    Ship.reaperMax = 1 if enemy_score_1 > enemy_score_2 else 2
        
    my_rage = int(input())
    enemy_rage_1 = int(input())
    enemy_rage_2 = int(input())
    unit_count = int(input())
    Ship.rage = my_rage
    for i in range(unit_count):
        unit_id, unit_type, player, mass, radius, x, y, vx, vy, extra, extra_2 = input().split()
        unit_id = int(unit_id)

        if unit_id not in Ship.listOfReaper:
            temp = Ship()
            Ship.listOfReaper[unit_id] = temp
        temp = Ship.listOfReaper[unit_id]
        temp.type = int(unit_type)
        temp.idPlayer = int(player)
        if temp.idPlayer == 0:
            if temp.type == 0:
                Ship.myReaper = temp
            elif temp.type == 1:
                Ship.myDestroyer = temp
            elif temp.type == 2:
                Ship.myDoof = temp
        temp.mass = float(mass)
        temp.radius = int(radius)
        temp.x = int(x)
        temp.y = int(y)
        temp.vx = int(vx)
        temp.vy = int(vy)
        temp.extra = int(extra)
        temp.extra_2 = int(extra_2)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    if Ship.myReaper is not None:
        Ship.myReaper.run()
    if Ship.myDestroyer is not None:
        Ship.myDestroyer.run()
    if Ship.myDoof is not None:
        Ship.myDoof.run()

