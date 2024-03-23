from random import randint

name = "final_scipt"

def get_quadrant(pirate, x, y):
    dimension_x = pirate.getDimensionX()
    dimension_y = pirate.getDimensionY()
    if x < dimension_x / 2:
        if y < dimension_y / 2:
            return 2
        return 3
    if y < dimension_y / 2:
        return 1
    return 4

def get_opposite_quadrant(quadrant):
    if quadrant == 1:
        return 3
    if quadrant == 2:
        return 4
    if quadrant == 3:
        return 1
    return 2

percent_chance = lambda percent_chance: randint(1, 100) <= percent_chance

def explore_main_quadrant(pirate, move_1, move_2):
    pirate_signal = list(pirate.getSignal())

    # The information about the last move is stored in index 5 of the pirate signal   
    was_last_move_1 =  pirate_signal[5] == "T"
    current_move = None

    if percent_chance(75):
        current_move = move_1 if was_last_move_1 else move_2
    else:
        was_last_move_1 = not was_last_move_1
        current_move = move_2 if was_last_move_1 else move_1
    
    pirate_signal[5] = "T" if was_last_move_1 else "F"
    pirate.setSignal("".join(pirate_signal))
    return current_move

def explore_side_quadrant(pirate, primary_move, secondary_moves):
    sample = lambda collection: collection[randint(0, len(collection) - 1)]

    return primary_move if percent_chance(60) else sample(secondary_moves)

def scout_explore(pirate):
    # "North" is 1, "East" is 2, "South" is 3, "West" is 4
    x_dimension = pirate.getDimensionX()
    y_dimension = pirate.getDimensionY()
    x, y = pirate.getPosition()
    pirate_signal = list(pirate.getSignal())

    # whether home quadrant is explored or not is stored in index 6 of the pirate signal
    is_home_explored = pirate_signal[6] == "T"

    if is_home_explored:
        # Index 7 contains the quadrant being explored
        # Index 8 contains the direction being explored
        # Index 12 stores T if rebound is activated
        quadrant_exploring = int(pirate_signal[7])
        is_exploring_X = pirate_signal[8] == "T"
        if quadrant_exploring == 1:
            if is_exploring_X:
                if x == x_dimension - 1:
                    pirate_signal[12] = "T"
                    pirate.setSignal("".join(pirate_signal))
                # if x == 0:
                if x == x_dimension//2:
                    pirate_signal[12] = " "
                    pirate.setSignal("".join(pirate_signal))
                if pirate_signal[12] == "T":
                    return explore_side_quadrant(pirate, 4, [1, 3])
                return explore_side_quadrant(pirate, 2, [1, 3])

            if y == 0:
                pirate_signal[12] = "T"
                pirate.setSignal("".join(pirate_signal))
            # if y == y_dimension - 1:
            if y == y_dimension//2:
                pirate_signal[12] = " "
                pirate.setSignal("".join(pirate_signal))
            if pirate_signal[12] == "T":
                return explore_side_quadrant(pirate, 3, [2, 4])
            return explore_side_quadrant(pirate, 1, [2, 4])
        
        if quadrant_exploring == 2:
            if is_exploring_X:
                if x == 0:
                    pirate_signal[12] = "T"
                    pirate.setSignal("".join(pirate_signal))
                # if x == x_dimension - 1:
                if x == x_dimension//2:
                    pirate_signal[12] = " "
                    pirate.setSignal("".join(pirate_signal))
                if pirate_signal[12] == "T":
                    return explore_side_quadrant(pirate, 2, [1, 3])
                return explore_side_quadrant(pirate, 4, [1, 3])
        
            if y == 0:
                pirate_signal[12] = "T"
                pirate.setSignal("".join(pirate_signal))
            # if y == y_dimension - 1:
            if y == y_dimension//2:
                pirate_signal[12] = " "
                pirate.setSignal("".join(pirate_signal))
            if pirate_signal[12] == "T":
                return explore_side_quadrant(pirate, 3, [2, 4])
            return explore_side_quadrant(pirate, 1, [2, 4])
        
        if quadrant_exploring == 3:
            if is_exploring_X:
                if x == 0 :
                    pirate_signal[12] = "T"
                    pirate.setSignal("".join(pirate_signal))
                # if x == x_dimension - 1:
                if x == x_dimension//2:
                    pirate_signal[12] = " "
                    pirate.setSignal("".join(pirate_signal))
                if pirate_signal[12] == "T":
                    return explore_side_quadrant(pirate, 2, [1, 3])
                return explore_side_quadrant(pirate, 4, [1, 3])

            if y == y_dimension - 1:
                pirate_signal[12] = "T"
                pirate.setSignal("".join(pirate_signal))
            # if y == 0:
            if y == y_dimension//2:
                pirate_signal[12] = " "
                pirate.setSignal("".join(pirate_signal))
            if pirate_signal[12] == "T":
                return explore_side_quadrant(pirate, 1, [2, 4])
            return explore_side_quadrant(pirate, 3, [2, 4])
            
        if is_exploring_X:
            if x == x_dimension - 1 :
                pirate_signal[12] = "T"
                pirate.setSignal("".join(pirate_signal))
            # if x == 0:
            if x == x_dimension//2:
                pirate_signal[12] = " "
                pirate.setSignal("".join(pirate_signal))
            if pirate_signal[12] == "T":
                return explore_side_quadrant(pirate, 4, [1, 3])
            return explore_side_quadrant(pirate, 2, [1, 3])
                    
        if y == y_dimension - 1:
            pirate_signal[12] = "T"
            pirate.setSignal("".join(pirate_signal))
        # if y == 0:
        if y == y_dimension//2:
            pirate_signal[12] = " "
            pirate.setSignal("".join(pirate_signal))
        if pirate_signal[12] == "T":
            return explore_side_quadrant(pirate, 1, [2, 4])
        return explore_side_quadrant(pirate, 3, [2, 4])    

    # if the pirate has just completed home quadrant, switch to side quadrant exploration
    if x == x_dimension // 2 or y == y_dimension // 2:
        is_home_explored = True
        quadrant_exploring = None
        is_exploring_X = None
        current_move = None

        # determine which quadrant is the home quadrant
        deploy_x, deploy_y = pirate.getDeployPoint()
        
        def get_home_quadrant():
            if deploy_x < x_dimension / 2:
                if deploy_y < y_dimension / 2:
                    return 2
                return 3
            if deploy_y < y_dimension / 2:
                return 1
            return 4
        
        home_quadrant = get_home_quadrant()

        # TODO: Condense this
        if x == x_dimension // 2:
            if home_quadrant == 1:
                # gotta explore quadrant 4
                current_move = explore_side_quadrant(pirate, 3, [2, 4])
                quadrant_exploring = 2
                is_exploring_X = True
            elif home_quadrant == 2:
                # gotta explore quadrant 3
                current_move = explore_side_quadrant(pirate, 3, [2, 4])
                quadrant_exploring = 1
                is_exploring_X = True
            elif home_quadrant == 3:
                # gotta explore quadrant 2
                current_move = explore_side_quadrant(pirate, 1, [2, 4])
                quadrant_exploring = 4
                is_exploring_X = True
            else:
                # gotta explore quadrant 1
                current_move = explore_side_quadrant(pirate, 1, [2, 4])
                quadrant_exploring = 3
                is_exploring_X = True
        else:
            if home_quadrant == 1:
                # gotta explore quadrant 2
                current_move = explore_side_quadrant(pirate, 4, [1, 3])
                quadrant_exploring = 4
                is_exploring_X = False
            elif home_quadrant == 2:
                # gotta explore quadrant 1
                current_move = explore_side_quadrant(pirate, 2, [1, 3])
                quadrant_exploring = 3
                is_exploring_X = False
            elif home_quadrant == 3:
                # gotta explore quadrant 4
                current_move = explore_side_quadrant(pirate, 2, [1, 3])
                quadrant_exploring = 2
                is_exploring_X = False
            else:
                # gotta explore quadrant 3
                current_move = explore_side_quadrant(pirate, 4, [1, 3])
                quadrant_exploring = 1
                is_exploring_X = False

        # Index 7 contains the quadrant being explored
        # Index 8 contains the direction being explored
        pirate_signal[6] = "T"
        pirate_signal[7] = str(quadrant_exploring)
        pirate_signal[8] = "T" if is_exploring_X else "F"
        pirate.setSignal("".join(pirate_signal))
        return current_move
    
    # otherwise, explore the home quadrant
    if x < x_dimension / 2 and y < y_dimension / 2:
        return explore_main_quadrant(pirate, 2, 3)
    elif x < x_dimension / 2 and y > y_dimension / 2:
        return explore_main_quadrant(pirate, 2, 1)
    elif x > x_dimension / 2 and y < y_dimension / 2:
        return explore_main_quadrant(pirate, 4, 3)
    elif x > x_dimension / 2 and y > y_dimension / 2:
        return explore_main_quadrant(pirate, 4, 1)

