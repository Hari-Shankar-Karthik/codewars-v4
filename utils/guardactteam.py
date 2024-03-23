from utils.closestN import ClosestN
from utils.decipher import decipher
def guard_team(team):
    teamsignal = team.getTeamSignal()
    island2_location = decipher(teamsignal[2:4])
    trackplayers = team.trackplayers
    if trackplayers[1]=='myCapturing' and teamsignal[44:47]=='   ':
        lis = ClosestN(team , island2_location[0] , island2_location[1] , 16)
        lis.sort()
        add = []
        j = 0
        L = [44,47,50,53,56,59,62,65]
        for i in range(44,68):
            if i not in L:
                add.append(lis[j])
                j+=1
            else:
                add.append((i-44)//3 + 1)
        adds = "".join(map(str,add))
        final_teamsignal = teamsignal[:43] + adds + teamsignal[68:]
        team.setTeamSignal(final_teamsignal)
        pass
        
        
        
        
        