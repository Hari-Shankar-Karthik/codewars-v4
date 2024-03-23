from random import randint
from utils.pirate_movements import moveTo
from final_script import get_quadrant
from utils.decipher import decipher

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
    pirate_signal = list(pirate.getSignal())
    pirate_x, pirate_y = pirate.getPosition()
    dimension_x, dimension_y = pirate.getDimensionX(), pirate.getDimensionY()

    # if we have completed exploring this quadrant, check if this is the one with no island
    # if so, we need to move to the home quadrant
    # index 12 in the pirate signal stores whether or not the quadrant has an island
    my_quadrant = get_quadrant(pirate, pirate_x, pirate_y)
    
    for island_number in [1, 2, 3]:
        island_x = decipher(pirate_signal[island_number * 2 - 2])
        island_y = decipher(pirate_signal[island_number * 2 - 1])
        if island_x != " " and island_y != " ":
            island_quadrant = get_quadrant(pirate, island_x, island_y)

            if my_quadrant == island_quadrant:
                return primary_move if percent_chance(60) else sample(secondary_moves)
    
    if primary_move == 1 and pirate_y == 0:
        pirate_signal[12] = "T"
    if primary_move == 2 and pirate_x == dimension_x - 1:
        pirate_signal[12] = "T"
    if primary_move == 3 and pirate_y == dimension_y - 1:
        pirate_signal[12] = "T"
    if primary_move == 4 and pirate_x == 0:
        pirate_signal[12] = "T"
    
    if pirate_signal[12] == "T":
        pirate.setSignal("".join(pirate_signal))

        def get_home_center():
            deploy_x, deploy_y = pirate.getDeployPoint()
            home_quadrant = get_quadrant(pirate, deploy_x, deploy_y)

            if home_quadrant == 1:
                return dimension_x * 3 // 4, dimension_y // 4
            if home_quadrant == 2:
                return dimension_x // 4, dimension_y // 4
            if home_quadrant == 3:
                return dimension_x // 4, dimension_y * 3 // 4
            # home_quadrant == 4
            return dimension_x * 3 // 4, dimension_y * 3 // 4

        home_center_x, home_center_y = get_home_center()
        return moveTo(home_center_x, home_center_y, pirate)

    return primary_move if percent_chance(60) else sample(secondary_moves)