def infiltrate(pirate):
    pirate_signal = list(pirate.getSignal())
    deploy_x, deploy_y = pirate.getDeployPoint()

    home_quadrant = get_quadrant(pirate, deploy_x, deploy_y)
    opponent_quadrant = get_opposite_quadrant(home_quadrant)
    
    if pirate_signal[7] == " ":
        pirate_signal[7] = str(home_quadrant)
    
    quadrant = int(pirate_signal[7])
    
    if quadrant == home_quadrant or quadrant == opponent_quadrant:
        return None
    
    def goto_edge(current_quadrant, target_quadrant):
        if current_quadrant == 1:
            if target_quadrant == 2:
                if pirate.investigate_up()[0] == "wall":
                    return None
                return 1
            # target_quadrant == 4
            if pirate.investigate_right()[0] == "wall":
                return None
            return 2
        if current_quadrant == 2:
            if target_quadrant == 1:
                if pirate.investigate_up()[0] == "wall":
                    return None
                return 1
            # target_quadrant == 3
            if pirate.investigate_left()[0] == "wall":
                return None
            return 4
        if current_quadrant == 3:
            if target_quadrant == 2:
                if pirate.investigate_left()[0] == "wall":
                    return None
                return 4
            # target_quadrant == 4
            if pirate.investigate_down()[0] == "wall":
                return None
            return 3
        # current_quadrant == 4
        if target_quadrant == 1:
            if pirate.investigate_right()[0] == "wall":
                return None
            return 2
        # target_quadrant == 3
        if pirate.investigate_down()[0] == "wall":
            return None
        return 3

    def goto_enemy_spawn(current_quadrant, opponent_quadrant):
        if opponent_quadrant == 1:
            if pirate.investigate_up()[0] == "wall" and pirate.investigate_right()[0] == "wall":
                return None
        if opponent_quadrant == 2:
            if pirate.investigate_up()[0] == "wall" and pirate.investigate_left()[0] == "wall":
                return None
        if opponent_quadrant == 3:
            if pirate.investigate_down()[0] == "wall" and pirate.investigate_left()[0] == "wall":
                return None
        # opponent_quadrant == 4
        if pirate.investigate_down()[0] == "wall" and pirate.investigate_right()[0] == "wall":
            return None
                
        if current_quadrant == 1:
            if opponent_quadrant == 2:
                return 4
            # opponent_quadrant == 4
            return 3
        if current_quadrant == 2:
            if opponent_quadrant == 1:
                return 2
            # opponent_quadrant == 3
            return 3
        if current_quadrant == 3:
            if opponent_quadrant == 2:
                return 1
            # opponent_quadrant == 4
            return 2
        # current_quadrant == 4
        if opponent_quadrant == 1:
            return 1
        # opponent_quadrant == 3
        return 4


    def find_enemy_island(opponent_quadrant):
        if opponent_quadrant == 1:
            return explore_main_quadrant(pirate, 3, 4)
        if opponent_quadrant == 2:
            return explore_main_quadrant(pirate, 2, 3)
        if opponent_quadrant == 3:
            return explore_main_quadrant(pirate, 1, 2)
        # opponent_quadrant == 4
        return explore_main_quadrant(pirate, 1, 4)
    
    has_infiltrated = pirate_signal[14] == "T"

    if not has_infiltrated:
        temp = goto_edge(quadrant, opponent_quadrant)
        if temp is not None:
            return temp
        
        temp = goto_enemy_spawn(quadrant, opponent_quadrant)
        if temp is not None:
            return temp
        
        has_infiltrated = True
        pirate_signal[14] = "T"
        pirate.setSignal("".join(pirate_signal))
    
    return find_enemy_island(opponent_quadrant)

