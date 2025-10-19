import random

from py_graph.node import Node
from py_graph.edge import Edge
from py_graph.graph import Graph


def erdos_renyi_graph(
    m: int, n: int, path_to_save: str, is_directed: bool = False
) -> Graph:
    """
    SUMMARY
    -------
    Genera grafo aleatorio con el modelo Erdos-Renyi.

    PARAMETERS
    ----------
    m : int
        Número de aristas (>= n-1).
    n : int
        Número de nodos (> 0).
    path_to_save : str
        Ruta donde se guardará el grafo.
    is_directed : bool, optional
        Indica si el grafo es dirigido (por defecto es False).

    RETURNS
    -------
    Graph
        El grafo generado.
    """
    print(f"\nGrafo Erdos - Renyi para m = {m} y n = {n}\n")

    str_directed = "Dirigido" if is_directed else "No-Dirigido"
    graph = Graph(
        f"Grafo-Erdos-Renyi-{str_directed}-n={str(n)}-m={str(m)}",
        path_to_save,
        is_directed=is_directed,
    )

    for i in range(n):
        node = Node(f"N-{i}")
        graph.add_node(node)

    count_edges = 0

    while count_edges < m:
        rand1 = random.randrange(0, n)
        rand2 = random.randrange(0, n)
        if rand1 != rand2:
            node_source = graph._nodes[rand1]
            node_dest = graph._nodes[rand2]
            if isinstance(node_source, Node) and isinstance(node_dest, Node):
                if is_directed:
                    edge = Edge(node_source, node_dest)
                    if not graph.exist_edge(edge):
                        node_source._edges.append(edge)
                        count_edges += 1
                else:
                    edge1 = Edge(node_source, node_dest)
                    edge2 = Edge(node_dest, node_source)
                    if not graph.exist_edge(edge1) and not graph.exist_edge(edge2):
                        node_source._edges.append(edge1)
                        node_dest._edges.append(edge2)
                        count_edges += 1
    return graph
