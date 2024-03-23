from utils.cipher import cipher

def intitializePirate(pirate):
    pirate_signal  = pirate.getSignal()
    if pirate_signal == "":                         # Initialization
        pirate_signal = cipher(int(pirate.getID())) + cipher(pirate.getPosition()[0]) + cipher(pirate.getPosition()[1]) + " "*97
        pirate.setSignal(pirate_signal)
    else:
        pirate_signal = pirate_signal[:1] + cipher(pirate.getPosition()[0]) + cipher(pirate.getPosition()[1]) + pirate_signal[3:]