import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
class Ship:
    listOfReaper = {}

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
        self.radius = 0


def calcDistance(ship1, ship2):
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
    my_rage = int(input())
    enemy_rage_1 = int(input())
    enemy_rage_2 = int(input())
    unit_count = int(input())
    for i in range(unit_count):
        unit_id, unit_type, player, mass, radius, x, y, vx, vy, extra, extra_2 = input().split()
        unit_id = int(unit_id)

        if unit_id not in Ship.listOfReaper:
            temp = Ship()
            Ship.listOfReaper[unit_id] = temp
        instance = Ship.listOfReaper[unit_id]
        instance.type = int(unit_type)
        instance.idPlayer = int(player)
        if instance.idPlayer == 0:
            myRepear = instance
        instance.mass = float(mass)
        instance.radius = int(radius)
        instance.x = int(x)
        instance.y = int(y)
        instance.vx = int(vx)
        instance.vy = int(vy)
        instance.extra = int(extra)
        extra_2 = int(extra_2)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    minDist = -1
    shipTogo = None
    for itShip in Ship.listOfReaper:
        instance = Ship.listOfReaper[itShip]
        if instance.type != 1 and instance.extra > 2:
            dist = calcDistance(instance, myRepear)
            print("DIST " + str(dist), file=sys.stderr)
            if minDist == -1 or minDist > dist:
                minDist = dist
                shipTogo = instance

    print(minDist, file=sys.stderr)
    print("TT " + str(calcDistance(myRepear, shipTogo)), file=sys.stderr)
    minDist = minDist - shipTogo.radius // 2
    if minDist < 200:
        print("WAIT")
    # elif minDist < 1000 and myRepear.vx != 0:
    #    print(str(instance.x) + " " + str(instance.y) +" 75")
    elif minDist < 4000 and myRepear.vx != 0:
        print(str(instance.x) + " " + str(instance.y) + " 125")
    else:
        print(str(instance.x) + " " + str(instance.y) + " 250")

    print("WAIT")
    print("WAIT")