def cipher(l):
    s = ""
    if type(l) is list:
        for item in l:
            if item != " ":
                s += chr(int(item) + 63)
            else:
                s += " "
        return s
    else:
        if l != " ":
            return chr(int(l) + 63)
        else:
            return " "

def decipher(s):
    if len(s) > 1:
        l = []
        for ch in s:
            if ch == " ":
                l.append(" ")
            else:
                l.append(ord(ch) - 63)
        return l
    else:
        if s != " ":
            return ord(s) - 63
        else:
            return " "

def moveTo(x, y, Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return 0
    if position[0] == x:
        return (position[1] < y) * 2 + 1
    if position[1] == y:
        return (position[0] > x) * 2 + 2
    if randint(1, 2) == 1:
        return (position[0] > x) * 2 + 2
    else:
        return (position[1] < y) * 2 + 1

def reduceFrames(team, island_no):
    team_signal = team.getTeamSignal()
    team_signal = team_signal[:5 + island_no] + chr(ord(team_signal[5 + island_no]) - 1) + team_signal[6 + island_no:]
    team.setTeamSignal(team_signal)

def calculateFrames(team, no_of_pirates_defending, island_no):
    pirate_signals = team.getListOfSignals()
    team_signal = team.getTeamSignal()
    island_x = decipher(team_signal[2*island_no - 2])
    island_y = decipher(team_signal[2*island_no - 1])

    for pirate_signal in pirate_signals:
        if pirate_signal[0] == team_signal[10*island_no + no_of_pirates_defending - 1]:
            curr_x = decipher(pirate_signal[1])
            curr_y = decipher(pirate_signal[2])
            time_frames_reqd = abs(curr_x - max(island_x-6,1)) + abs(curr_y - island_y)
            team_signal = team_signal[:5 + island_no] + cipher(time_frames_reqd) + team_signal[6 + island_no:]
            team.setTeamSignal(team_signal)
            break

def resetPirateSignal(pirate):
    pirate_signal = pirate.getSignal()

    if pirate_signal[3] == pirate_signal[1]:            # Reset target location if target reached
        pirate_signal = pirate_signal[:3] + " " + pirate_signal[4:]
    if pirate_signal[4] == pirate_signal[2]:
        pirate_signal = pirate_signal[:4] + " " + pirate_signal[5:]
    pirate.setSignal(pirate_signal)

def ClosestN(team, x, y, N):        #Returns list of decipher closest N pirates to a point. Need to cipher it if using for team signal

    x = int(x)
    y = int(y)
    distances = {}
    pirate_signals = team.getListOfSignals()

    for pirate_signal in pirate_signals:
        if len(pirate_signal) == 100:
            curr_x = decipher(pirate_signal[1])
            curr_y = decipher(pirate_signal[2])
            pirate_id = decipher(pirate_signal[0])
            distances[pirate_id] = abs(curr_x - x) + abs(curr_y - y)
    
    sorted_dist = dict(sorted(distances.items(), key=lambda item: item[1]))
    l = []

    for index in range(0,min(N,len(list(sorted_dist)))):
        l.append(list(sorted_dist)[index])

    return l

def updateIslandCord(pirate):
    up = pirate.investigate_up()[0]
    ne = pirate.investigate_ne()[0]
    nw = pirate.investigate_nw()[0]
    down = pirate.investigate_down()[0]
    se = pirate.investigate_se()[0]
    sw = pirate.investigate_sw()[0]
    right = pirate.investigate_right()[0]
    left = pirate.investigate_left()[0]
    x, y = pirate.getPosition()

    team_signal = pirate.getTeamSignal()

    if (up[:-1] == "island"):

        island_no = int(up[-1])

        if (up == ne and up == nw):
            island_x = x 
            island_y = y - 2
        elif (up == ne):
            island_x = x + 1
            island_y = y - 2
        else:
            island_x = x - 1
            island_y = y - 2
    
        if(team_signal[2*island_no-2] == " "):
            team_signal = team_signal[0:2*island_no-2] + cipher(island_x) + cipher(island_y) + team_signal[2*island_no:]

    elif (down[:-1] == "island"):

        island_no = int(down[-1])

        if (down == se and down == sw):
            island_x = x
            island_y = y + 2
        elif (down == se):
            island_x = x + 1
            island_y = y + 2
        else:
            island_x = x - 1
            island_y = y + 2

        if(team_signal[2*island_no-2] == " "):
            team_signal = team_signal[0:2*island_no-2] + cipher(island_x) + cipher(island_y) + team_signal[2*island_no:]

    elif (left[:-1] == "island"):

        island_no = int(left[-1])

        if (left == nw and left == sw):
            island_x = x - 2
            island_y = y
        elif (left == nw):
            island_x = x - 2
            island_y = y - 1
        else:
            island_x = x - 2
            island_y = y + 1

        if(team_signal[2*island_no-2] == " "):
            team_signal = team_signal[0:2*island_no-2] + cipher(island_x) + cipher(island_y) + team_signal[2*island_no:]

    elif (right[:-1] == "island"):

        island_no = int(right[-1])

        if(right == ne and right == se):
            island_x = x + 2
            island_y = y
        elif(right == ne):
            island_x = x + 2
            island_y = y - 1
        else:
            island_x = x + 2
            island_y = y + 1

        if(team_signal[2*island_no-2] == " "):
            team_signal = team_signal[0:2*island_no-2] + cipher(island_x) + cipher(island_y) + team_signal[2*island_no:]
    
    elif (ne[:-1] == "island"):

        island_no = int(ne[-1])

        island_x = x + 2
        island_y = y - 2

        if(team_signal[2*island_no-2] == " "):
            team_signal = team_signal[0:2*island_no-2] + cipher(island_x) + cipher(island_y) + team_signal[2*island_no:]

    elif (se[:-1] == "island"):

        island_no = int(se[-1])

        island_x = x + 2
        island_y = y + 2

        if(team_signal[2*island_no-2] == " "):
            team_signal = team_signal[0:2*island_no-2] + cipher(island_x) + cipher(island_y) + team_signal[2*island_no:]


    elif (nw[:-1] == "island"):

        island_no = int(nw[-1])

        island_x = x - 2
        island_y = y - 2

        if(team_signal[2*island_no-2] == " "):
            team_signal = team_signal[0:2*island_no-2] + cipher(island_x) + cipher(island_y) + team_signal[2*island_no:]

    elif (sw[:-1] == "island"):

        island_no = int(sw[-1])

        island_x = x - 2
        island_y = y + 2

        if(team_signal[2*island_no-2] == " "):
            team_signal = team_signal[0:2*island_no-2] + cipher(island_x) + cipher(island_y) + team_signal[2*island_no:]

    pirate.setTeamSignal(team_signal)

def intitializePirate(pirate):
    pirate_signal  = pirate.getSignal()
    if pirate_signal == "":                         # Initialization
        pirate_signal = cipher(int(pirate.getID())) + cipher(pirate.getPosition()[0]) + cipher(pirate.getPosition()[1]) + " "*97
        pirate.setSignal(pirate_signal)
    else:
        pirate_signal = pirate_signal[:1] + cipher(pirate.getPosition()[0]) + cipher(pirate.getPosition()[1]) + pirate_signal[3:]
        pirate.setSignal(pirate_signal) 

def intitializeTeam(team):
    team_signal = team.getTeamSignal()
    no_of_pirates = int(team.getTotalPirates())

    if team_signal == "":               # Intitialization
        team_signal = " "*9 + cipher(no_of_pirates) + " "*90
        team.setTeamSignal(team_signal)
    
    team_signal = team_signal[:9] + cipher(no_of_pirates) + team_signal[10:] 
    team_signal_final = team_signal[:75] + "000" + team_signal[78:]
    #Updating no of pirates
    team.setTeamSignal(team_signal_final)

def gradualDefensePirate(pirate):
    
    # updateIslandCord(pirate)        # updates island coordiantes in team signal
    x, y = pirate.getPosition()
    team_signal = pirate.getTeamSignal()
    status = pirate.trackPlayers()
    no_of_pirates = decipher(team_signal[9])
    resetPirateSignal(pirate)

    for island_no in range(1,4):        #First loop to put a serpoint some tiles away and add it to team signal
        if status[island_no + 2] == "oppCapturing" and status[island_no - 1] == "myCaptured" and team_signal[5 + island_no] != " " and decipher(team_signal[5 + island_no]) > 0:
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
        if status[island_no+2] == "oppCapturing" and status[island_no - 1] == "myCaptured" and team_signal[5 + island_no] != " " and decipher(team_signal[5 + island_no]) <= 0:
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

def gradualDefenseTeam(team):
    team_signal = team.getTeamSignal()
    no_of_pirates = int(team.getTotalPirates())
    for island_no in range(1,4):                # Updating closest 10 using closestN (wrt to assembly point)
        if team_signal[2*island_no - 2] != " " and team_signal[2*island_no - 1] != " ":
            island_x = decipher(team_signal[2*island_no - 2])
            island_y = decipher(team_signal[2*island_no - 1])
            assembly_x = max(island_x - 6, 1)
            assembly_y = island_y
            l = ClosestN(team, assembly_x, assembly_y, min(no_of_pirates,10))
            while len(l) != 10:
                l.append(" ")
            team_signal = team_signal[0:10*island_no] + cipher(l) + team_signal[10*(island_no + 1):]
            team.setTeamSignal(team_signal)

    team_signal = team.getTeamSignal()
    status = team.trackPlayers()

    for island_no in range(1,4):            # Reducing frames so that defense entry is coordinated
        if status[island_no + 2] == "oppCapturing" and team_signal[5 + island_no] != " ":
            reduceFrames(team, island_no)              #Reduces frames required to reach assembly point by 1 

    for island_no in range(1,4):            # if Opp capturing calculating frames to assemble at common defense point
        if team_signal[2*island_no - 2] != " " and status[2 + island_no] == "oppCapturing" and status[island_no - 1] == "myCaptured" and team_signal[5 + island_no] == " ":
            island_x = decipher(team_signal[2*island_no - 2])
            island_y = decipher(team_signal[2*island_no - 1])
            pirates_defending = max(min(10,no_of_pirates//10),min(no_of_pirates,3))
            calculateFrames(team, pirates_defending, island_no)

    team_signal = team.getTeamSignal()

    for island_no in range(1,4):        # Reset signal if island is defended successfully or if all pirates have died which is remaining
            if team_signal[5 + island_no] != " " and (status[2 + island_no] != "oppCapturing" or decipher(team_signal[5 + island_no]) == -60):
                team_signal = team_signal[:5 + island_no] + " " + team_signal[6 + island_no:]
                team.setTeamSignal(team_signal) 
def monk(pirate):
    teamsignal = pirate.getTeamSignal()
    piratesignal = pirate.getSignal()
    island1_monk = teamsignal[40]
    island2_monk = teamsignal[41]
    island3_monk = teamsignal[42]
    island1_location = decipher(teamsignal[0:2])
    island2_location = decipher(teamsignal[2:4])
    island3_location = decipher(teamsignal[4:6])
    #check whether the monk is at the center of the island or not.if it is M then he is a monk
    location = decipher(piratesignal[1:3])
    trackplayers = pirate.trackPlayers()
    if (location == island1_location and trackplayers[0]=='myCaptured' and island1_monk !='N' and trackplayers[3]!='oppCaptured' ):
        final_pirate_signal = piratesignal[:9] + "M" + piratesignal[10:]
        pirate.setsignal(final_pirate_signal)
        final_team_signal = teamsignal[:40] + "Y" + teamsignal[41:]
        pirate.setTeamSignal(final_team_signal)
        return 0
    elif (location == island2_location and trackplayers[1]=='myCaptured' and island2_monk !='N' and trackplayers[4]!='oppCaptured'):
        final_pirate_signal = piratesignal[:10] + "M" + piratesignal[11:]
        pirate.setsignal(final_pirate_signal)
        final_team_signal = teamsignal[:41] + "Y" + teamsignal[42:]
        pirate.setTeamSignal(final_team_signal)  
        return 0
    elif (location == island3_location and trackplayers[3]=='myCaptured' and island3_monk !='N' and trackplayers[5]!='oppCaptured'):
        final_pirate_signal = piratesignal[:11] + "M" + piratesignal[12:]
        pirate.setsignal(final_pirate_signal)
        final_team_signal = teamsignal[:42] + "Y" + teamsignal[43:]
        pirate.setTeamSignal(final_team_signal)  
        return 0
    return None
def monkteam(team):
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
def circling_movement_of_guards(pirate):
    nw = pirate.investigate_nw()[0]
    sw = pirate.investigate_sw()[0]
    ne = pirate.investigate_ne()[0]
    se = pirate.investigate_se()[0]
    up = pirate.investigate_up()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    down = pirate.investigate_down()[0]
    current = pirate.investigate_current()[0]
    if(current.startswith('island') and se.startswith('island') and down.startswith('island') and right.startswith('island') ):
        return 2
    elif(current.startswith('island') and se.startswith('island') and sw.startswith('island') and down.startswith('island') and right.startswith('island') and left.startswith('island')):
        return 2
    elif(current.startswith('island') and  sw.startswith('island') and down.startswith('island') and right.startswith('island')):
        return 3
    elif(current.startswith('island') and se.startswith('island') and sw.startswith('island') and down.startswith('island') and up.startswith('island') and left.startswith('island')):
        return 3
    elif(current.startswith('island') and nw.startswith('island') and up.startswith('island') and left.startswith('island')):
        return 4
    elif(current.startswith('island') and ne.startswith('island') and nw.startswith('island') and up.startswith('island') and right.startswith('island') and left.startswith('island')):
        return 4
    elif(current.startswith('island') and ne.startswith('island') and right.startswith('island')and up.startswith('island') ):
        return 1
    elif(current.startswith('island') and ne.startswith('island') and se.startswith('island') and up.startswith('island') and right.startswith('island') and down.startswith('island')):
        return 1
def guard(pirate):
    
    teamsignal = pirate.getTeamSignal()
    piratesignal = pirate.getSignal()
    pirateID = int(pirate.getID())
    location = decipher(piratesignal[1:3])
    island2_location = decipher(teamsignal[2:4])
    if  piratesignal[13]=="C":
        for i in range(44,68):
            #the below case is completely meant when the pirate is becoming guard for the first time and once he has become a guard and reached 
            # the desired location he'll set the signal in both pirate and team signal. Upto that instant when they are about to reach their final
            #location 1 tile before their destination , they will not update the pirate signal or team signal. Once they update that for sure they
            #will reach their destination and follow the circling movement principle.
            #list of indices which will have location 
            L = [44,47,50,53,56,59,62,65]
            if i not in L:
                if teamsignal[i]==pirateID:
                    pirate1 = i-1
                    pirate2 = i-2
                    for d in L:
                        if d==pirate1:
                            l = (d-44)//3 + 1
                            if l==1:
                                destination = [island2_location[0]-1 ,island2_location[1]+1 ]
                                if(max(abs(location[0]-destination[0]) , abs(location[1]-destination[1]))==1 and min(abs(location[0]-destination[0]) , abs(location[1]-destination[1]))==0):
                                    finalteamsignal =teamsignal[:i] + " " + teamsignal[i+1:]
                                    final_piratesignal = piratesignal[:13] + "G" + piratesignal[14:]
                                    pirate.setTeamSignal(finalteamsignal)
                                    pirate.setSignal(final_piratesignal)
                                result = moveTo(destination[0] , destination[1] , pirate)
                                if (result==0):
                                    finalteamsignal =teamsignal[:i] + " " + teamsignal[i+1:]
                                    final_piratesignal = piratesignal[:13] + "G" + piratesignal[14:]
                                    pirate.setTeamSignal(finalteamsignal)
                                    pirate.setSignal(final_piratesignal)
                                return result
                            elif l==2:
                                destination = [island2_location[0] ,island2_location[1]+1 ]
                                if(max(abs(location[0]-destination[0]) , abs(location[1]-destination[1]))==1 and min(abs(location[0]-destination[0]) , abs(location[1]-destination[1]))==0):
                                    finalteamsignal =teamsignal[:i] + " " + teamsignal[i+1:]
                                    final_piratesignal = piratesignal[:13] + "G" + piratesignal[14:]
                                    pirate.setTeamSignal(finalteamsignal)
                                    pirate.setSignal(final_piratesignal)
                                result = moveTo(destination[0] , destination[1] , pirate)
                                if (result==0):
                                    finalteamsignal =teamsignal[:i] + " " + teamsignal[i+1:]
                                    final_piratesignal = piratesignal[:13] + "G" + piratesignal[14:]
                                    pirate.setTeamSignal(finalteamsignal)
                                    pirate.setSignal(final_piratesignal) 
                                return result
                            elif l==3:
                                destination = [island2_location[0]+1 ,island2_location[1]+1 ]
                                if(max(abs(location[0]-destination[0]) , abs(location[1]-destination[1]))==1 and min(abs(location[0]-destination[0]) , abs(location[1]-destination[1]))==0):
                                    finalteamsignal =teamsignal[:i] + " " + teamsignal[i+1:]
                                    final_piratesignal = piratesignal[:13] + "G" + piratesignal[14:]
                                    pirate.setTeamSignal(finalteamsignal)
                                    pirate.setSignal(final_piratesignal)
                                result = moveTo(destination[0] , destination[1] , pirate)
                                if (result==0):
                                    finalteamsignal =teamsignal[:i] + " " + teamsignal[i+1:]
                                    final_piratesignal = piratesignal[:13] + "G" + piratesignal[14:]
                                    pirate.setTeamSignal(finalteamsignal)
                                    pirate.setSignal(final_piratesignal)
                                return result
                            elif l==4:
                                destination = [island2_location[0]+1 ,island2_location[1] ]
                                if(max(abs(location[0]-destination[0]) , abs(location[1]-destination[1]))==1 and min(abs(location[0]-destination[0]) , abs(location[1]-destination[1]))==0):
                                    finalteamsignal =teamsignal[:i] + " " + teamsignal[i+1:]
                                    final_piratesignal = piratesignal[:13] + "G" + piratesignal[14:]
                                    pirate.setTeamSignal(finalteamsignal)
                                    pirate.setSignal(final_piratesignal)
                                result = moveTo(destination[0] , destination[1] , pirate)
                                if (result==0):
                                    finalteamsignal =teamsignal[:i] + " " + teamsignal[i+1:]
                                    final_piratesignal = piratesignal[:13] + "G" + piratesignal[14:]
                                    pirate.setTeamSignal(finalteamsignal)
                                    pirate.setSignal(final_piratesignal)   
                                return result
                            elif l==5:
                                destination = [island2_location[0]+1 ,island2_location[1]-1 ]
                                if(max(abs(location[0]-destination[0]) , abs(location[1]-destination[1]))==1 and min(abs(location[0]-destination[0]) , abs(location[1]-destination[1]))==0):
                                    finalteamsignal =teamsignal[:i] + " " + teamsignal[i+1:]
                                    final_piratesignal = piratesignal[:13] + "G" + piratesignal[14:]
                                    pirate.setTeamSignal(finalteamsignal)
                                    pirate.setSignal(final_piratesignal)
                                result = moveTo(destination[0] , destination[1] , pirate)
                                if (result==0):
                                    finalteamsignal =teamsignal[:i] + " " + teamsignal[i+1:]
                                    final_piratesignal = piratesignal[:13] + "G" + piratesignal[14:]
                                    pirate.setTeamSignal(finalteamsignal)
                                    pirate.setSignal(final_piratesignal)
                                return result
                            elif l==6:
                                destination = [island2_location[0]-1 ,island2_location[1] ]
                                if(max(abs(location[0]-destination[0]) , abs(location[1]-destination[1]))==1 and min(abs(location[0]-destination[0]) , abs(location[1]-destination[1]))==0):
                                    finalteamsignal =teamsignal[:i] + " " + teamsignal[i+1:]
                                    final_piratesignal = piratesignal[:13] + "G" + piratesignal[14:]
                                    pirate.setTeamSignal(finalteamsignal)
                                    pirate.setSignal(final_piratesignal)
                                result = moveTo(destination[0] , destination[1] , pirate)
                                if (result==0):
                                    finalteamsignal =teamsignal[:i] + " " + teamsignal[i+1:]
                                    final_piratesignal = piratesignal[:13] + "G" + piratesignal[14:]
                                    pirate.setTeamSignal(finalteamsignal)
                                    pirate.setSignal(final_piratesignal)
                                return result
                            elif l==7:
                                destination = [island2_location[0]-1 ,island2_location[1]-1 ]
                                if(max(abs(location[0]-destination[0]) , abs(location[1]-destination[1]))==1 and min(abs(location[0]-destination[0]) , abs(location[1]-destination[1]))==0):
                                    finalteamsignal =teamsignal[:i] + " " + teamsignal[i+1:]
                                    final_piratesignal = piratesignal[:13] + "G" + piratesignal[14:]
                                    pirate.setTeamSignal(finalteamsignal)
                                    pirate.setSignal(final_piratesignal)
                                result = moveTo(destination[0] , destination[1] , pirate)
                                if (result==0):
                                    finalteamsignal =teamsignal[:i] + " " + teamsignal[i+1:]
                                    final_piratesignal = piratesignal[:13] + "G" + piratesignal[14:]
                                    pirate.setTeamSignal(finalteamsignal)
                                    pirate.setSignal(final_piratesignal)
                                return result  
                            elif l==8:
                                destination = [island2_location[0]-1 ,island2_location[1] ]
                                if(max(abs(location[0]-destination[0]) , abs(location[1]-destination[1]))==1 and min(abs(location[0]-destination[0]) , abs(location[1]-destination[1]))==0):
                                    finalteamsignal =teamsignal[:i] + " " + teamsignal[i+1:]
                                    final_piratesignal = piratesignal[:13] + "G" + piratesignal[14:]
                                    pirate.setTeamSignal(finalteamsignal)
                                    pirate.setSignal(final_piratesignal)
                                result = moveTo(destination[0] , destination[1] , pirate)
                                if (result==0):
                                    finalteamsignal =teamsignal[:i] + " " + teamsignal[i+1:]
                                    final_piratesignal = piratesignal[:13] + "G" + piratesignal[14:]
                                    pirate.setTeamSignal(finalteamsignal)
                                    pirate.setSignal(final_piratesignal)
                                return result    
                            break
                        elif d==pirate2:
                            l = (d-44)//3 + 1
                            if l==1:
                                destination = [island2_location[0]-1 ,island2_location[1]+1 ]
                                if(max(abs(location[0]-destination[0]) , abs(location[1]-destination[1]))==1 and min(abs(location[0]-destination[0]) , abs(location[1]-destination[1]))==0):
                                    finalteamsignal =teamsignal[:i] + " " + teamsignal[i+1:]
                                    final_piratesignal = piratesignal[:13] + "G" + piratesignal[14:]
                                    pirate.setTeamSignal(finalteamsignal)
                                    pirate.setSignal(final_piratesignal)
                                result = moveTo(destination[0] , destination[1] , pirate)
                                if (result==0):
                                    finalteamsignal =teamsignal[:i] + " " + teamsignal[i+1:]
                                    final_piratesignal = piratesignal[:13] + "G" + piratesignal[14:]
                                    pirate.setTeamSignal(finalteamsignal)
                                    pirate.setSignal(final_piratesignal)
                                return result
                            elif l==2:
                                destination = [island2_location[0] ,island2_location[1]+1 ]
                                if(max(abs(location[0]-destination[0]) , abs(location[1]-destination[1]))==1 and min(abs(location[0]-destination[0]) , abs(location[1]-destination[1]))==0):
                                    finalteamsignal =teamsignal[:i] + " " + teamsignal[i+1:]
                                    final_piratesignal = piratesignal[:13] + "G" + piratesignal[14:]
                                    pirate.setTeamSignal(finalteamsignal)
                                    pirate.setSignal(final_piratesignal)
                                result = moveTo(destination[0] , destination[1] , pirate) 
                                if (result==0):
                                    finalteamsignal =teamsignal[:i] + " " + teamsignal[i+1:]
                                    final_piratesignal = piratesignal[:13] + "G" + piratesignal[14:]
                                    pirate.setTeamSignal(finalteamsignal)
                                    pirate.setSignal(final_piratesignal)
                                return result
                            elif l==3:
                                destination = [island2_location[0]+1 ,island2_location[1]+1 ]
                                if(max(abs(location[0]-destination[0]) , abs(location[1]-destination[1]))==1 and min(abs(location[0]-destination[0]) , abs(location[1]-destination[1]))==0):
                                    finalteamsignal =teamsignal[:i] + " " + teamsignal[i+1:]
                                    final_piratesignal = piratesignal[:13] + "G" + piratesignal[14:]
                                    pirate.setTeamSignal(finalteamsignal)
                                    pirate.setSignal(final_piratesignal)
                                result = moveTo(destination[0] , destination[1] , pirate)
                                if (result==0):
                                    finalteamsignal =teamsignal[:i] + " " + teamsignal[i+1:]
                                    final_piratesignal = piratesignal[:13] + "G" + piratesignal[14:]
                                    pirate.setTeamSignal(finalteamsignal)
                                    pirate.setSignal(final_piratesignal)
                                return result
                            elif l==4:
                                destination = [island2_location[0]+1 ,island2_location[1] ]
                                if(max(abs(location[0]-destination[0]) , abs(location[1]-destination[1]))==1 and min(abs(location[0]-destination[0]) , abs(location[1]-destination[1]))==0):
                                    finalteamsignal =teamsignal[:i] + " " + teamsignal[i+1:]
                                    final_piratesignal = piratesignal[:13] + "G" + piratesignal[14:]
                                    pirate.setTeamSignal(finalteamsignal)
                                    pirate.setSignal(final_piratesignal)
                                result = moveTo(destination[0] , destination[1] , pirate)  
                                if (result==0):
                                    finalteamsignal =teamsignal[:i] + " " + teamsignal[i+1:]
                                    final_piratesignal = piratesignal[:13] + "G" + piratesignal[14:]
                                    pirate.setTeamSignal(finalteamsignal)
                                    pirate.setSignal(final_piratesignal)
                                return result 
                            elif l==5:
                                destination = [island2_location[0]+1 ,island2_location[1]-1 ]
                                if(max(abs(location[0]-destination[0]) , abs(location[1]-destination[1]))==1 and min(abs(location[0]-destination[0]) , abs(location[1]-destination[1]))==0):
                                    finalteamsignal =teamsignal[:i] + " " + teamsignal[i+1:]
                                    final_piratesignal = piratesignal[:13] + "G" + piratesignal[14:]
                                    pirate.setTeamSignal(finalteamsignal)
                                    pirate.setSignal(final_piratesignal)
                                result = moveTo(destination[0] , destination[1] , pirate)
                                if (result==0):
                                    finalteamsignal =teamsignal[:i] + " " + teamsignal[i+1:]
                                    final_piratesignal = piratesignal[:13] + "G" + piratesignal[14:]
                                    pirate.setTeamSignal(finalteamsignal)
                                    pirate.setSignal(final_piratesignal)
                                return result
                            elif l==6:
                                destination = [island2_location[0]-1 ,island2_location[1] ]
                                if(max(abs(location[0]-destination[0]) , abs(location[1]-destination[1]))==1 and min(abs(location[0]-destination[0]) , abs(location[1]-destination[1]))==0):
                                    finalteamsignal =teamsignal[:i] + " " + teamsignal[i+1:]
                                    final_piratesignal = piratesignal[:13] + "G" + piratesignal[14:]
                                    pirate.setTeamSignal(finalteamsignal)
                                    pirate.setSignal(final_piratesignal)
                                result = moveTo(destination[0] , destination[1] , pirate)
                                if (result==0):
                                    finalteamsignal =teamsignal[:i] + " " + teamsignal[i+1:]
                                    final_piratesignal = piratesignal[:13] + "G" + piratesignal[14:]
                                    pirate.setTeamSignal(finalteamsignal)
                                    pirate.setSignal(final_piratesignal)
                                return result
                            elif l==7:
                                destination = [island2_location[0]-1 ,island2_location[1]-1 ]
                                if(max(abs(location[0]-destination[0]) , abs(location[1]-destination[1]))==1 and min(abs(location[0]-destination[0]) , abs(location[1]-destination[1]))==0):
                                    finalteamsignal =teamsignal[:i] + " " + teamsignal[i+1:]
                                    final_piratesignal = piratesignal[:13] + "G" + piratesignal[14:]
                                    pirate.setTeamSignal(finalteamsignal)
                                    pirate.setSignal(final_piratesignal)
                                result = moveTo(destination[0] , destination[1] , pirate)  
                                if (result==0):
                                    finalteamsignal =teamsignal[:i] + " " + teamsignal[i+1:]
                                    final_piratesignal = piratesignal[:13] + "G" + piratesignal[14:]
                                    pirate.setTeamSignal(finalteamsignal)
                                    pirate.setSignal(final_piratesignal)
                                return result
                            elif l==8:
                                destination = [island2_location[0]-1 ,island2_location[1] ]
                                if(max(abs(location[0]-destination[0]) , abs(location[1]-destination[1]))==1 and min(abs(location[0]-destination[0]) , abs(location[1]-destination[1]))==0):
                                    finalteamsignal =teamsignal[:i] + " " + teamsignal[i+1:]
                                    final_piratesignal = piratesignal[:13] + "G" + piratesignal[14:]
                                    pirate.setTeamSignal(finalteamsignal)
                                    pirate.setSignal(final_piratesignal)
                                result = moveTo(destination[0] , destination[1] , pirate)
                                if (result==0):
                                    finalteamsignal =teamsignal[:i] + " " + teamsignal[i+1:]
                                    final_piratesignal = piratesignal[:13] + "G" + piratesignal[14:]
                                    pirate.setTeamSignal(finalteamsignal)
                                    pirate.setSignal(final_piratesignal)
                                return result    
                            break        
    elif piratesignal[13]=='G':
        L = [44,47,50,53,56,59,62,65]
        #did every guard reached his location then only circling motion will begin.total is the variable that will denote whether everyone 
        #reached or not
        total = 0
        for i in range(44,68):
            if i not in L:
                if teamsignal[i]==" ":
                    total+=1
        if(total ==16):
            result = circling_movement_of_guards(pirate)
            return result
        else:
            return 0
    elif piratesignal[13]==' ':
        teamsignal = pirate.getTeamSignal()
        piratesignal = pirate.getSignal()
        pirateID = int(pirate.getID())
        location = decipher(piratesignal[1:3])
        island2_location = decipher(teamsignal[2:4])
        for i in range(44,68):
            L = [44,47,50,53,56,59,62,65]
            if i not in L:
                if teamsignal[i]==pirateID:
                    result = moveTo(island2_location[0] , island2_location[1] , pirate)
                    if(location[0]==island2_location[0] and location[1]==island2_location[1]):
                        final_piratesignal = piratesignal[:13] + "C" + piratesignal[14:]
                        pirate.setSignal(final_piratesignal)
                    return result
    return None
def guard_team(team):
    teamsignal = team.getTeamSignal()
    island2_location = decipher(teamsignal[2:4])
    trackplayers = team.trackPlayers()
    if trackplayers[1]=='myCapturing' and teamsignal[44:47]=='   ':
        lis = ClosestN(team , island2_location[0] , island2_location[1] , 16)
        add = [" "]*24
        #below approach will ensure that each location is atleast given one pirate 
        j = 0#j is used as index to loop over lis
        x = 0#x is used as index for loop over location
        y = 1#y is used as index for 1st pirate in each location
        z = 2#z is used as index for 2nd pirate in each location
        L = [44,47,50,53,56,59,62,65]
        for i in range(44,68):
            if i not in L:
                # print(lis)
                # print(j)
                if i%3==0:
                    if j<len(lis):
                        add[y] = cipher(lis[j])
                        j+=1
                        y+=3
                else:
                    if j<len(lis):
                        add[z] = cipher(lis[j])
                        j+=1
                        z+=3
            else:
                add[x] = str(((i-44)//3 + 1))
                x+=3
        adds = "".join(map(str,add))
        final_teamsignal = teamsignal[:43] + adds + teamsignal[68:]
        print(final_teamsignal)
        team.setTeamSignal(final_teamsignal)
        pass               
def attacking_monk(pirate):
    teamsignal = pirate.getTeamSignal()
    piratesignal = pirate.getSignal()
    currentx = pirate.investigate_current()
    current = currentx[0]
    print(teamsignal)
    if current == "island1" and int(teamsignal[75]) < 5 and piratesignal[17]!="Y":
        n = int(teamsignal[75])+1
        final_pirate_signal = piratesignal[:17]+"Y"+piratesignal[18:]
        final_team_signal = teamsignal[:75] + str(n) + teamsignal[76:]
        pirate.setTeamSignal(final_team_signal)
        pirate.setSignal(final_pirate_signal)
        return 0
    elif current == "island2" and int(teamsignal[76]) < 5 and piratesignal[18]!="Y":
        n = int(teamsignal[76])+1
        final_pirate_signal = piratesignal[:18]+"Y"+piratesignal[19:]
        final_team_signal = teamsignal[:76] + str(n) + teamsignal[77:]
        pirate.setTeamSignal(final_team_signal)
        pirate.setSignal(final_pirate_signal)
        return 0
    elif current == "island3" and int(teamsignal[77]) < 5 and piratesignal[19]!="Y":
        n = int(teamsignal[77])+1
        final_pirate_signal = piratesignal[:19]+"Y"+piratesignal[20:]
        final_team_signal = teamsignal[:77] + str(n) + teamsignal[78:]
        pirate.setTeamSignal(final_team_signal)
        pirate.setSignal(final_pirate_signal)
        return 0
    return None
def ActPirate(pirate):
    
    intitializePirate(pirate)
    updateIslandCord(pirate)
    attackmonk = attacking_monk(pirate)
    print(attackmonk)
    if attackmonk is not None:
        return attackmonk
        
    # check for sahil's L-shape capture function (capturing home island)
    # check for rolling guard (capturing second`` island)
    move_guard = guard(pirate)
    #print (move_guard)
    if move_guard is not None:
        return move_guard
    # check for monk (defending captured islands)
    move_monk = monk(pirate)
    #print(move_monk)
    if move_monk is not None:
        return move_monk
    # check for gradual defense (defending islands whose monk has been killed)
    gradual_defense_move = gradualDefensePirate(pirate)
    if gradual_defense_move is not None:
        return gradual_defense_move

    # check for infiltrate (capturing third island if second island is oppCaptured)
    # infiltrate_move = infiltrate(pirate)
    # if infiltrate_move is not None:
    #     return infiltrate_move
    
    # check for exploration (in all other cases)
    return scout_explore(pirate)

        
def ActTeam(team):
    intitializeTeam(team)
    gradualDefenseTeam(team)
    monkteam(team)
    guard_team(team)
    # print(team.getTeamSignal())
    # team.buildWalls(1)
    # team.buildWalls(2)
    # team.buildWalls(3)