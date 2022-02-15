import itertools
import sys

""" Constants used for reading the input files """
K_INDEX = 0
N_INDEX = 1
M_INDEX = 2
EDGES_OFFSET = 3

""" This is class is used for storing the nodes and neighbors """
class Node(object):
    def __init__(self, index):
        self.index = index
        self.neighbors = []

    def __repr__(self):
        return str(self.index)


"""" This method is used for reading from input file """
def parse_input_file():
    file_name = sys.argv[1]
    with open(file_name, 'r') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    k = int(lines[K_INDEX])  # k = Clique dimension searched in graph G
    N = int(lines[N_INDEX])  # N = Number of vertices in graph G (indexes from 1 to N)
    M = int(lines[M_INDEX])  # M = Number of edges in graph G

    edges = []  # Edges in graph G
    for i in range(M):
        vertices = lines[i + EDGES_OFFSET]
        curr_edges = [int(vertex) for vertex in vertices.split(' ') if vertex.strip()]
        edges.append(curr_edges)

    return k, N, M, edges


""" This method is used from deserializing """
def create_graph(N, edges):
    # Create nodes
    nodes = []
    for i in range(N):
        nodes.append(Node(i + 1))  # Index starts from 1

    # Set neighbors
    for u, v in edges:
        nodes[u - 1].neighbors.append(nodes[v - 1])  # Mark edge (u,v)
        nodes[v - 1].neighbors.append(nodes[u - 1])  # Mark edge (v,u)

    return nodes
