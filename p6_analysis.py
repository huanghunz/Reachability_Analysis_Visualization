from p6_game import Simulator


def get_adj(sim, state):
    """
        The function gets the simulator and state
        return a list of available adjacents
    """
    adj_list = []

    for move in sim.get_moves():
        try:
            next_state = sim.get_next_state(state, move)
        except:
            next_state = None

        if next_state:
            adj_list.append((next_state) )

    return adj_list    


def analyze(design):
    """
        Gets a design object from p6_tool
        Do breath first search to find path for every position, 
        Save a dictionary of parent states.
    """
    global ANALYSIS
    sim = Simulator(design)

    init = sim.get_initial_state()
    ANALYSIS = {init: (None, None)}

    queue = []
    queue.append(init)

    while queue:
        curr_state = queue.pop(0) # list.pop(0) gets the first item, pop() gets the last one
        adj_list = get_adj(sim, curr_state)
        for adj in adj_list:
            if adj not in ANALYSIS:
                queue.append(adj)
                ANALYSIS[adj] = curr_state

    return

def inspect((i,j), draw_line):
    """
        Called when mouse hovers.
        Get coordination and a draw line function
        Pass line segments to draw_line function to draw on GUI
    """
   
    # look in the ANALYSIS dictionary to fetch all the possible path to the coordination
    for state in ANALYSIS:

        if (i,j) == state[0]: 
            _, color_offset = state
            node = state
           
            while node:
                curr_location, _ = node
                node = ANALYSIS[node]
                next, _ = node

                if next and curr_location:
                    draw_line(next, curr_location, color_offset, color_offset)
                else:
                    break
    return

