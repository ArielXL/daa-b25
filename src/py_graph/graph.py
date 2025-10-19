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

    def add_node(self, node_name: str) -> None:
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

    def find_node(self, node_name: str) -> bool:
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
