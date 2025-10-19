from py_graph.node import Node
from py_graph.edge import Edge
from py_graph.graph import Graph


def malla_graph(m: int, n: int, path_to_save: str, is_directed: bool = False) -> Graph:
    """
    SUMMARY
    -------
    Esta función genera un grafo de malla de tamaño m x n.

    PARAMETERS
    ----------
    m : int
        Número de columnas (> 1).
    n : int
        Número de filas (> 1).
    path_to_save : str
        Ruta donde se guardará el grafo.
    is_directed : bool, optional
        Indica si el grafo es dirigido (por defecto es False).

    RETURNS
    -------
    Graph
        El grafo de malla generado.
    """
    print(f"\nGrafo Malla para m = {m} y n = {n}\n")

    str_directed = "Dirigido" if is_directed else "No-Dirigido"
    graph = Graph(
        f"Grafo-Malla-{str_directed}-n={str(n)}-m={str(m)}",
        path_to_save,
        is_directed=is_directed,
    )

    nodes_graph = []

    for i in range(m):
        nodes = []
        for j in range(n):
            node = Node(f"N{i}-{j}")
            nodes.append(node)
            graph.add_node(node)

        nodes_graph.append(nodes)

    for i in range(m):
        for j in range(n):
            if (i + 1) < m:
                nnode = nodes_graph[i + 1][j]
                cnode = nodes_graph[i][j]
                if isinstance(cnode, Node) and isinstance(nnode, Node):
                    cnode._edges.append(Edge(cnode, nnode))
            if (j + 1) < n:
                nnode = nodes_graph[i][j + 1]
                cnode = nodes_graph[i][j]
                if isinstance(cnode, Node) and isinstance(nnode, Node):
                    cnode._edges.append(Edge(cnode, nnode))

    return graph
