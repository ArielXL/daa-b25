import heapq
import random

from py_graph.node import Node
from py_graph.edge import Edge


class Graph:

    def __init__(
        self,
        name: str,
        path_to_save: str,
        is_directed: bool = False,
        is_geo: bool = False,
    ) -> None:
        """
        SUMMARY
        -------
        Esta clase representa un grafo, que es una estructura de
        datos compuesta por nodos y aristas. Permite la creación,
        modificación y eliminación de nodos y aristas, así como
        la búsqueda de estos elementos.

        PARAMETERS
        ----------
        :param name: nombre del grafo
        :param path_to_save: ruta donde se guardará el grafo
        :param is_directed: si es verdadero el grafo es dirigido
        :param is_geo: si es verdadero el grafo es geográfico
        """
        self._name = name
        self._path_to_save = path_to_save
        self._nodes = []
        self._edges = []
        self._is_directed = is_directed
        self._is_geo = is_geo

    def add_node_name(self, node_name: str) -> None:
        """
        SUMMARY
        -------
        Este método agrega un nuevo nodo al grafo por nombre. Si
        el grafo es geográfico, se le pide al nodo que inicialice
        las coordenadas X y Y.

        PARAMETERS
        ----------
        :param node_name: nombre del nodo a crear
        """
        if not self._is_geo:
            new_node = Node(node_name)
            self._nodes.append(new_node)
        elif self._is_geo:
            new_node = Node(node_name, self._is_geo)
            self._nodes.append(new_node)

    def add_node(self, new_node: Node) -> None:
        """
        SUMMARY
        -------
        Agrega un nuevo nodo al grafo dando por parámetro el nodo
        a añadir.

        PARAMETERS
        ----------
        :param new_node: nodo a añadir al grafo
        """
        self._nodes.append(new_node)

    def remove_node(self, node: Node) -> None:
        """
        SUMMARY
        -------
        Elimina un nodo del grafo.

        PARAMETERS
        ----------
        :param node: nodo a eliminar
        """
        self._nodes.remove(node)

    def find_node_name(self, node_name: str) -> bool:
        """
        SUMMARY
        -------
        Busca un nodo por su nombre.

        PARAMETERS
        ----------
        :param node_name: nombre del nodo a buscar

        RETURNS
        -------
        :return: True si el nodo es encontrado, False en caso contrario
        """
        for node in self._nodes:
            if isinstance(node, Node):
                if node._name == node_name:
                    return True
        return False

    def find_node(self, node: Node) -> bool:
        """
        SUMMARY
        -------
        Busca un nodo dado, si le encuentra retorna verdadero sino
        falso

        PARAMETERS
        ----------
        :param node: nodo a buscar

        RETURNS
        -------
        :return: True si el nodo es encontrado, False en caso
        contrario
        """
        for n in self._nodes:
            if isinstance(node, Node):
                if n == node:
                    return True
        return False

    def add_edge(self, edge: Edge) -> bool:
        """
        SUMMARY
        -------
        Agrega una arista al grafo. Retorna verdadero si fue
        añadida sino falso

        PARAMETERS
        ----------
        :param edge: arista a añadir

        RETURNS
        -------
        :return: True si la arista fue añadida, False en caso
        contrario
        """
        if (
            isinstance(edge, Edge)
            and (
                isinstance(edge._source_node, Node)
                and isinstance(edge._destination_node, Node)
            )
            and self.find_node(edge._source_node)
            and self.find_node(edge._destination_node)
        ):
            edge._source_node._edges.append(edge)
            self._edges.append(edge)
            return True
        return False

    def find_edge(self, edge: Edge) -> Node | None:
        """
        SUMMARY
        -------
        Busca una arista dada. Si lo encuentra retorna el nodo
        origen sino retorna None

        PARAMETERS
        ----------
        :param edge: arista a buscar

        RETURNS
        -------
        :return: el nodo origen si la arista es encontrada, None
        en caso contrario
        """
        for node in self._nodes:
            if isinstance(node, Node):
                for e in node._edges:
                    if isinstance(e, Edge):
                        if e == edge:
                            return node
        return None

    def exist_edge(self, edge: Edge) -> bool:
        """
        SUMMARY
        -------
        Combrueba si existe una arista en el grafo. Retorna
        verdadero si la encuentra sino falso.

        PARAMETERS
        ----------
        :param edge: arista a encontrar.

        RETURNS
        -------
        :return: True si la arista es encontrada, False en caso
        contrario
        """
        for node in self._nodes:
            if isinstance(node, Node):
                for e in node._edges:
                    if isinstance(e, Edge):
                        if e == edge:
                            return True
        return False

    def remove_edge(self, edge: Edge) -> bool:
        """
        SUMMARY
        -------
        Elimina una arista del grafo. Retorna verdadero si la
        elimina sino retorna falso.

        PARAMETERS
        ----------
        :param edge: arista a eliminar.

        RETURNS
        -------
        :return: True si la arista fue eliminada, False en caso
        contrario
        """
        if isinstance(edge, Edge):
            node = self.find_edge(edge)
            if isinstance(node, Node):
                node._edges.remove(edge)
                return True
        return False

    def save(self) -> None:
        """
        SUMMARY
        -------
        Exporta el grafo en formato GraphViz (.gv) usando el nombre
        del grafo como nombre del archivo.

        PARAMETERS
        ----------
        :param graph: El grafo a exportar.

        RETURNS
        -------
        :return: None
        """
        filename = f"{self._path_to_save}{self._name}.dot"

        with open(filename, "w") as file:
            if self._is_directed:
                file.write("digraph G {\n")
                conector = " -> "
            else:
                file.write("graph G {\n")
                conector = " -- "

            for node in self._nodes:
                if isinstance(node, Node):
                    file.write(f'    "{node._name}";\n')

            exported_edges = set()

            for node in self._nodes:
                if isinstance(node, Node):
                    for edge in node._edges:
                        if isinstance(edge, Edge):
                            source_node = edge._source_node
                            destination_node = edge._destination_node
                            if isinstance(source_node, Node) and isinstance(
                                destination_node, Node
                            ):
                                if not self._is_directed:
                                    if (
                                        destination_node._name,
                                        source_node._name,
                                    ) in exported_edges:
                                        continue
                                    exported_edges.add(
                                        (source_node._name, destination_node._name)
                                    )

                                file.write(
                                    f'    "{source_node._name}"{conector}"{destination_node._name}";\n'
                                )

            file.write("}\n")

        print(f"\nGrafo exportado a {filename} en formato GraphViz.")

    def show_graph(self) -> None:
        """
        SUMMARY
        -------
        Muestra el grafo en la consola.
        """
        for node in self._nodes:
            if isinstance(node, Node):
                print(f"Nodo: {node._name}")
                for edge in node._edges:
                    if (
                        isinstance(edge, Edge)
                        and isinstance(edge._source_node, Node)
                        and isinstance(edge._destination_node, Node)
                    ):
                        print(
                            f"Arista: {edge._source_node._name}-{edge._destination_node._name}"
                        )

    def get_node(self, node_name: str) -> Node | None:
        """
        SUMMARY
        -------
        Devuelve un nodo por su nombre.

        PARAMETERS
        ----------
        :param node_name: nombre del nodo a buscar

        RETURNS
        -------
        :return: El nodo encontrado o None si no se encuentra
        """
        for node in self._nodes:
            if isinstance(node, Node):
                if node._name == node_name:
                    return node
        return None

    def load(self, filename: str) -> None:
        """
        SUMMARY
        -------
        Carga un grafo desde un archivo en formato GraphViz.

        PARAMETERS
        ----------
        :param filename: nombre del archivo a cargar
        """
        self.load_nodes(filename)
        self.load_edges(filename)
        print(
            f"\nGrafo cargado desde {filename} en formato GraphViz a Grafo con nombre {self._name}.\n"
        )

    def load_edges(self, filename: str) -> None:
        """
        SUMMARY
        -------
        Lee el archivo gv y carga las aristas.

        PARAMETERS
        ----------
        :param filename: nombre del archivo a cargar
        """
        with open(filename) as file:
            for line in file:
                if "--" in line or "->" in line:
                    if "--" in line:
                        self._is_directed = False
                        clean_line = line.replace('"', "").replace(";", "").strip()
                        edge = clean_line.split("--")
                        source_node = self.get_node(edge[0].strip())
                        dest_node = self.get_node(edge[1].strip())
                        self.add_edge(Edge(source_node, dest_node))
                        self.add_edge(Edge(dest_node, source_node))
                    elif "->" in line:
                        self._is_directed = True
                        clean_line = line.replace('"', "").replace(";", "").strip()
                        edge = clean_line.split("->")
                        source_node = self.get_node(edge[0].strip())
                        dest_node = self.get_node(edge[1].strip())
                        self.add_edge(Edge(source_node, dest_node))
        file.close()

    def load_nodes(self, filename: str) -> None:
        """
        SUMMARY
        -------
        Lee el archivo gv y carga los nodos.

        PARAMETERS
        ----------
        :param filename: nombre del archivo a cargar
        """
        nodes = []
        with open(filename) as file:
            for line in file:
                if ";" in line and "--" not in line and "->" not in line:
                    clean_line = line.replace('"', "").replace(";", "").strip()
                    nodes.append(Node(clean_line))
        file.close()
        self._nodes = nodes

    def bfs(self, source: Node, path_to_save: str) -> "Graph":
        """
        SUMMARY
        -------
        Realiza la búsqueda a lo ancho en el grafo a partir del
        nodo dado y devuelve el árbol generado.

        PARAMETERS
        ----------
        :param source: nodo a tomar como raíz
        :param path_to_save: ruta donde se guardará el árbol generado

        RETURNS
        -------
        :return: árbol
        """
        tree = Graph(
            name=f"BFS-{self._name}",
            path_to_save=path_to_save,
            is_directed=self._is_directed,
        )

        nodes_tree, edges_tree, visited, current_layer = set(), set(), set(), set()
        nodes_tree.add(Node(source._name))
        visited.add(source)
        current_layer.add(source)

        stop = False

        while stop == False:
            errors = 0
            count_rec_edges = 0
            next_layer = set()

            for node in current_layer:
                if isinstance(node, Node):
                    for edge in node._edges:
                        count_rec_edges += 1
                        if (
                            isinstance(edge, Edge)
                            and edge._destination_node not in visited
                        ):
                            visited.add(edge._destination_node)
                            source_node, dest_node = Node(
                                edge._source_node._name
                            ), Node(edge._destination_node._name)

                            edge1, edge2 = Edge(source_node, dest_node), Edge(
                                dest_node, source_node
                            )
                            edge1._source_node._edges.append(edge1)
                            edge2._source_node._edges.append(edge2)

                            nodes_tree.add(dest_node)
                            next_layer.add(edge._destination_node)
                            edges_tree.add(edge1)
                        else:
                            errors += 1

            current_layer = next_layer

            if errors == count_rec_edges:
                stop = True

        tree._nodes = list(nodes_tree)
        tree._edges = list(edges_tree)

        return tree

    def dfs_recursive(self, source: Node, path_to_save: str) -> "Graph":
        """
        SUMMARY
        -------
        Realiza la búsqueda en profundidad de manera recursiva en el
        grafo a partir del nodo dado y devuelve el árbol generado.

        PARAMETERS
        ----------
        :param source: nodo a tomar como raíz

        RETURNS
        -------
        :return: árbol
        """
        tree = Graph(
            name=f"DFS-Recursive-{self._name}",
            path_to_save=path_to_save,
            is_directed=self._is_directed,
        )
        nodes_tree, edges_tree, visited = set(), set(), set()
        visited.add(source)

        if isinstance(source, Node):
            for edge in source._edges:
                dest_node = edge._destination_node
                if isinstance(dest_node, Node) and dest_node not in visited:
                    node1, node2 = Node(edge._source_node._name), Node(
                        edge._destination_node._name
                    )

                    edge1, edge2 = Edge(node1, node2), Edge(node2, node1)
                    edge1._source_node._edges.append(edge1)
                    edge2._source_node._edges.append(edge2)

                    nodes_tree.add(node2)
                    edges_tree.add(edge1)

                    nodes, edges = self.dfs_call(dest_node, visited)

                    nodes_tree.update(nodes)
                    edges_tree.update(edges)

        tree._nodes = list(nodes_tree)
        tree._edges = list(edges_tree)

        return tree

    def dfs_call(self, source: Node, visited: set) -> tuple[set, set]:
        """
        SUMMARY
        -------
        Función auxiliar para la búsqueda en profundidad recursiva.

        PARAMETERS
        ----------
        :param source: nodo a tomar como raíz
        :param visited: conjunto de nodos visitados

        RETURNS
        -------
        :return: Tupla -> nodes_tree: nodos del subárbol
                          edges_tree: aristas del subárbol
        """
        nodes_tree, edges_tree = set(), set()

        if isinstance(source, Node):
            visited.add(source)
            for edge in source._edges:
                dest_node = edge._destination_node
                if isinstance(dest_node, Node) and dest_node not in visited:
                    node1, node2 = Node(edge._source_node._name), Node(
                        edge._destination_node._name
                    )

                    edge1, edge2 = Edge(node1, node2), Edge(node2, node1)
                    edge1._source_node._edges.append(edge1)
                    edge2._source_node._edges.append(edge2)

                    nodes_tree.add(node2)
                    edges_tree.add(edge1)

                    nodes, edges = self.dfs_call(dest_node, visited)

                    nodes_tree.update(nodes)
                    edges_tree.update(edges)

        return nodes_tree, edges_tree

    def dfs_iterative(self, source: Node, path_to_save: str) -> "Graph":
        """
        SUMMARY
        -------
        Realiza la búsqueda en profundidad de manera iterativa en el
        grafo a partir del nodo dado y devuelve el árbol generado.

        PARAMETERS
        ----------
        :param source: nodo a tomar como raíz

        RETURNS
        -------
        :return: árbol
        """
        tree = Graph(
            name=f"DFS-Iterative-{self._name}",
            path_to_save=path_to_save,
            is_directed=self._is_directed,
        )
        nodes_tree, edges_tree, visited = set(), set(), set()
        stack = [source]

        while stack:
            node = stack.pop()
            if isinstance(node, Node) and node not in visited:
                visited.add(node)
                for edge in node._edges:
                    if isinstance(edge, Edge) and edge not in edges_tree:
                        node1, node2 = Node(edge._source_node._name), Node(
                            edge._destination_node._name
                        )

                        edge1, edge2 = Edge(node1, node2), Edge(node2, node1)
                        edge1._source_node._edges.append(edge1)
                        edge2._source_node._edges.append(edge2)

                        nodes_tree.add(node2)
                        stack.append(edge._destination_node)

        tree._nodes = list(nodes_tree)
        tree._edges = list(edges_tree)

        return tree

    def assign_weight(self) -> None:
        """
        SUMMARY
        -------
        Asigna un peso aleatorio a cada arista del grafo.
        """
        for node in self._nodes:
            if isinstance(node, Node):
                for edge in node._edges:
                    if (
                        isinstance(edge, Edge)
                        and isinstance(edge._source_node, Node)
                        and isinstance(edge._destination_node, Node)
                    ):
                        edge._weight = random.random() * 100

    def save_with_labels_and_color(self, path=set(), last: str = "") -> None:
        """
        SUMMARY
        -------
        Exporta el grafo en formato GraphViz (.gv), resaltando nodos
        específicos y coloreando un camino dado.

        PARAMETERS
        ----------
        :param path: conjunto de nombres de nodos que forman el camino a resaltar
        :param last: nombre del nodo a resaltar

        RETURNS
        -------
        :return: None
        """
        filename = f"{self._path_to_save}{self._name}.gv"

        with open(filename, "w") as file:
            if self._is_directed:
                file.write("digraph G {\n")
                conector = " -> "
            else:
                file.write("graph G {\n")
                conector = " -- "

            for node in self._nodes:
                if isinstance(node, Node):
                    if node._name == last:
                        file.write(
                            f'    "{node._name}" [label="{node._name}",color=red, fontcolor=red, style=filled, fillcolor=red];\n'
                        )
                    else:
                        file.write(f'    "{node._name}";\n')

            exported_edges = set()

            for node in self._nodes:
                if isinstance(node, Node):
                    for edges in node._edges:
                        if isinstance(edges, Edge):
                            source_node = edges._source_node
                            dest_node = edges._destination_node
                            if isinstance(source_node, Node) and isinstance(
                                dest_node, Node
                            ):
                                if not self._is_directed:
                                    if (
                                        dest_node._name,
                                        source_node._name,
                                    ) in exported_edges:
                                        continue
                                    exported_edges.add(
                                        (source_node._name, dest_node._name)
                                    )

                                if node._name in path:
                                    file.write(
                                        f'    "{source_node._name}"{conector}"{dest_node._name}" [color=red, penwidth=2, weight=2];\n'
                                    )
                                else:
                                    file.write(
                                        f'    "{source_node._name}"{conector}"{dest_node._name}" [color=black, penwidth=2, weight=2];\n'
                                    )

            file.write("}\n")

        print(
            f"\nGrafo exportado a {filename} con etiquetas y camino resaltado en formato GraphViz.\n"
        )

    def dijkstra(self, source: Node) -> "Graph":
        """
        SUMMARY
        -------
        Realiza el algoritmo de Dijkstra en el grafo a partir del nodo dado y devuelve el árbol generado.

        PARAMETERS
        ----------
        :param source: nodo a tomar como raíz

        RETURNS
        -------
        :return: árbol generado a partir del algoritmo de Dijkstra
        """
        tree = Graph(
            name=f"Dijkstra-{self._name}",
            path_to_save=self._path_to_save,
            is_directed=self._is_directed,
        )

        dist, predecessor, visited, heap = {}, {}, set(), []

        for nodo in self._nodes:
            dist[nodo] = 99999999999
        dist[source] = 0
        heapq.heappush(heap, (0, source))

        while heap:
            current_dist, current_node = heapq.heappop(heap)

            if dist[current_node] == 99999999999:
                break

            if isinstance(current_node, Node):
                for edges in current_node._edges:
                    if isinstance(edges, Edge):
                        poss_dist = current_dist + edges._weight
                        if poss_dist < dist[edges._destination_node]:
                            dist[edges._destination_node] = poss_dist
                            predecessor[edges._destination_node] = current_node
                            heapq.heappush(heap, (poss_dist, edges._destination_node))

            visited.add(current_node)

        nodes_tree, edges_tree = set(), set()
        nodes_tree.add(Node(source._name))

        for pred in predecessor.keys():
            source_node, dest_node = Node(predecessor[pred]._name), Node(
                f"{pred._name}({str(dist[pred])})"
            )
            edge1, edge2 = Edge(source_node, dest_node), Edge(dest_node, source_node)

            edge1._source_node._edges.append(edge1)
            edge2._source_node._edges.append(edge2)

            if source_node._name != source._name:
                source_node._name = (
                    f"{source_node._name}({str(dist[predecessor[pred]])})"
                )
            nodes_tree.add(dest_node)
            edges_tree.add(edge1)

        tree._nodes = list(nodes_tree)
        tree._edges = list(edges_tree)

        return tree
