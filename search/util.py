"""
This module contains some helper functions for printing actions and boards.
Feel free to use and/or modify them to help you develop your program.
"""

def print_move(n, x_a, y_a, x_b, y_b, **kwargs):
    """
    Output a move action of n pieces from square (x_a, y_a)
    to square (x_b, y_b), according to the format instructions.
    """
    print("MOVE {} from {} to {}.".format(n, (x_a, y_a), (x_b, y_b)), **kwargs)


def print_boom(x, y, **kwargs):
    """
    Output a boom action initiated at square (x, y) according to
    the format instructions.
    """
    print("BOOM at {}.".format((x, y)), **kwargs)


def print_board(board_dict, message="", unicode=False, compact=True, **kwargs):
    """
    For help with visualisation and debugging: output a board diagram with
    any information you like (tokens, heuristic values, distances, etc.).

    Arguments:
    board_dict -- A dictionary with (x, y) tuples as keys (x, y in range(8))
        and printable objects (e.g. strings, numbers) as values. This function
        will arrange these printable values on the grid and output the result.
        Note: At most the first 3 characters will be printed from the string
        representation of each value.
    message -- A printable object (e.g. string, number) that will be placed
        above the board in the visualisation. Default is "" (no message).
    unicode -- True if you want to use non-ASCII symbols in the board
        visualisation (see below), False to use only ASCII symbols.
        Default is False, since the unicode symbols may not agree with some
        terminal emulators.
    compact -- True if you want to use a compact board visualisation, with
        coordinates along the edges of the board, False to use a bigger one
        with coordinates alongside the printable information in each square.
        Default True (small board).

    Any other keyword arguments are passed through to the print function.
    """
    if unicode:
        if compact:
            template = """# {}
#    ┌───┬───┬───┬───┬───┬───┬───┬───┐
#  7 │{:}│{:}│{:}│{:}│{:}│{:}│{:}│{:}│
#    ├───┼───┼───┼───┼───┼───┼───┼───┤
#  6 │{:}│{:}│{:}│{:}│{:}│{:}│{:}│{:}│
#    ├───┼───┼───┼───┼───┼───┼───┼───┤
#  5 │{:}│{:}│{:}│{:}│{:}│{:}│{:}│{:}│
#    ├───┼───┼───┼───┼───┼───┼───┼───┤
#  4 │{:}│{:}│{:}│{:}│{:}│{:}│{:}│{:}│
#    ├───┼───┼───┼───┼───┼───┼───┼───┤
#  3 │{:}│{:}│{:}│{:}│{:}│{:}│{:}│{:}│
#    ├───┼───┼───┼───┼───┼───┼───┼───┤
#  2 │{:}│{:}│{:}│{:}│{:}│{:}│{:}│{:}│
#    ├───┼───┼───┼───┼───┼───┼───┼───┤
#  1 │{:}│{:}│{:}│{:}│{:}│{:}│{:}│{:}│
#    ├───┼───┼───┼───┼───┼───┼───┼───┤
#  0 │{:}│{:}│{:}│{:}│{:}│{:}│{:}│{:}│
#    └───┴───┴───┴───┴───┴───┴───┴───┘
# y/x  0   1   2   3   4   5   6   7"""
        else:
            template = """# {}
# ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
# │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │
# │ 0,7 │ 1,7 │ 2,7 │ 3,7 │ 4,7 │ 5,7 │ 6,7 │ 7,7 │
# ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
# │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │
# │ 0,6 │ 1,6 │ 2,6 │ 3,6 │ 4,6 │ 5,6 │ 6,6 │ 7,6 │
# ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
# │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │
# │ 0,5 │ 1,5 │ 2,5 │ 3,5 │ 4,5 │ 5,5 │ 6,5 │ 7,5 │
# ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
# │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │
# │ 0,4 │ 1,4 │ 2,4 │ 3,4 │ 4,4 │ 5,4 │ 6,4 │ 7,4 │
# ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
# │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │
# │ 0,3 │ 1,3 │ 2,3 │ 3,3 │ 4,3 │ 5,3 │ 6,3 │ 7,3 │
# ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
# │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │
# │ 0,2 │ 1,2 │ 2,2 │ 3,2 │ 4,2 │ 5,2 │ 6,2 │ 7,2 │
# ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
# │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │
# │ 0,1 │ 1,1 │ 2,1 │ 3,1 │ 4,1 │ 5,1 │ 6,1 │ 7,1 │
# ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
# │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │
# │ 0,0 │ 1,0 │ 2,0 │ 3,0 │ 4,0 │ 5,0 │ 6,0 │ 7,0 │
# └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘"""
    else:
        if compact:
            template = """# {}
#    +---+---+---+---+---+---+---+---+
#  7 |{:}|{:}|{:}|{:}|{:}|{:}|{:}|{:}|
#    +---+---+---+---+---+---+---+---+
#  6 |{:}|{:}|{:}|{:}|{:}|{:}|{:}|{:}|
#    +---+---+---+---+---+---+---+---+
#  5 |{:}|{:}|{:}|{:}|{:}|{:}|{:}|{:}|
#    +---+---+---+---+---+---+---+---+
#  4 |{:}|{:}|{:}|{:}|{:}|{:}|{:}|{:}|
#    +---+---+---+---+---+---+---+---+
#  3 |{:}|{:}|{:}|{:}|{:}|{:}|{:}|{:}|
#    +---+---+---+---+---+---+---+---+
#  2 |{:}|{:}|{:}|{:}|{:}|{:}|{:}|{:}|
#    +---+---+---+---+---+---+---+---+
#  1 |{:}|{:}|{:}|{:}|{:}|{:}|{:}|{:}|
#    +---+---+---+---+---+---+---+---+
#  0 |{:}|{:}|{:}|{:}|{:}|{:}|{:}|{:}|
#    +---+---+---+---+---+---+---+---+
# y/x  0   1   2   3   4   5   6   7"""
        else:
            template = """# {}
# +-----+-----+-----+-----+-----+-----+-----+-----+
# | {:} | {:} | {:} | {:} | {:} | {:} | {:} | {:} |
# | 0,7 | 1,7 | 2,7 | 3,7 | 4,7 | 5,7 | 6,7 | 7,7 |
# +-----+-----+-----+-----+-----+-----+-----+-----+
# | {:} | {:} | {:} | {:} | {:} | {:} | {:} | {:} |
# | 0,6 | 1,6 | 2,6 | 3,6 | 4,6 | 5,6 | 6,6 | 7,6 |
# +-----+-----+-----+-----+-----+-----+-----+-----+
# | {:} | {:} | {:} | {:} | {:} | {:} | {:} | {:} |
# | 0,5 | 1,5 | 2,5 | 3,5 | 4,5 | 5,5 | 6,5 | 7,5 |
# +-----+-----+-----+-----+-----+-----+-----+-----+
# | {:} | {:} | {:} | {:} | {:} | {:} | {:} | {:} |
# | 0,4 | 1,4 | 2,4 | 3,4 | 4,4 | 5,4 | 6,4 | 7,4 |
# +-----+-----+-----+-----+-----+-----+-----+-----+
# | {:} | {:} | {:} | {:} | {:} | {:} | {:} | {:} |
# | 0,3 | 1,3 | 2,3 | 3,3 | 4,3 | 5,3 | 6,3 | 7,3 |
# +-----+-----+-----+-----+-----+-----+-----+-----+
# | {:} | {:} | {:} | {:} | {:} | {:} | {:} | {:} |
# | 0,2 | 1,2 | 2,2 | 3,2 | 4,2 | 5,2 | 6,2 | 7,2 |
# +-----+-----+-----+-----+-----+-----+-----+-----+
# | {:} | {:} | {:} | {:} | {:} | {:} | {:} | {:} |
# | 0,1 | 1,1 | 2,1 | 3,1 | 4,1 | 5,1 | 6,1 | 7,1 |
# +-----+-----+-----+-----+-----+-----+-----+-----+
# | {:} | {:1} | {:} | {:} | {:} | {:} | {:} | {:} |
# | 0,0 | 1,0 | 2,0 | 3,0 | 4,0 | 5,0 | 6,0 | 7,0 |
# +-----+-----+-----+-----+-----+-----+-----+-----+"""
    # board the board string
    coords = [(x,7-y) for y in range(8) for x in range(8)]
    cells = []
    for xy in coords:
        if xy not in board_dict:
            cells.append("   ")
        else:
            cells.append(str(board_dict[xy])[:3].center(3))
    # print it
    print(template.format(message, *cells), **kwargs)



