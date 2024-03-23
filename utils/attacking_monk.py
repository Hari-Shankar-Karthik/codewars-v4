from utils.cipher import cipher
from utils.decipher import decipher

def defending_monk(pirate):
    teamsignal = pirate.getTeamSignal()
    piratesignal = pirate.getSignal()
    current = pirate.investigate_current()[0]
    if current == "island1" and int(teamsignal[75]) < 5 and piratesignal[17]!="Y":
        n = int(teamsignal[75])+1
        final_pirate_signal = piratesignal[:17]+"Y"+piratesignal[18:]
        final_team_signal = teamsignal[:75] + str(n) + teamsignal[76:]
        pirate.setTeamSignal(final_team_signal)
        pirate.setSignal(final_pirate_signal)
        return 0
    elif current == "island2" and int(teamsignal[76]) < 5 and piratesignal[18]!="Y":
        n = int(teamsignal[76]+1)
        final_pirate_signal = piratesignal[:18]+"Y"+piratesignal[19:]
        final_team_signal = teamsignal[:76] + str(n) + teamsignal[77:]
        pirate.setTeamSignal(final_team_signal)
        pirate.setSignal(final_pirate_signal)
        return 0
        
    
    
    