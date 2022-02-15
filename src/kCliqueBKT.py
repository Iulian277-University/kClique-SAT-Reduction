from common import *

""" 
    This method is used for checking if a given set of nodes 
    are forming a clique in a given graph G
"""
def is_clique(nodes, G):
    for u in nodes:
        for v in nodes:
            if u != v and v not in G[u.index - 1].neighbors:
                return False
    return True


""" This method is used for generating all combinations of nodes of length k """
def generate_all_subsets(k, G):
    # Generate all k-combinations
    subsets = list(itertools.combinations(G, k))
    subsets = [list(node) for node in subsets]  # Convert from list of tuples to list of lists

    # Check if a subset is forming a clique
    for subset in subsets:
        if (is_clique(subset, G)):
            return True

    return False


"""" This method is the entry point of the program """
def main():
    k, N, M, edges = parse_input_file()
    G = create_graph(N, edges)
    print(generate_all_subsets(k, G))


if __name__ == "__main__":
    main()