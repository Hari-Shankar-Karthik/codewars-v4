from random import randint

def explore_quadrant(pirate, primary_moves, lateral_moves):
    pirate_signal = pirate.getSignal().split(" ")
    last_move =  int(pirate_signal[2])
    current_move = None

    def sample(collection):
        return collection[randint(0, len(collection) - 1)]

    if last_move < 0:
        current_move = sample(lateral_moves)
        last_move *= -1
    else:
        current_move = primary_moves[last_move % len(primary_moves)]
        last_move = -(1 + last_move)
    
    pirate_signal[2] = str(last_move)
    pirate.setSignal(" ".join(pirate_signal))
    return current_move