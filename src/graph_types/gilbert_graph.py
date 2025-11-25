import random

from py_graph.node import Node
from py_graph.edge import Edge
from py_graph.graph import Graph


def gilbert_graph(
    n: int, p: float, path_to_save: str, is_directed: bool = False
) -> Graph:
    """
    SUMMARY
    -------
    Genera un grafo aleatorio utilizando el modelo de Gilbert.

    PARAMETERS
    ----------
    n : int
        Número de nodos (> 0).
    p : float
        Probabilidad de crear una arista (0, 1).
    path_to_save : str
        Ruta donde se guardará el grafo.
    is_directed : bool, optional
        Indica si el grafo es dirigido (por defecto es False).

    RETURNS
    -------
    Graph
        El grafo generado.
    """
    print(f"\nGrafo Gilbert para n = {n} y p = {p}\n")

    str_directed = "Dirigido" if is_directed else "No-Dirigido"
    graph = Graph(
        f"Grafo-Gilbert-{str_directed}-n={str(n)}-p={str(p)}",
        path_to_save,
        is_directed=is_directed,
    )

    for i in range(n):
        nodo = Node(f"N-{str(i)}")
        graph.add_node(nodo)

    for node in graph._nodes:
        i = 0
        if isinstance(node, Node):
            while i < n:
                num_rand = random.randrange(0, n)
                rand = random.random()
                dest_node = graph._nodes[num_rand]
                if isinstance(dest_node, Node) and node != dest_node and rand <= p:
                    edge1 = Edge(node, dest_node)
                    edge2 = Edge(dest_node, node)
                    if is_directed and graph.exist_edge(edge1) == False:
                        node._edges.append(edge1)
                    elif (
                        not is_directed
                        and not graph.exist_edge(edge1)
                        and not graph.exist_edge(edge2)
                    ):
                        node._edges.append(edge1)
                i += 1

    return graph
