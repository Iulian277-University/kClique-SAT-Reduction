from common import *

def intersection(list1, list2):
    return [node for node in list1 if node in list2]

# Bron–Kerbosch-Algorithm (without pivoting)
max_clique_dim = 0
def find_cliques(potential_clique=[], remaining_nodes=[], skip_nodes=[]):
    global max_clique_dim

    if (len(remaining_nodes) == 0 and len(skip_nodes) == 0):
        max_clique_dim = max(max_clique_dim, len(potential_clique))
        return

    for node in remaining_nodes:
        # Try adding the node to the current potential_clique to see if we can make it work.
        new_potential_clique = potential_clique + [node]
        new_remaining_nodes = intersection(remaining_nodes, node.neighbors)
        new_skip_list = intersection(skip_nodes, node.neighbors)
        find_cliques(new_potential_clique, new_remaining_nodes, new_skip_list)

        # We're done considering this node. If there was a way to form a clique with it, we
        # already discovered its maximal clique in the recursive call above. So, go ahead
        # and remove it from the list of remaining nodes and add it to the skip list.
        remaining_nodes.remove(node)
        skip_nodes.append(node)


def main():
    k, N, M, edges = parse_input_file()
    G = create_graph(N, edges)

    find_cliques(remaining_nodes=G)
    if (max_clique_dim >= k):
        print("True")
    else:
        print("False")


if __name__ == "__main__":
    main()