# Student made functions follow below

#Define Global Variables
z=0
x=1
y=2
stack=0
BUDGET=75
STATE=2

import heapq

def find_solution(data, **kwargs):

    # Prep data for use
    bridge_locs=[]

    # Step 1. Use data to form islands.
    islands,shorelines = form_islands(data)

    # Step 2. Check if the island is isolated or not to find any potential bridges.
    for curr_group in islands:

        if((isol_and_bridges(data, curr_group, bridge_locs))==True):

            #So that the positions in the list of islands corresponds to the list of bridge locs, add empty element
            bridge_locs.append(" ")

    # Step 3. Search through bridges to find final winning positions.
    return finalise_win_pos(data, islands, bridge_locs, shorelines)

class state:
    def __init__(self,win_pos,islands_left):
        self.win_pos=win_pos
        self.islands_states=islands_left

    def sol_found(self):
        if -1 in self.win_pos:
            return False
        else:
            return True

class node:
    def __init__(self,tile_data,wh_tiles,parent,in_position):
        self.tile_data=tile_data
        self.wh_tiles=wh_tiles
        self.parent=parent
        self.in_position=in_position

#Put adjacent bl_tiles into groups called "islands"
def form_islands(data, **kwargs):

        islands=[]
        group=[]
        win_pos=[]
        island_shore=[]

        #Initialise list of black tile locations from data
        black_tiles=data["black"]


        for curr_bl_tile in range(0,len(black_tiles)):


            if(len(group)==0):
                group = [black_tiles[curr_bl_tile]]

            #Step through a 1x1 square around the tile.
            for i in range(black_tiles[curr_bl_tile][x]-1, black_tiles[curr_bl_tile][x]+2):
                for j in range(black_tiles[curr_bl_tile][y]-1, black_tiles[curr_bl_tile][y]+2):

                    #Check the coordinate is actually on the board
                    if(on_board([i,j])):

                        #Can skip checking the tile the piece is on
                        if(not ((i==black_tiles[curr_bl_tile][x]) and (j==black_tiles[curr_bl_tile][y]))):

                                to_append=True

                                for bl_tile in range(0,len(black_tiles)):

                                    #To stop duplicates, only check bl_tiles that are further on in the list
                                    if((bl_tile>curr_bl_tile) and (black_tiles[bl_tile][x]==i) and (black_tiles[bl_tile][y]==j)):

                                        #The tile is adjacent so add it to the group, and swap so that it will be checked next.
                                        group.append(black_tiles[bl_tile])
                                        black_tiles=swap(black_tiles,curr_bl_tile+1,bl_tile)

                                    if([i,j] == [black_tiles[bl_tile][x],black_tiles[bl_tile][y]]):
                                        to_append=False

                                if([i,j] not in island_shore and to_append):
                                    island_shore.append([i,j])

            #If the curr_bl_tile is the last in the group list then we know it does not
            #have anymore adjacent tiles - append to lists and clear the group list
            if(group[-1] == black_tiles[curr_bl_tile]):
                islands.append(group)
                group=[]
                win_pos.append(island_shore)
                island_shore=[]

        return islands, win_pos

