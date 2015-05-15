from p6_game import Simulator



def get_adj(sim, state):
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


    sim = Simulator(design)
    # TODO: fill in this function, populating the ANALYSIS dict
    init = sim.get_initial_state()


    global ANALYSIS

    queue = []
    ANALYSIS = {init: (None, None)}


    queue.append(init)
    while queue:
        curr_state = queue.pop(0)
        adj_list = get_adj(sim, curr_state)
        for adj in adj_list:
            if adj not in ANALYSIS:
                queue.append(adj)
                ANALYSIS[adj] = curr_state


    print ANALYSIS

    return

def inspect((i,j), draw_line):
    src = (1,1)
    possible_solution_list = get_possible_solution(ANALYSIS, (i,j))
    #print possible_solution_list

    for solution in possible_solution_list:
        _, color_offset = solution
        node = solution
        #print "node ", node
        while node:
            curr_location, _ = node
            node = ANALYSIS[node]
            next, _ = node

            if next and curr_location:
                draw_line(next, curr_location, color_offset, color_offset)
            else:
                break



def get_possible_solution(analysis,coord):
    newlist = []
    for state in analysis:
        if coord == state[0]:
            newlist.append(state)
    return newlist

