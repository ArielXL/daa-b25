class Edge:

    def __init__(self, source_node, destination_node, weight=0):
        """
        SUMMARY
        -------
        Esta clase representa una arista en un grafo, conectando
        dos nodos. Se define por su nodo origen, nodo destino y
        un peso opcional. Si el grafo es no dirigido, la arista
        se considera bidireccional. Por lo tanto, una arista de
        A a B es equivalente a una arista de B a A.

        PARAMETERS
        ----------
        :param source_node: nodo origen de la arista
        :param destination_node: nodo destino de la arista
        :param weight: peso de la arista
        """
        self._source_node = source_node
        self._destination_node = destination_node
        self._weight = weight

    def __eq__(self, other) -> bool:
        """
        SUMMARY
        -------
        Este método compara dos aristas. Considera las aristas
        iguales si conectan los mismos nodos, independientemente
        del orden.

        PARAMETERS
        ----------
        :param other: otra arista para comparar

        RETURNS
        -------
        :return: True si las aristas son iguales, False en caso
        contrario
        """
        if isinstance(other, Edge):
            return (
                self._source_node == other._source_node
                and self._destination_node == other._destination_node
            ) or (
                self._source_node == other._source_node
                and self._destination_node == other._destination_node
            )
        return False

    def __hash__(self):
        """
        SUMMARY
        -------
        Este método implementa hash para que las aristas puedan
        ser utilizadas en sets o como claves de diccionario.

        RETURNS
        -------
        :return: valor hash de la arista
        """
        return hash(
            (
                min(self._source_node, self._destination_node),
                max(self._source_node, self._destination_node),
            )
        )
