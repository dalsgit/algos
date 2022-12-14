class Graph:
  def __init__(self, num_nodes, edges) -> None:
      self.data = [[] for _ in range(num_nodes)]
      self.num_nodes = num_nodes
      self.edges = edges
      for e1, e2 in edges:
        self.data[e1].append(e2)
        self.data[e2].append(e1)
  
  def remove(self, edge):
    e1, e2 = edge
    self.data[e1].remove(e2)
    self.data[e2].remove(e1)

  def add(self, edge):
    e1, e2 = edge
    self.data[e1].append(e2)
    self.data[e2].append(e1)

  def __repr__(self) -> str:
      return "\n".join("{} -> {}".format(idx, an) for idx, an in enumerate(self.data))

  def __str__(self) -> str:
     return self.__repr__()

  def am(self):
    am = [[0 for _ in range(self.num_nodes)] for _ in range(self.num_nodes)]
    for e1, e2 in self.edges:
        am[e1][e2] = 1
        am[e2][e1] = 1 
    return am

  def bfs(self, start):
    from queue import SimpleQueue
    queue = SimpleQueue()
    visited = [0] * self.num_nodes
    queue.put(start)
    while not queue.empty():
      item = queue.get()
      visited[item] = 1
      print(item)
      for neighbor in self.data[item]:
        if visited[neighbor] == 0:
          queue.put(neighbor)

num_nodes1 = 5
#0 -- 1 -- 2
#|    |  \ |
#| -- 4 -- 3
edges1 = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (1, 4), (1, 3)]
num_nodes1, len(edges1)
g = Graph(num_nodes1, edges1)
#print(g)
#g.bfs(3)

