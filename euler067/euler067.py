#Project Euler problem #67
#
# I will attempt to solve this using Djikstra's Algorithm.

import heapq
from collections import defaultdict
 
class Edge(object):
    def __init__(self, start, end, weight):
        self.start, self.end, self.weight = start, end, weight
 
    # For heapq.
    def __cmp__(self, other): return cmp(self.weight, other.weight)
 
class Graph(object):
    def __init__(self):
        # The adjacency list.
        self.adj = defaultdict(list)
 
    def add_e(self, start, end, weight = 0):
        #print "add_e:",start,end,weight
        self.adj[start].append(Edge(start, end, weight))
 
    def s_path(self, src):
        """
        Returns the distance to every vertex from the source and the
        array representing, at index i, the node visited before
        visiting node i. This is in the form (dist, previous).
        """
        dist, visited, previous, queue = {src: 0}, {}, {}, []
        heapq.heappush(queue, (dist[src],src))
        while len(queue) > 0:
            distance, current = heapq.heappop(queue)
            if current in visited:
                continue
            visited[current] = True
 
            for edge in self.adj[current]:
                relaxed = dist[current] + edge.weight
                end = edge.end
                if end not in dist or relaxed < dist[end]:
                    previous[end], dist[end] = current, relaxed
                    heapq.heappush(queue, (dist[end],end))
        return dist, previous




##g = Graph()
##g.add_e(0,1,0)
##g.add_e(1,2,4)
##g.add_e(1,4,1)
##g.add_e(2,1,74)
##g.add_e(2,3,2)
##g.add_e(2,5,12)
##g.add_e(3,2,12)
##g.add_e(3,10,12)
##g.add_e(3,6,74)
##g.add_e(4,7,22)
##g.add_e(4,5,32)
##g.add_e(5,8,33)
##g.add_e(5,4,66)
##g.add_e(5,6,76)
##g.add_e(6,10,21)
##g.add_e(6,9,11)
##g.add_e(7,3,12)
##g.add_e(7,8,10)
##g.add_e(8,7,2)
##g.add_e(8,9,72)
##g.add_e(9,10,7)
##g.add_e(9,6,31)
##g.add_e(9,8,18)
##g.add_e(10,6,8)
##
##start,end = 0,10
### Find a shortest path from vertex 'a' (1) to 'j' (10).
##dist, prev = g.s_path(start)
### Trace the path back using the prev array.
##path, current = [], end
##while current in prev:
##    path.insert(0, prev[current])
##    current = prev[current]
## 
##print path
##print dist[end]


g = Graph()
#fin = open('input_min.txt','r')
fin = open('triangle.txt','r')
##line = fin.readline()
##inputs = [int(x) for x in line.split()]

node = 1
lastrow = [1]
##g.add_e(0,node,inputs[0])


inputs = []

for line in fin:
    inputs.append( [100-int(x) for x in line.split()] )
##    print inputs
##    for l in lastrow:
##        g.add_e(l,0,0)
    
##print inputs
##print len(inputs)

nrows = len(inputs)
g.add_e(0,1,inputs[0][0])
for row in xrange(1,nrows):
    col = 0
    node = col + 1 + row*(row+1)/2
    g.add_e(node-row,node,inputs[row][col])

    for col in xrange(1,row):
        node = col + 1 + row*(row+1)/2
        g.add_e(node-row-1,node,inputs[row][col])
        g.add_e(node-row,node,inputs[row][col])

    col = row
    node = col + 1 + row*(row+1)/2
    g.add_e(node-row-1,node,inputs[row][col])

for col in xrange(len(inputs[-1])):
    node = col + 1 + row*(row+1)/2
    g.add_e(node,node-col+nrows,0)




start,end = 0,node-col+nrows
# Find a shortest path
dist, prev = g.s_path(start)
# Trace the path back using the prev array.
path, current = [], end
while current in prev:
    path.insert(0, prev[current])
    current = prev[current]
 
print path
print dist[end]
print (len(path)-1)*100 - dist[end]