# the function 'isolated' should check if there is a bl_tile in the outer side of the 2x2 square and return True or False
def isol_and_bridges(data, island, bridge_locs, **kwargs):

    #Initialise list of black tile locations from data
    black_tiles=data["black"]
    isol=True
    isls_bridges=[]

    #Search in a 2x2 square around each tile that makes up the island
    for curr_tile in island:
        for i in range(curr_tile[x]-2,curr_tile[x]+3,1):
            for j in range(curr_tile[y]-2,curr_tile[y]+3,1):

                #Don't need to check if its in the 1x1 square, this has already been checked
                if(not ((abs(i-curr_tile[x])<=1) and (abs(j-curr_tile[y])<=1))):

                    #See if a black tile is on this location (that isn't already in the island)
                    for bl_tile in black_tiles:
                                if ((bl_tile not in island) and (bl_tile[x]==i) and (bl_tile[y]==j)):
                                    isol=False

                                    #Now to find the bridge locations. There are three cases to check
                                    #1. if the gap is a straight diagonal, there is only one tile that can be the bridge
                                    if(abs(curr_tile[x]-bl_tile[x])==2 and abs(curr_tile[y]-bl_tile[y])==2):
                                        if([(curr_tile[x]+bl_tile[x])/2,(curr_tile[y]+bl_tile[y])/2] not in bridge_locs):
                                            isls_bridges.append([int((curr_tile[x]+bl_tile[x])/2),int((curr_tile[y]+bl_tile[y])/2)])
                                    #2. if the gap is straight then there are three tiles that can form the bridge
                                    elif(curr_tile[x]-bl_tile[x]==0):
                                        for k in range(curr_tile[x]-1,curr_tile[x]+2):
                                            if([k,(curr_tile[y]+bl_tile[y])/2] not in bridge_locs):
                                                isls_bridges.append([k,int((curr_tile[y]+bl_tile[y])/2)])
                                    elif(curr_tile[y]-bl_tile[y]==0):
                                       for p in range(curr_tile[y]-1,curr_tile[y]+2):
                                            if([(curr_tile[x]+bl_tile[x])/2,p] not in bridge_locs):
                                                isls_bridges.append([int((curr_tile[x]+bl_tile[x])/2),p])
                                    #3. if the gap is like a knights move in chess, there are two tiles to bridge.
                                    else:
                                        if(abs(curr_tile[x]-bl_tile[x])==1):
                                         if([curr_tile[x],(curr_tile[y]+bl_tile[y])/2] not in bridge_locs):
                                                isls_bridges.append([curr_tile[x],int((curr_tile[y]+bl_tile[y])/2)])
                                         if([bl_tile[x],(curr_tile[y]+bl_tile[y])/2] not in bridge_locs):
                                                isls_bridges.append([bl_tile[x],int((curr_tile[y]+bl_tile[y])/2)])

                                        if(abs(curr_tile[y]-bl_tile[y])==1):
                                         if([curr_tile[y],(curr_tile[x]+bl_tile[x])/2] not in bridge_locs):
                                                isls_bridges.append([int((curr_tile[x]+bl_tile[x])/2),curr_tile[y]])
                                         if([bl_tile[y],(curr_tile[y]+bl_tile[y])/2] not in bridge_locs):
                                                isls_bridges.append([int((curr_tile[x]+bl_tile[x])/2),bl_tile[y]])

    if(not isol):
        bridge_locs.append(isls_bridges)
    return isol

