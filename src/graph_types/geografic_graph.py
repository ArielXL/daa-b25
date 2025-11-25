import math

from py_graph.node import Node
from py_graph.edge import Edge
from py_graph.graph import Graph


def geografic_graph(
    n: int, r: float, path_to_save: str, is_directed: bool = False
) -> Graph:
    """
    SUMMARY
    -------
    Genera un grafo aleatorio utilizando el modelo geográfico simple.

    PARAMETERS
    ----------
    n : int
        Número de nodos (> 0).
    r : float
        Distancia máxima para crear un nodo (0, 1).
    path_to_save : str
        Ruta para guardar el grafo.
    is_directed : bool, optional
        El grafo es dirigido? (por defecto es False).

    RETURNS
    -------
    Graph
        Grafo generado.
    """
    print(f"\nGrafo Geográfico para n = {n} y r = {r}\n")

    str_directed = "Dirigido" if is_directed else "No-Dirigido"
    graph = Graph(
        f"Grafo-Geográfico-{str_directed}-n={str(n)}-r={str(r)}",
        path_to_save,
        is_directed=is_directed,
    )

    for i in range(n):
        node = Node(f"N-{str(i)}", is_geo=True)
        graph.add_node(node)

    for node in graph._nodes:
        i = 1
        while i < n:
            node_dest = graph._nodes[i]
            if (
                isinstance(node, Node)
                and isinstance(node_dest, Node)
                and node != node_dest
            ):
                dist = math.dist([node.X, node.Y], [node_dest.X, node_dest.Y])
                if dist <= r:
                    edge1 = Edge(node, node_dest)
                    edge2 = Edge(node_dest, node)
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
