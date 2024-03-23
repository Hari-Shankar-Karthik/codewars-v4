def checkInIsland(pirate, island_no):
    x, y = pirate.getPosition()
    team_signal = pirate.getTeamSignal()
    if island_no == 1 and team_signal[2*island_no - 1] != " ":
        island_x, island_y = decipher(team_signal[2*island_no - 2]), decipher(team_signal[2*island_no - 1])
        if abs(x - island_x) <=1  and abs(y - island_y) <= 1:
            return 1
        else:
            return 0
    elif island_no == 2 and team_signal[2*island_no - 1] != " ":
        island_x, island_y = decipher(team_signal[2*island_no - 2]), decipher(team_signal[2*island_no - 1])
        if abs(x - island_x) <=1  and abs(y - island_y) <= 1:
            return 1
        else:
            return 0
    elif island_no == 3 and team_signal[2*island_no - 1] != " ":
        island_x, island_y = decipher(team_signal[2*island_no - 2]), decipher(team_signal[2*island_no - 1])
        if abs(x - island_x) <=1  and abs(y - island_y) <= 1:
            return 1
        else:
            return 0

        
