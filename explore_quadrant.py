from random import randint
from utils.pirate_movements import moveTo, moveAway

def explore_main_quadrant(pirate, move_1, move_2):
    pirate_signal = pirate.getSignal().split(" ")
    if pirate_signal[2] == "":
        pirate_signal[2] = "F"
    
    was_last_move_1 =  pirate_signal[2] == "T"
    current_move = None

    is_favourable = lambda percent_chance: randint(1, 100) <= percent_chance

    if is_favourable(75):
        current_move = move_1 if was_last_move_1 else move_2
    else:
        was_last_move_1 = not was_last_move_1
        current_move = move_2 if was_last_move_1 else move_1
    
    pirate_signal[2] = "T" if was_last_move_1 else "F"
    pirate.setSignal(" ".join(pirate_signal))
    return current_move
    
    # last_move = (last_move + 1) % len(primary_moves)
    
    # pirate_signal[2] = str(last_move)
    # pirate.setSignal(" ".join(pirate_signal))
    # return current_move

    # sample = lambda collection: collection[randint(0, len(collection) - 1)]
    # return sample(primary_moves)