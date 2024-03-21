island_cord =["","","",""]

def updateIslandCord(pirate):
    up = pirate.investigate_up()[0]
    ne = pirate.investigate_ne()[0]
    nw = pirate.investigate_nw()[0]
    down = pirate.investigate_down()[0]
    se = pirate.investigate_se()[0]
    sw = pirate.investigate_sw()[0]
    right = pirate.investigate_right()[0]
    left = pirate.investigate_left()[0]
    x, y = pirate.getPosition()

    if (up[:-1] == "island"):
        if (up == ne and up == nw):
            s = up[-1] + str(x) + "," + str(y - 2)
        elif (up == ne):
            s = up[-1] + str(x+1) + "," + str(y - 2)
        else:
            s = up[-1] + str(x-1) + "," + str(y - 2)

        if(island_cord[int(s[0])] == ""):
            island_cord[int(s[0])] = s[1:]

    elif (down[:-1] == "island"):
        if (down == se and down == sw):
            s = down[-1] + str(x) + "," + str(y + 2)
        elif (down == se):
            s = down[-1] + str(x+1) + "," + str(y + 2)
        else:
            s = down[-1] + str(x-1) + "," + str(y + 2)

        if(island_cord[int(s[0])] == ""):
            island_cord[int(s[0])] = s[1:]

    elif (left[:-1] == "island"):
        if (left == nw and left == sw):
            s = left[-1] + str(x - 2) + "," + str(y)
        elif (left == nw):
            s = left[-1] + str(x - 2) + "," + str(y-1)
        else:
            s = left[-1] + str(x - 2) + "," + str(y+1)

        if(island_cord[int(s[0])] == ""):
            island_cord[int(s[0])] = s[1:]

    elif (right[:-1] == "island"):
        if(right == ne and right == se):
            s = right[-1] + str(x + 2) + "," + str(y)
        elif(right == ne):
            s = right[-1] + str(x + 2) + "," + str(y-1)
        else:
            s = right[-1] + str(x + 2) + "," + str(y+1)

        if(island_cord[int(s[0])] == ""):
            island_cord[int(s[0])] = s[1:]
    
    elif (ne[:-1] == "island"):
        s = ne[-1] + str(x + 2) + "," + str(y-2)
        if(island_cord[int(s[0])] == ""):
            island_cord[int(s[0])] = s[1:]

    elif (se[:-1] == "island"):
        s = se[-1] + str(x + 2) + "," + str(y+2)
        if(island_cord[int(s[0])] == ""):
            island_cord[int(s[0])] = s[1:]

    elif (nw[:-1] == "island"):
        s = nw[-1] + str(x - 2) + "," + str(y-2)
        if(island_cord[int(s[0])] == ""):
            island_cord[int(s[0])] = s[1:]

    elif (sw[:-1] == "island"):
        s = sw[-1] + str(x - 2) + "," + str(y + 2)
        if(island_cord[int(s[0])] == ""):
            island_cord[int(s[0])] = s[1:]

    return island_cord