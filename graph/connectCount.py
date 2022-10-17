from graph import Graph
def connectCount(graph):
    visited = {}
    for node in graph:
        exploreDFS(graph, visited, node)

def exploreDFS(graph, visited, node):
    if(visited.get(node)): return False
    print(node)
    visited[node] = True
    for neighbor in graph[node]:
        exploreDFS(graph, visited, neighbor)
    return True

#    1       
#    0 - 8   2 - 3
#    5 - |   4 - |

g = {  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]}
print(g.keys())
connectCount(g)