# Finds winning solution coords, given bridge locations and win_pos for islands
def finalise_win_pos(data, islands, bridge_locs, shorelines, **kwargs):

    #Simplify problem automatically by removing islands that don't have a bridge as an option
    #Need to fix len of white so that it includes if white has a stack of more than 1
    win_pos=[-1]*len(data["white"])
    count=0
    islands_left=[1]*len(islands)

    for element in range(0,len(bridge_locs)):

        if bridge_locs[element] == " ":
            win_pos[count]=shorelines[element]
            count+=1
            islands_left[element]=0

    #Initialise states
    prior=0
    h=[]
    heapq.heapify(h)
    count=add_state(h,state(win_pos,islands_left),prior,0)

    expanded_states=0


    while (len(h)>0):

        #Pop next element off heap
        curr_entry=heapq.heappop(h)
        expanded_states+=1

        #Check if the solution has been found
        if(curr_entry[STATE].sol_found()):
            break

        #Check there are still white tiles to use
        elif -1 in curr_entry[STATE].win_pos:

            #Check if the program has been running for too long
            if(expanded_states>=BUDGET):
                print("Unable to find solution. Whoopsies.")
                break

            #Otherwise try a different solution
            else:
                for element in range(0,len(bridge_locs)):

                    if curr_entry[STATE].islands_states[element]==1:
                        original_curr_entry=curr_entry

                        for i in range(0,len(bridge_locs[element])):
                            curr_entry[STATE]=state(original_curr_entry[STATE].win_pos,original_curr_entry[STATE].islands_states)
                            coord = bridge_locs[element][i]
                            check_boom(curr_entry[STATE], bridge_locs, coord)
                            count=add_state(h,curr_entry[STATE],prior,count)

        prior+=1

    return curr_entry[STATE].win_pos


