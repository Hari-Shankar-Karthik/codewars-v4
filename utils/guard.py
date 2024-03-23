from utils import closestN
from utils.cipher import cipher
from utils.decipher import decipher
from utils.Monk_and_guards import circling_movement_of_guards
from utils.pirate_movements import moveTo
def guard(pirate):
    teamsignal = pirate.getTeamSignal()
    piratesignal = pirate.getSignal()
    pirateID = decipher(pirateID = int(pirate.getID())())
    location = decipher(piratesignal[1:3])
    island2_location = decipher(teamsignal[2:4])
    if piratesignal[13]!="G":
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