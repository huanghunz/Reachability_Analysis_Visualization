from p6_game import Simulator
import copy



def reset_ANALYSIS():
    global ANALYSIS 
    ANALYSIS = {}


sim = None
moves = []


def get_adj(sim, curr_state, moves, ability_list ):
    adj_list = []

    # print "abi = ", ability_list
    # print "cur - ", curr_state[1]
    update_state = (curr_state[0], ability_list)
    #check = False
    #print "[1] :", curr_state[1]
    #s = copy.copy(special_list)
    for move in moves: 

        try: 
            next_state = sim.get_next_state(update_state, move)
        except:
            next_state = None

        # #if next_state:
        # # ex. ((10, 5), frozenset(['water_survival']))
        # if not next_state: # die

        #     while s and not next_state: # multi abilities, want to get a avaiable state

        #         special_state = s.pop() # ability state
        #         try:
        #             next_state = sim.get_next_state(special_state, move)
        #             print next_state
        #             check = True
        #         except:
        #             #next_state = None

        if next_state:
            adj_list.append((next_state) )
  
    return adj_list


def analyze(design):

    reset_ANALYSIS()
    sim = Simulator(design)
    # TODO: fill in this function, populating the ANALYSIS dict
    init = sim.get_initial_state()
  #  print "init: " + str(init[0])
    moves = sim.get_moves()
  #  print "move: " + str(moves)

    width, height = sim.get_map_size()

    path = []
    #ANALYSIS = {}

    queue = []
    prev = {init:None}
    ANALYSIS[init[0]] = None


    # print
    # print "================="
    # print ANALYSIS[init[0]]
    # print
    # print
    # print "================="


    discovered = []

    discovered.append(init[0])
   
    queue.append(init)
    ability_list = frozenset()

    while queue:
        curr_state = queue.pop()

        adj_list = get_adj(sim, curr_state, moves, ability_list) #[ ( (), check) ]

        for adj in adj_list:

        
            if adj[0] not in discovered :
                if adj[1]:
                    ability_list = adj[1]
                discovered.append(adj[0])
                queue.append(adj)
               # prev[adj] = curr_state
                ANALYSIS[adj[0]] = curr_state
              
    # for a in ANALYSIS:
    #     print ANALYSIS[a][0], " - "

    print ANALYSIS[init[0]]

    return


def inspect((i,j), draw_line):
    # TODO: use ANALYSIS and (i,j) draw some lines
    #raise NotImplementedError

    #return
  # prevTable = ANALYSIS
  

    src = (1,1)
    dst = (i,j)

    dst_state = fake_convert(dst)

    src_state = fake_convert(src)


    # #print "Analysis: " + str( ANALYSIS )
    parent = ANALYSIS # parent is a list
  
    path = []
    node = parent[src]

    #print node



    if parent:
        node = dst_state[0]

       # print node
        node = parent[dst] # get a state ---> ( (x,y), abi_set)
        while node:

            #print "node: " + str(node)

            path.append(node[0])
            node = (parent[node[0]]) #

            #print "parent" + str(parent[node])
            #print "node" + str(node)
            #draw_line((parent[node])[0], node[0],offset_obj=None, color_obj=None)
        path.append(src_state[0])
        #for node in parent:
        #    path.append(node)
    

    # print path
    # ANALYSIS[a][0]
    #path = ANALYSIS
    #print path
    # #print "testing: ", path[0][0]
    for next in path:
         draw_line(dst, next, offset_obj=None, color_obj=None)
         dst = next



    # #print node[0]
    # #draw_line(node[0], (1,1), offset_obj=None, color_obj=None)
    # #print path
    # #draw_line((1,1), (2,2), offset_obj=None, color_obj=None)
    # #draw_line((1,2), (2,2), offset_obj=None, color_obj=None)
    # #draw_line((2,2), (3,2), offset_obj=None, color_obj=None)
    # print "return"

    return


def adj(src,sim,moves):
    state_list = []
    next = None
    i = 0
    while i < 5:
        #print "next: " + str(next)
        try:
            next_pos, next_abi = sim.get_next_state(src,moves[i])
        except:
            next_pos = None
            next_abi = None
        state_list.append((next_pos,next_abi))
        i += 1
    return state_list


def bfs(source, target, adj,sim,moves):
    """Find a path from source to target on the graph defined by the adj function."""
    # initialize bookkeeping structures
    parent = {}
    discovered = {}
    queue = []

    # explore starting at the source node

    discovered[source] = True
    queue.append(source)


    while queue:
        u = queue.pop()
        #print "queue: " + str(u)
        if u == target: # early termination
            break
        next = adj(u,sim,moves)
        if next is not None:
            for v in next:
                #print "v: " + str(v)
                if v not in discovered:
                    discovered[v] = True
                    parent[v] = u
                    queue.append(v)


    # reconstruct the path backwards, starting at the target node
    if u != target:
        #print "no path"
        return []

    path = []
    node = target
    while node in parent:
        #print "abc"
        path.append(node)
        node = parent[node]
    path.append(source)
    #path.reverse()

    return path

def fake_convert((i,j)):
    fake_state = ((i,j),frozenset())
    return fake_state