def check_boom(curr_state, bridge_locs, coord, **kwargs):

    for element in range(0,len(bridge_locs)):
        for i in bridge_locs[element]:
            if i == coord:
                curr_state.islands_states[element]=0

    for element in range(0,len(curr_state.win_pos)):
        if curr_state.win_pos[element]==-1:
            curr_state.win_pos[element]=coord
            break

#Extra helper functions#
def swap(list, pos_1, pos_2, **kwargs):

    list[pos_1], list[pos_2] = list[pos_2], list[pos_1]
    return list


def on_board(coords, **kwargs):

    return (coords[0]>=0 and coords[0]<=7 and coords[1]>=0 and coords[1]<=7)

def add_state(h, object, priority, count, **kwargs):

    entry=[priority, count, object]
    heapq.heappush(h,entry)
    return count+1


def closest_sol(possible_pos, initial_coord, **kwargs):
    closest_el=0
    for i in range(1,len(possible_pos)):
        if(manh_dist(possible_pos[i],initial_coord)<manh_dist(possible_pos[closest_el],initial_coord)):
            closest_el=i
    return possible_pos[closest_el]

def manh_dist(a, b):

    return (abs(a[0] - b[0]) + abs(a[1] - b[1]))

def is_on_black(data, coords, **kwargs):

    for bl_tile in data["black"]:
        if(coords[1:3] == bl_tile[1:3]):
            return True
    return False
    
def heuristic(x, y):

    return (abs(x[1] - x[0]) + abs(y[1] - y[0]))

def print_sol(data, paths, booms):

    #Print the movements of the white tiles
    #Check if the length of paths list is larger than 1
    #FIX
    if isinstance(paths[0], list):
        #Print through the path
        for i in range(0,len(paths),1):
            if(paths[i][0][0]-paths[i][1][0]==0):
                print_move(paths[i][0][0],paths[i][1][1],paths[i][1][2],paths[i][0][1],paths[i][0][2])
            else:
                print_move(abs(paths[i][0][0]-paths[i][1][0]),paths[i][1][1],paths[i][1][2],paths[i][0][1],paths[i][0][2])

    #Print the boom statements.
    for curr_wh_tile in range(0,len(data["white"])):
        #Check if the length of paths list is larger than 1
        print_boom(booms[curr_wh_tile][1],booms[curr_wh_tile][2])


