from explore_quadrant import explore_main_quadrant

name = "trial_script"

def ActPirate(pirate):
    if pirate.getSignal() == "":
        pirate.setSignal(" " * 50)
    
    # "North" is 1, "East" is 2, "South" is 3, "West" is 4
    x_dimension = pirate.getDimensionX()
    y_dimension = pirate.getDimensionY()
    x, y = pirate.getPosition()

    if x < x_dimension / 2:
        if y < y_dimension / 2:
            return explore_main_quadrant(pirate, 2, 3)
    
        return explore_main_quadrant(pirate, 1, 2)
    
    if y < y_dimension / 2:
        return explore_main_quadrant(pirate, 3, 4)
    
    return explore_main_quadrant(pirate, 1, 4)

def ActTeam(team):
    pass