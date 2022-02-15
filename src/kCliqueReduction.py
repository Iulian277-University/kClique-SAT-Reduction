from common import *


""" Constraint 1 """
def each_slot_taken(k, N):
    constraint = ""
    for j in range(1, k + 1):
        constraint += "("
        for i in range(1, N + 1):
            constraint += f"x{i}{j}"
            if i < N:
                constraint += " V "
        constraint += ")"
        if j < k:
            constraint += " ^ "

    return constraint


""" Constraint 2 """
def each_slot_only_one_true(k, N):
    constraint = ""
    for j in range(1, k + 1):
        for i in range(1, N + 1):
            for h in range(i + 1, N + 1):
                constraint += f"(~x{i}{j} V ~x{h}{j}) ^ "

    return constraint[:-3]


""" Constraint 3 """
def each_node_only_one_slot(k, N):
    constraint = ""
    for i in range(1, N + 1):
        for j in range(1, k + 1):
            for h in range(j + 1, k + 1):
                constraint += f"(~x{i}{j} V ~x{i}{h}) ^ "

    return constraint[:-3]


def generate_all_edges(N):
    all_edges = []
    for u in range(1, N + 1):
        for v in range(u + 1, N + 1):
            all_edges.append([u, v])

    return all_edges


def generate_complement_edges(N, edges):
    all_edges = generate_all_edges(N)
    complement_edges = []
    for u, v in all_edges:
        if not edges.__contains__([u, v]) and not edges.__contains__([v, u]):
            complement_edges.append([u, v])

    return complement_edges


""" Constraint 4 """
def any_two_nodes_from_clique_connected(k, complement_edges):
    constraint = ""
    if len(complement_edges) == 0:
        return constraint

    for idx, node in enumerate(complement_edges):
        u, v = node
        for i in range(1, k + 1):
            for j in range(1, k + 1):
                constraint += f"(~x{u}{i} V ~x{v}{j})"
                if j < k:
                    constraint += " ^ "
            if i < k:
                constraint += " ^ "
        if idx < len(complement_edges) - 1:
            constraint += " ^ "

    return constraint


""" x_ij = "node i is on slot j" """
def main():
    k, N, M, edges = parse_input_file()
    G = create_graph(N, edges)

    # Slots constraints
    constraint_1 = each_slot_taken(k, N)
    constraint_2 = each_slot_only_one_true(k, N)
    constraint_3 = each_node_only_one_slot(k, N)

    # Clique constraints
    complement_edges = generate_complement_edges(N, edges)
    constraint_4 = any_two_nodes_from_clique_connected(k, complement_edges)

    formula = ""
    if len(constraint_4) == 0:
        formula = constraint_1 + " ^ " + constraint_2 + " ^ " + constraint_3
    else:
        formula = constraint_1 + " ^ " + constraint_2 + " ^ " + constraint_3 + " ^ " + constraint_4
    print(formula)


if __name__ == "__main__":
    main()