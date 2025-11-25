import random

from py_graph.edge import Edge
from py_graph.node import Node
from py_graph.graph import Graph


def dorogovtsev_mendes_graph(n: int, path_to_save: str, is_directed: bool = False):
    """
    SUMMARY
    -------
    Genera grafo aleatorio con el modelo Dorogovtsev - Mendes.


    PARAMETERS
    ----------
    n : int
        Número de nodos (debe ser ≥ 3).
    path_to_save : str
        Ruta donde se guardará el grafo generado.
    is_directed : bool, optional
        Indica si el grafo es dirigido (por defecto es False).

    RETURNS
    -------
    Graph
        El grafo generado.
    """
    print(f"\nGrafo Dorogovtsev - Mendes para n = {n}\n")

    str_directed = "Dirigido" if is_directed else "No-Dirigido"
    graph = Graph(
        f"Grafo-Dorogovtsev-Mendes-{str_directed}-n={str(n)}",
        path_to_save,
        is_directed=is_directed,
    )

    for i in range(n):
        node = Node(f"N-{str(i)}")
        graph.add_node(node)

    for i in range(3):
        for j in range(3):
            source_node = graph._nodes[i]
            dest_node = graph._nodes[j]
            if (
                source_node != dest_node
                and isinstance(source_node, Node)
                and isinstance(dest_node, Node)
            ):
                edge1 = Edge(source_node, dest_node)
                edge2 = Edge(dest_node, source_node)
                if is_directed and not graph.exist_edge(edge1):
                    graph.add_edge(edge1)
                elif (
                    not is_directed
                    and not graph.exist_edge(edge1)
                    and not graph.exist_edge(edge2)
                ):
                    graph.add_edge(edge1)
                    graph.add_edge(edge2)

    for i in range(3, n):
        source_node = graph._nodes[i]
        count_edges = len(graph._edges)
        rand = random.randrange(0, count_edges)
        edge = graph._edges[rand]

        if isinstance(edge, Edge) and isinstance(source_node, Node):
            for node in [edge._source_node, edge._destination_node]:
                edge1 = Edge(source_node, node)
                edge2 = Edge(node, source_node)
                if is_directed and not graph.exist_edge(edge1):
                    graph.add_edge(edge1)
                elif (
                    not is_directed
                    and not graph.exist_edge(edge1)
                    and not graph.exist_edge(edge2)
                ):
                    graph.add_edge(edge1)
                    graph.add_edge(edge2)

    return graph