def move_function(data, win_pos):

    coordinates = []
    white_tile = data["white"]
    curr=node(0, white_tile, 0,in_position=[-1]*len(white_tile))

    for curr_wh_tile in range(0,len(win_pos)):
        #Check if there is more than 1 winning position
        if isinstance(win_pos[curr_wh_tile][0], list):
            #Choose the closest coordinate to this white tile
            final=closest_sol(win_pos[curr_wh_tile],curr.wh_tiles[curr_wh_tile][1:3])
        else:
            final=win_pos[curr_wh_tile]

        wh_tiles=list(curr.wh_tiles)
        n=node(tuple(curr.wh_tiles[curr_wh_tile]),wh_tiles,-1,curr.in_position)
        n.wh_tiles.remove(curr.wh_tiles[curr_wh_tile])

        move_coordinates=[(0,1), (0,-1), (1,0), (-1,0)] 

        coord_set = set()
        heap =[]

        gscore = {n.tile_data:0}
        fscore = {n.tile_data:heuristic(n.tile_data[1:3], final)}

        count=add_state(heap,(fscore[n.tile_data], n),0,0)

        while heap:

            curr = heapq.heappop(heap)[2][1]

            if curr.tile_data[1:3] == tuple(final):

                #If stack is greater than 1, remove extra tiles at old location
                if(curr.tile_data[stack]>1):
                    #Make new tile have stack-1
                    curr.wh_tiles.append([curr.tile_data[stack]-1,curr.parent.tile_data[x],curr.parent.tile_data[y]])
                    #Make current tile have 1
                    curr.tile_data=[1,list(curr.tile_data)[x],list(curr.tile_data)[y]]
                    curr.tile_data=tuple(curr.tile_data)

                #Updates that the tile is in position, doesn't need to be checked to move anymore. 
                #Also updates the list of target locations to not include the already solved location.
                for el in range(0,len(curr.in_position)):
                    if curr.in_position[el] == -1 and (curr.tile_data not in curr.in_position):
                        curr.in_position[el]=curr.tile_data[1:3]
                        break

                curr.wh_tiles.insert(0,list(curr.tile_data))
                #print(white_tile)

                finish=curr.tile_data
                to_fix_wh_tiles=curr.wh_tiles
                #Travels through tree, recreating path as it goes.
                temp_list=[]
                while curr.parent != -1:
                    temp_list.append([curr.tile_data, curr.parent.tile_data])
                    curr = curr.parent
                for i in range(len(temp_list)-1,-1,-1):
                    coordinates.append(temp_list[i])

                for el in range(0,len(white_tile)):
                    if(white_tile[el][1:3]==list(curr.tile_data)[1:3]):
                        white_tile[el]=list(finish)

                curr.wh_tiles=to_fix_wh_tiles
                break

            coord_set.add(curr)

            for stack_height in range(1,curr.tile_data[stack]+1):
                for i, j in move_coordinates:

                    to_leave_behind=0
                    #Check if curr_pos is already in a winning position when about to jump - if so then leave behind a tile.
                    if(stack_height!=1 and curr.tile_data[1:3] in curr.in_position):
                            to_leave_behind=abs(1-curr.tile_data[stack])
                            if(([1,list(curr.tile_data)[1],list(curr.tile_data)[2]] not in curr.wh_tiles)):
                                curr.wh_tiles.insert(0,[1,curr.tile_data[x],curr.tile_data[y]])

                    check_coordinates = curr.tile_data[stack]-to_leave_behind, curr.tile_data[x] + i*stack_height, curr.tile_data[y] + j*stack_height

                    #Check the coordinate is on the board and not on a black tile
                    if(on_board(check_coordinates[1:3]) and (not is_on_black(data, list(check_coordinates)))):
                        temp_score = gscore[curr.tile_data] + heuristic(curr.tile_data, check_coordinates)

                        if check_coordinates in coord_set and temp_score >= gscore.get(check_coordinates, 0):
                            continue

                        if temp_score < gscore.get(check_coordinates, 0) or check_coordinates not in [i[1] for i in heap]:

                           #Check if the coordinate is on a white tile
                            for wh_tile in curr.wh_tiles:
                                if(list(check_coordinates)[1:3] == wh_tile[1:3] and (list(check_coordinates)[1:3] != n.tile_data[1:3])):
                                    check_coordinates=list(check_coordinates)[0]+list(wh_tile)[0], list(check_coordinates)[1],list(check_coordinates)[2]
                                    check_coordinates=tuple(check_coordinates)
                                    curr.wh_tiles.remove(wh_tile)
                                    break

                            gscore[check_coordinates] = temp_score
                            fscore[check_coordinates] = temp_score + heuristic(check_coordinates, final)

                            new_curr_wh_tiles=list(curr.wh_tiles)
                            new_node=node(check_coordinates,new_curr_wh_tiles,curr, curr.in_position)
                            count=add_state(heap,(fscore[check_coordinates], new_node),0,count)
                
    return coordinates, curr.wh_tiles
