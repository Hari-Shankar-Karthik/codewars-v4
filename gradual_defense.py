from random import randint
from utils.closestN import ClosestN
from utils.cipher import cipher
from utils.decipher import decipher
from utils.island_identification import updateIslandCord
from utils.pirate_movements import moveTo
from utils.reduce_frames import reduceFrames
from utils.calculate_frames import calculateFrames
from utils.team_initialization_and_update import intitializeTeam
from utils.pirate_initialization import intitializePirate
from utils.reset_pirate_signal import resetPirateSignal

name = "Hack_of_clans"

def gradualDefensePirate(pirate):
    
    updateIslandCord(pirate)        # updates island coordiantes in team signal
    x, y = pirate.getPosition()
    team_signal = pirate.getTeamSignal()
    status = pirate.trackPlayers()
    no_of_pirates = decipher(team_signal[9])
    resetPirateSignal(pirate)

    for island_no in range(1,4):        #First loop to put a serpoint some tiles away and add it to team signal
        if status[island_no + 2] == "oppCapturing" and status[island_no - 1] == "myCaptured" and team_signal[5 + island_no] != " " and decipher(team_signal[5 + island_no]) != 0:
            for index in range(0,max(min(10,no_of_pirates//10),min(no_of_pirates,3))):
                if(team_signal[island_no*10+index] == cipher(int(pirate.getID()))):
                    island_x = decipher(team_signal[2*island_no-2])
                    island_y = decipher(team_signal[2*island_no-1])
                    pirate_signal = pirate.getSignal()
                    pirate_signal = pirate_signal[:3] + cipher(max(island_x-6,1)) + cipher(island_y) + pirate_signal[5:]
                    pirate_signal = pirate_signal[0] + cipher(x) + cipher(y) + pirate_signal[3:]
                    pirate.setSignal(pirate_signal)
                    return moveTo(decipher(pirate_signal[3]), decipher(pirate_signal[4]), pirate)

    for island_no in range(1,4):        #Once checkpoint reached push all pirates to interior of island
        if status[island_no+2] == "oppCapturing" and status[island_no - 1] == "myCaptured" and decipher(team_signal[5 + island_no]) == 0:
            for index in range(0,max(min(10,no_of_pirates//10),min(no_of_pirates,3))):
                if(team_signal[island_no*10+index] == cipher(int(pirate.getID()))):
                    island_x = decipher(team_signal[2*island_no-2])
                    island_y = decipher(team_signal[2*island_no-1])
                    pirate_signal = pirate.getSignal()
                    pirate_signal = pirate_signal[:3] + cipher(island_x) + cipher(island_y) + pirate_signal[5:]
                    pirate_signal = pirate_signal[0] + cipher(x) + cipher(y) + pirate_signal[3:]
                    pirate.setSignal(pirate_signal)
                    return moveTo(decipher(pirate_signal[3]), decipher(pirate_signal[4]), pirate)

    return None

def ActPirate(pirate):

    intitializePirate(pirate)
    move = gradualDefensePirate(pirate)
    if move is not None:
        return move

    team_signal = pirate.getTeamSignal()
    status = pirate.trackPlayers()
    pirate_signal = pirate.getSignal()
    x, y = pirate.getPosition()

    for island_no in range(1,4):                    # random attack strategy to be replaced with final. Used for testing gradual defense
        island_x = team_signal[2*island_no-2]
        island_y = team_signal[2*island_no-1]
        if island_x != " " and island_y != " " and status[island_no-1] != "myCaptured":
            rand = randint(1,10)
            if rand <= 1:
                pirate_signal = pirate_signal[0] + cipher(x) + cipher(y) + pirate_signal[3:]
                pirate.setSignal(pirate_signal)
                return moveTo(decipher(island_x), decipher(island_y), pirate)
    
    pirate_signal = pirate_signal[0] + cipher(x) + cipher(y) + pirate_signal[3:]
    pirate.setSignal(pirate_signal)
    return randint(1,4)

def gradualDefenseTeam(team):
    team_signal = team.getTeamSignal()
    no_of_pirates = int(team.getTotalPirates())
    for island_no in range(1,4):                # Updating closest 10 using closestN (wrt to assembly point)
        if team_signal[2*island_no - 2] != " " and team_signal[2*island_no - 1] != " ":
            island_x = decipher(team_signal[2*island_no - 2])
            island_y = decipher(team_signal[2*island_no - 1])
            assembly_x = max(island_x - 6, 1)
            assembly_y = island_y
            l = ClosestN(team, assembly_x, assembly_x, min(no_of_pirates,10))
            while len(l) != 10:
                l.append(" ")
            team_signal = team_signal[0:10*island_no] + cipher(l) + team_signal[10*(island_no + 1):]
            team.setTeamSignal(team_signal)

    team_signal = team.getTeamSignal()
    status = team.trackPlayers()

    for island_no in range(1,4):            # Reducing frames so that defense entry is coordinated
        if status[island_no + 2] == "oppCapturing" and team_signal[5 + island_no] != " " and decipher(team_signal[5 + island_no]) != 0:
            reduceFrames(team, island_no)              #Reduces frames required to reach assembly point by 1 

    for island_no in range(1,4):            # if Opp capturing calculating frames to assemble at common defense point
        if team_signal[2*island_no - 2] != " " and status[2 + island_no] == "oppCapturing" and status[island_no - 1] == "myCaptured" and team_signal[5 + island_no] == " ":
            island_x = decipher(team_signal[2*island_no - 2])
            island_y = decipher(team_signal[2*island_no - 1])
            pirates_defending = max(min(10,no_of_pirates//10),min(no_of_pirates,3))
            calculateFrames(team, pirates_defending, island_no)

    team_signal = team.getTeamSignal()

    for island_no in range(1,4):        # Reset signal if island is defended successfully 
        if status[2 + island_no] != "oppCapturing":
            team_signal = team_signal[:5 + island_no] + " " + team_signal[6 + island_no:]
            team.setTeamSignal(team_signal) 
        
def ActTeam(team):
  
    intitializeTeam(team)
    gradualDefenseTeam(team)

    # team_signal = team.getTeamSignal()
    # print(decipher(team_signal))
    # print(status)

    team.buildWalls(1)
    team.buildWalls(2)
    team.buildWalls(3)
