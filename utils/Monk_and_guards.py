from utils.decipher import decipher
#each pirate should check whether he is in the center of the island and in the team signal do we have a presence of monk in that island or not
#team signal will have something like "Y" for presence of monk in that island and "N" for absence of monk in that island
#in the pirate signal 7th character is meant for whether he is monk or not 
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
        
        
#  thing to be included in actteam  
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