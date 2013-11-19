#PE 82

#determines whether we run the small 5x5 case or the full 80x80 case
DEBUG = False

from pygraph.algorithms.minmax import shortest_path
from pygraph.classes.digraph import digraph

if DEBUG:
    N = 5
else:
    N = 80
    
matrix = [[0]*N]*N

if DEBUG:
    matrix = [[131,	673,	234,	103,	18],
                [201,	96,	342,	965,	150],
                [630,	803,	746,	422,	111],
                [537,	699,	497,	121,	956],
                [805,	732,	524,	37,	331]]
else:
    row = 0
    for line in file('matrix.txt','r'):
        matrix[row] = [int(c) for c in line.split(',')]
        row += 1

#Maps row & column indexes to the node label
def rctonode(r, c):
    return r * N + c

#just pick some node labels outside of [0,N*N-1]
START = 2*N*N
END = 3*N*N

g = digraph()
g.add_nodes(range(N*N))
g.add_nodes([START, END])

for c in xrange(N):
    for r in xrange(N):
        #top-left corner
        if r==0 and c==0:
            g.add_edge((START, rctonode(r,c)), matrix[r][c])
            g.add_edge((rctonode(r+1,c), rctonode(r,c)),matrix[r][c])
            
        #top-right corner
        elif r==0 and c==(N-1):
            g.add_edge((rctonode(r,c),END), 0)
            g.add_edge((rctonode(r,c-1), rctonode(r,c)),matrix[r][c])
            g.add_edge((rctonode(r+1,c), rctonode(r,c)),matrix[r][c])
            
        #bottom-left corner
        elif r==(N-1) and c==0:
            g.add_edge((START, rctonode(r,c)), matrix[r][c])
            g.add_edge((rctonode(r-1,c), rctonode(r,c)),matrix[r][c])
            
        #bottom-right corner
        elif r==(N-1) and c==(N-1):
            g.add_edge((rctonode(r,c),END), 0)
            g.add_edge((rctonode(r-1,c), rctonode(r,c)),matrix[r][c])
            g.add_edge((rctonode(r,c-1), rctonode(r,c)),matrix[r][c])
            
        #first row
        elif r==0:
            g.add_edge((rctonode(r,c-1), rctonode(r,c)),matrix[r][c])
            g.add_edge((rctonode(r+1,c), rctonode(r,c)),matrix[r][c])
            
        #last row
        elif r==(N-1):
            g.add_edge((rctonode(r,c-1), rctonode(r,c)),matrix[r][c])
            g.add_edge((rctonode(r-1,c), rctonode(r,c)),matrix[r][c])
            
        #first column
        elif c==0:
            g.add_edge((START, rctonode(r,c)), matrix[r][c])
            g.add_edge((rctonode(r-1,c), rctonode(r,c)), matrix[r][c])
            g.add_edge((rctonode(r+1,c), rctonode(r,c)), matrix[r][c])
            
        #last column
        elif c==(N-1):
            g.add_edge((rctonode(r,c),END), 0)
            g.add_edge((rctonode(r,c-1), rctonode(r,c)), matrix[r][c])
            g.add_edge((rctonode(r-1,c), rctonode(r,c)), matrix[r][c])
            g.add_edge((rctonode(r+1,c), rctonode(r,c)), matrix[r][c])
            
        #everywhere else in the middle
        else:
            g.add_edge((rctonode(r,c-1), rctonode(r,c)),matrix[r][c])
            g.add_edge((rctonode(r-1,c), rctonode(r,c)),matrix[r][c])
            g.add_edge((rctonode(r+1,c), rctonode(r,c)),matrix[r][c])
            

st,dist = shortest_path(g, START)

if DEBUG:
    print(st)
    print(dist)

print(dist[END])

