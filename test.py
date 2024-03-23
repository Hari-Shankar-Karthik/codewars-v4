import random
import math
from utils.cipher import cipher
from utils.decipher import decipher
from utils.Monk_and_guards import monk
name = "sample1"


def moveTo(x, y, Pirate):
    position = Pirate.getPosition()
    if decipher(position[0]) == x and decipher(position[1]) == y:
        return 0
    if decipher(position[0]) == x:
        return ((position[1]) < y) * 2 + 1
    if decipher(position[1]) == y:
        return ((position[0]) > x) * 2 + 2
    if random.randint(1, 2) == 1:
        return (decipher(position[0]) > x) * 2 + 2
    else:
        return ((position[1]) < y) * 2 + 1


def ActPirate(pirate):
    up = pirate.investigate_up()
    down = pirate.investigate_down()
    left = pirate.investigate_left()
    right = pirate.investigate_right()
    x, y = decipher(pirate.getPosition())
    pirate.setSignal(" ")
    s = pirate.trackPlayers()
    monk(pirate)
    if (
        (up == "island1" and s[0] != "myCaptured")
        or (up == "island2" and s[1] != "myCaptured")
        or (up == "island3" and s[2] != "myCaptured")
    ):
        s = up[-1] + str(x) + "," + str(y - 1)
        pirate.setTeamSignal(s)

    if (
        (down == "island1" and s[0] != "myCaptured")
        or (down == "island2" and s[1] != "myCaptured")
        or (down == "island3" and s[2] != "myCaptured")
    ):
        s = down[-1] + str(x) + "," + str(y + 1)
        pirate.setTeamSignal(s)

    if (
        (left == "island1" and s[0] != "myCaptured")
        or (left == "island2" and s[1] != "myCaptured")
        or (left == "island3" and s[2] != "myCaptured")
    ):
        s = left[-1] + str(x - 1) + "," + str(y)
        pirate.setTeamSignal(s)

    if (
        (right == "island1" and s[0] != "myCaptured")
        or (right == "island2" and s[1] != "myCaptured")
        or (right == "island3" and s[2] != "myCaptured")
    ):
        s = right[-1] + str(x + 1) + "," + str(y)
        pirate.setTeamSignal(s)

    
    if pirate.getTeamSignal() != "":
        s = pirate.getTeamSignal()
        l = s.split(",")
        x = int(l[0][1:])
        y = int(l[1])
    
        return moveTo(x, y, pirate)

    else:
        return random.randint(1, 4)


def ActTeam(team):
    teamsignal = team.getTeamSignal()
    island1_monk = decipher(teamsignal[40])
    island2_monk = decipher(teamsignal[41])
    island3_monk = decipher(teamsignal[42])
    if island1_monk=="Y":
        team.buildWalls(1)
    if island2_monk=="Y":
        team.buildWalls(2)
    if island3_monk=="Y":
        team.buildWalls(3)   
    pass 