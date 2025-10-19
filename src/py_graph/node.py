import random


class Node:

    def __init__(self, name: str, is_geo: bool = False) -> None:
        """
        SUMMARY
        -------
        Esta clase representa un nodo en un grafo. Cada nodo tiene
        un nombre único y puede tener una lista de aristas que lo
        conectan con otros nodos. Si el grafo es geográfico, el
        nodo también tiene coordenadas X e Y.

        PARAMETERS
        ----------
        :param name: nombre del nodo
        :param is_geo: si es verdadero inicializa las cordenadas X y Y
        """
        self._name = name
        self._edges = []
        self.X = 0
        self.Y = 0
        if is_geo == True:
            self.X = random.random()
            self.Y = random.random()

    def __eq__(self, other) -> bool:
        """
        SUMMARY
        -------
        Este método compara dos nodos. Considera los nodos iguales
        si tienen el mismo nombre.

        PARAMETERS
        ----------
        :param other: otro nodo para comparar

        RETURNS
        -------
        :return: True si los nodos son iguales, False en caso
        contrario
        """
        if isinstance(other, Node):
            return (self._name == other._name) or (self._name == other._name)
        return False

    def deg(self) -> int:
        """
        SUMMARY
        -------
        Este método devuelve el grado del nodo, que es la cantidad
        de aristas que lo conectan con otros nodos.

        RETURNS
        -------
        :return: el grado del nodo
        """
        return len(self._edges)
