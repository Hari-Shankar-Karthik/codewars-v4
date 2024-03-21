from explore_quadrant import explore_main_quadrant, explore_side_quadrant

name = "trial_script"

def ActPirate(pirate):
    if pirate.getSignal() == "":
        pirate.setSignal(" " * 50)
    
    # "North" is 1, "East" is 2, "South" is 3, "West" is 4
    x_dimension = pirate.getDimensionX()
    y_dimension = pirate.getDimensionY()
    x, y = pirate.getPosition()

    

    if is_home_explored:
        return explore_side_quadrant(pirate)

    if x < x_dimension / 2 and y < y_dimension / 2:
        return explore_main_quadrant(pirate, 2, 3)
    elif x < x_dimension / 2 and y > y_dimension / 2:
        return explore_main_quadrant(pirate, 2, 1)
    elif x > x_dimension / 2 and y < y_dimension / 2:
        return explore_main_quadrant(pirate, 4, 3)
    elif x > x_dimension / 2 and y > y_dimension / 2:
        return explore_main_quadrant(pirate, 4, 1)
        
def ActTeam(team):
    pass