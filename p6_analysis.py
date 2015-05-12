from p6_game import Simulator

ANALYSIS = {}

width = 32
height = 18
sim = None
moves = []

def analyze(design):
    sim = Simulator(design)
    # TODO: fill in this function, populating the ANALYSIS dict
    init = sim.get_initial_state()
    print "init: " + str(init)
    moves = sim.get_moves()
    print "move: " + str(moves)

    next_state = sim.get_next_state(init, moves[3])
    print "next state 1: " + str(next_state)
    next_state = sim.get_next_state(next_state, moves[3])
    print "next state 2: " + str(next_state)

    '''
    i = 0
    while i < 10:
        next_state = sim.get_next_state(next_state, moves[3])
        print "next state: " + str(next_state)
        i += 1
    '''

    #position, abilities = next_state # or None if character dies
    #i, j = position

    #path = bfs(init,next_state,adj,sim,moves)
    #ANALYSIS[next_state] = path



    x = 1
    y = 1
    while y < 32:
        x = 1
        while x < 17:

            current_state = ((x,y),frozenset())
            path = bfs(init,current_state,adj,sim,moves)
            #$path = []
            ANALYSIS[current_state] = path
            #print x," ", y
            x += 1
        y += 1

    current_state = ((3,3),frozenset())
    print "Analysis : " + str( ANALYSIS )
    print "Analysis -- : " + str( ANALYSIS[ current_state] )
    #raise NotImplementedError
    return

def inspect((i,j), draw_line):
    # TODO: use ANALYSIS and (i,j) draw some lines
    #raise NotImplementedError

    src = (1,1)
    dst = (i,j)

    dst_state = fake_convert(dst)

    src_state = fake_convert(src)


    #print "Analysis: " + str( ANALYSIS )
    parent = ANALYSIS[dst_state] # parent is a list
    print "parent" + str(parent)
    path = []
    '''
    if parent:
        node = dst_state
        # while node in parent:
        #     #print "node: " + str(node)
        #     path.append(node)
        #     node = parent[node]
        #     #print "parent" + str(parent[node])
        #     #print "node" + str(node)
        #     #draw_line((parent[node])[0], node[0],offset_obj=None, color_obj=None)
        # path.append(src_state)
        for node in parent:
            path.append(node)
    '''

    print path
    path = parent
    #print "testing: ", path[0][0]
    for next in path:
        draw_line(dst, next[0], offset_obj=None, color_obj=None)
        dst = next[0]



    #print node[0]
    #draw_line(node[0], (1,1), offset_obj=None, color_obj=None)
    #print path
    #draw_line((1,1), (2,2), offset_obj=None, color_obj=None)
    #draw_line((1,2), (2,2), offset_obj=None, color_obj=None)
    #draw_line((2,2), (3,2), offset_obj=None, color_obj=None)
    print "return"

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