#PE #107

#determines whether we run the small 7x7 case or the full 40x40 case
DEBUG = False

from pygraph.algorithms.minmax import minimal_spanning_tree
from pygraph.classes.graph import graph
from pygraph.mixins.labeling import labeling


def total_weight(g, refg):
    total = 0
    for edge in g.edges():
        total += refg.edge_weight(edge)
    return total/2 #This seems to be double-counting edges. E.g. (1,3) and (3,1)

N = 7 if DEBUG else 40
filename = 'network_min.txt' if DEBUG else 'network.txt'

matrix = []

for row,line in enumerate(file(filename,'r')):
    matrix.append([0]*N)
    line = line.strip()
    for col,cost in enumerate(line.split(',')):
        if cost != '-' and col >= row:
            matrix[row][col] = int(cost)
            if DEBUG:
                print(row, col, cost)


g = graph()
g.add_nodes(range(N))

for r in xrange(N):
    for c in xrange(r,N):
        if matrix[r][c] != 0:
            g.add_edge((r,c), matrix[r][c])
            if DEBUG:
                print(r, c, matrix[r][c])
        
            

st = minimal_spanning_tree(g)
ming = graph()
ming.add_spanning_tree(st)

if DEBUG:
    print(st)
    print()
    print(ming)
    print()

print(total_weight(g,g))
print(total_weight(ming,g))
print(total_weight(g,g) - total_weight(ming,g))

