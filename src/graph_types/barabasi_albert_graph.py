import random

from py_graph.node import Node
from py_graph.edge import Edge
from py_graph.graph import Graph


def barabasi_albert_graph(
    n: int, d: int, path_to_save: str, is_directed: bool = False
) -> Graph:
    """
    SUMMARY
    -------
    Genera un grafo aleatorio utilizando el modelo Barabasi-Albert.

    PARAMETERS
    ----------
    n : int
        Número de nodos (> 0).
    d : int
        Grado máximo esperado por cada nodo (> 1).
    path_to_save : str
        Ruta para guardar el grafo.
    is_directed : bool, optional
        El grafo es dirigido? (por defecto es False).

    RETURNS
    -------
    Graph
        Grafo generado.
    """
    print(f"\nGrafo Barabási - Albert para n = {n} y d = {d}\n")

    str_directed = "Dirigido" if is_directed else "No-Dirigido"
    graph = Graph(
        f"Grafo-Barabási-Albert-{str_directed}-n={str(n)}-d={str(d)}",
        path_to_save,
        is_directed=is_directed,
    )

    for i in range(d):
        node = Node(f"N-{str(i)}")
        graph.add_node(node)

    # Conecto los primeros d nodos

    for i in range(d):
        for j in range(d):
            source_node = graph._nodes[i]
            dest_node = graph._nodes[j]
            if i != j and isinstance(source_node, Node) and isinstance(dest_node, Node):
                edge1 = Edge(source_node, dest_node)
                edge2 = Edge(dest_node, source_node)
                if is_directed and not graph.exist_edge(edge1):
                    source_node._edges.append(edge1)
                elif (
                    not is_directed
                    and not graph.exist_edge(edge1)
                    and not graph.exist_edge(edge2)
                ):
                    source_node._edges.append(edge1)
                    dest_node._edges.append(edge2)

    i = d - 1  # Ya están creados los d primeros nodos (0, 1, 2, ..., d-1)
    while i < n:
        graph_copy = graph._nodes.copy()
        random.shuffle(graph_copy)
        node = Node(f"N-{str(i)}")
        graph.add_node(node)
        for dest_node in graph_copy:
            if isinstance(dest_node, Node) and node != dest_node:
                if dest_node.deg() < d:
                    volada = random.random()
                    degree = dest_node.deg()
                    p = 1 - degree / d
                    if volada < p:
                        edge1 = Edge(node, dest_node)
                        edge2 = Edge(dest_node, node)
                        if is_directed and not graph.exist_edge(edge1):
                            source_node._edges.append(edge1)
                        elif (
                            not is_directed
                            and not graph.exist_edge(edge1)
                            and not graph.exist_edge(edge2)
                        ):
                            source_node._edges.append(edge1)
                            dest_node._edges.append(edge2)
        i += 1

    return graph
