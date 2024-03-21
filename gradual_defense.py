from utils import pirate_movements
from random import randint
def ActPirate(pirate):
    state = pirate.trackPlayers()
    for index in range(3,len(state)):
        if state[index] == "oppCapturing" and island_cord[index-2] != "" and randint(1,10) == 1:
            x = island_cord[index-2].split(",")[0]
            y = island_cord[index-2].split(",")[1]
            pirate.moveTo(x,y,pirate)


def ActTeam(team):
    pass