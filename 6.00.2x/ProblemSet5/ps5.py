# 6.00.2x Problem Set 5
# Graph optimization
# Finding shortest paths through MIT buildings
#

import string
# This imports everything from `graph.py` as if it was defined in this file!
from graph import * 

#
# Problem 2: Building up the Campus Map
#
# Before you write any code, write a couple of sentences here 
# describing how you will model this problem as a graph. 

# This is a helpful exercise to help you organize your
# thoughts before you tackle a big design problem!
#

def load_map(mapFilename):
    """ 
    Parses the map file and constructs a directed graph

    Parameters: 
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive 
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    mapMIT = open(mapFilename, 'r')
    data = mapMIT.readlines()
    mitDigraph = WeightedDigraph()
    number = 0
    for i in data:
        number += 1
        values = i.split(' ')
        startNode = Node(values[0])
        endNode = Node(values[1])
        try:
            mitDigraph.addNode(startNode)
        except ValueError:
            pass
        try:
            mitDigraph.addNode(endNode)
        except ValueError:
            pass
        myEdge = WeightedEdge(startNode, endNode, float(values[2]), float(values[3]))
        mitDigraph.addEdge(myEdge)

    return mitDigraph


# mitMap = load_map('C:/Users/NetzeK/Documents/6.00.2x/ProblemSet5/mit_map.txt')
# print isinstance(mitMap, Digraph)
# print isinstance(mitMap, WeightedDigraph)
# print mitMap.nodes
# print mitMap.edges
        

#
# Problem 3: Finding the Shortest Path using Brute Force Search
#
# State the optimization problem as a function to minimize
# and what the constraints are
#
def getDistances(digraph, startNode, endNode):
    myList = digraph.edges[Node(startNode)]
    for i in myList:
        if Node(i[0]) == Node(endNode):
            return [i[1][0], i[1][1]]


def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    pathStack = []
    pathsFound = []
    shortestDist = maxTotalDist
    shortestPath = []
    pathStack.append([str(start)])
    while len(pathStack) != 0:
        for i in range(len(pathStack)):
            actualNode = pathStack[0][-1]
            childrens = digraph.childrenOf(Node(actualNode))
            newChildrens = []
            for j in range(len(childrens)):
                child = pathStack[0][:]
                child.append(str(childrens[j]))
                newChildrens.append(child)
                if Node(end) == Node(child[-1]) and child not in pathsFound:
                    actualDistOutdoors = 0
                    for k in range(len(child)-1):
                        actualDistOutdoors += getDistances(digraph, child[k], child[k+1])[1]
                    if actualDistOutdoors <= maxDistOutdoors:
                        pathsFound.append(child)
        pathStack = newChildrens + pathStack[1:]

    for i in pathsFound:
        actualTotalDist = 0
        for j in range(len(i)-1):
            actualTotalDist += getDistances(digraph, i[j], i[j+1])[0]
        if actualTotalDist <= shortestDist:
            shortestPath = i

    if len(shortestPath) != 0:
        return shortestPath
    else:
        raise ValueError



    # if Node(start) == Node(end):
    #     return Node(end)
    # for i in digraph.childrenOf(Node(start)):
    #     if getDistances(digraph.edges[Node(start)], i)[1] < maxDistOutdoors:
    #         bruteForceSearch(digraph, i, end, maxTotalDist, maxDistOutdoors)
    # return Node(start)


def testDFS():
    na = Node(1)
    nb = Node(2)
    nc = Node(3)
    nd = Node(4)
    ne = Node(5)
    nf = Node(6)
    ng = Node(7)
    nh = Node(8)
    ni = Node(9)
    nj = Node(10)
    nk = Node(11)
    nl = Node(12)

    g = WeightedDigraph()
    g.addNode(na)
    g.addNode(nb)
    g.addNode(nc)
    g.addNode(nd)
    g.addNode(ne)
    g.addNode(nf)
    g.addNode(ng)
    g.addNode(nh)
    g.addNode(ni)
    g.addNode(nj)
    g.addNode(nk)
    g.addNode(nl)
    randomEdge = WeightedEdge(na, nb, 2, 1)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(na, nc, 2, 1)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(nb, nd, 2, 1)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(nb, ne, 4, 3)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(nc, ne, 2, 1)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(nc, nf, 3, 2)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(nc, ng, 1, 1)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(nd, nh, 2, 1)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(nd, ni, 4, 3)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(ne, ni, 2, 1)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(ne, nj, 1, 1)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(nf, nj, 2, 1)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(nf, nk, 2, 1)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(nf, nl, 4, 3)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(ng, nf, 1, 1)
    g.addEdge(randomEdge)

    return bruteForceSearch(g, 1, 10, 8, 4)

print testDFS()

#
# Problem 4: Finding the Shortest Path using Optimized Search Method
#
def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using directed depth-first.
    search approach. The total distance travelled on the path must not
    exceed maxTotalDist, and the distance spent outdoor on this path must
	not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    pathStack = []
    pathsFound = []
    shortestDist = maxTotalDist
    shortestPath = []
    pathStack.append([str(start)])
    while len(pathStack) != 0:
        for i in range(len(pathStack)):
            actualNode = pathStack[0][-1]
            childrens = digraph.childrenOf(Node(actualNode))
            newChildrens = []
            for j in range(len(childrens)):
                child = pathStack[0][:]
                child.append(str(childrens[j]))
                newChildrens.append(child)
                if Node(end) == Node(child[-1]) and child not in pathsFound:
                    actualDistOutdoors = 0
                    for k in range(len(child)-1):
                        actualDistOutdoors += getDistances(digraph, child[k], child[k+1])[1]
                    if actualDistOutdoors <= maxDistOutdoors:
                        pathsFound.append(child)
        pathStack = newChildrens + pathStack[1:]

    for i in pathsFound:
        actualTotalDist = 0
        for j in range(len(i)-1):
            actualTotalDist += getDistances(digraph, i[j], i[j+1])[0]
        if actualTotalDist <= shortestDist:
            shortestPath = i

    if len(shortestPath) != 0:
        return shortestPath
    else:
        raise ValueError

# Uncomment below when ready to test
### NOTE! These tests may take a few minutes to run!! ####
if __name__ == '__main__':
    # Test cases
    mitMap = load_map("mit_map.txt")
    print isinstance(mitMap, Digraph)
    print isinstance(mitMap, WeightedDigraph)
    print 'nodes', mitMap.nodes
    print 'edges', mitMap.edges


    LARGE_DIST = 1000000

    # Test case 1
    print "---------------"
    print "Test case 1:"
    print "Find the shortest-path from Building 32 to 56"
    expectedPath1 = ['32', '56']
    brutePath1 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
    dfsPath1 = directedDFS(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath1
    print "Brute-force: ", brutePath1
    print "DFS: ", dfsPath1
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath1 == brutePath1, expectedPath1 == dfsPath1)

    # Test case 2
    print "---------------"
    print "Test case 2:"
    print "Find the shortest-path from Building 32 to 56 without going outdoors"
    expectedPath2 = ['32', '36', '26', '16', '56']
    brutePath2 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, 0)
    dfsPath2 = directedDFS(mitMap, '32', '56', LARGE_DIST, 0)
    print "Expected: ", expectedPath2
    print "Brute-force: ", brutePath2
    print "DFS: ", dfsPath2
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath2 == brutePath2, expectedPath2 == dfsPath2)

    # Test case 3
    print "---------------"
    print "Test case 3:"
    print "Find the shortest-path from Building 2 to 9"
    expectedPath3 = ['2', '3', '7', '9']
    brutePath3 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
    dfsPath3 = directedDFS(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath3
    print "Brute-force: ", brutePath3
    print "DFS: ", dfsPath3
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath3 == brutePath3, expectedPath3 == dfsPath3)

    # Test case 4
    print "---------------"
    print "Test case 4:"
    print "Find the shortest-path from Building 2 to 9 without going outdoors"
    expectedPath4 = ['2', '4', '10', '13', '9']
    brutePath4 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, 0)
    dfsPath4 = directedDFS(mitMap, '2', '9', LARGE_DIST, 0)
    print "Expected: ", expectedPath4
    print "Brute-force: ", brutePath4
    print "DFS: ", dfsPath4
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath4 == brutePath4, expectedPath4 == dfsPath4)

    # Test case 5
    print "---------------"
    print "Test case 5:"
    print "Find the shortest-path from Building 1 to 32"
    expectedPath5 = ['1', '4', '12', '32']
    brutePath5 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
    dfsPath5 = directedDFS(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath5
    print "Brute-force: ", brutePath5
    print "DFS: ", dfsPath5
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath5 == brutePath5, expectedPath5 == dfsPath5)

    # Test case 6
    print "---------------"
    print "Test case 6:"
    print "Find the shortest-path from Building 1 to 32 without going outdoors"
    expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
    brutePath6 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, 0)
    dfsPath6 = directedDFS(mitMap, '1', '32', LARGE_DIST, 0)
    print "Expected: ", expectedPath6
    print "Brute-force: ", brutePath6
    print "DFS: ", dfsPath6
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath6 == brutePath6, expectedPath6 == dfsPath6)

    # Test case 7
    print "---------------"
    print "Test case 7:"
    print "Find the shortest-path from Building 8 to 50 without going outdoors"
    bruteRaisedErr = 'No'
    dfsRaisedErr = 'No'
    try:
        bruteForceSearch(mitMap, '8', '50', LARGE_DIST, 0)
    except ValueError:
        bruteRaisedErr = 'Yes'
    
    try:
        directedDFS(mitMap, '8', '50', LARGE_DIST, 0)
    except ValueError:
        dfsRaisedErr = 'Yes'
    
    print "Expected: No such path! Should throw a value error."
    print "Did brute force search raise an error?", bruteRaisedErr
    print "Did DFS search raise an error?", dfsRaisedErr

    # Test case 8
    print "---------------"
    print "Test case 8:"
    print "Find the shortest-path from Building 10 to 32 without walking"
    print "more than 100 meters in total"
    bruteRaisedErr = 'No'
    dfsRaisedErr = 'No'
    try:
        bruteForceSearch(mitMap, '10', '32', 100, LARGE_DIST)
    except ValueError:
        bruteRaisedErr = 'Yes'
    
    try:
        directedDFS(mitMap, '10', '32', 100, LARGE_DIST)
    except ValueError:
        dfsRaisedErr = 'Yes'
    
    print "Expected: No such path! Should throw a value error."
    print "Did brute force search raise an error?", bruteRaisedErr
    print "Did DFS search raise an error?", dfsRaisedErr
