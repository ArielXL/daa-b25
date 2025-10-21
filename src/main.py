from graph_types.malla_graph import malla_graph
from graph_types.erdos_renyi_graph import erdos_renyi_graph
from graph_types.gilbert_graph import gilbert_graph
from graph_types.geografic_graph import geografic_graph
from graph_types.barabasi_albert_graph import barabasi_albert_graph
from graph_types.dorogovtsev_mendes_graph import dorogovtsev_mendes_graph

from utils.graphic_graph import graphic_graph


print("GRAFO MALLA")

graph = malla_graph(m=2, n=50, path_to_save="../doc/50-nodos/")
graph.show_graph()
graph.save()

graphic_graph(
    "../doc/50-nodos/Grafo-Malla-No-Dirigido-n=50-m=2.dot",
    "../doc/50-nodos/Grafo-Malla-No-Dirigido-n=50-m=2",
    profile="mesh",
)

graph = malla_graph(m=2, n=200, path_to_save="../doc/200-nodos/")
graph.show_graph()
graph.save()

graphic_graph(
    "../doc/200-nodos/Grafo-Malla-No-Dirigido-n=200-m=2.dot",
    "../doc/200-nodos/Grafo-Malla-No-Dirigido-n=200-m=2",
    profile="mesh",
)

graph = malla_graph(m=2, n=500, path_to_save="../doc/500-nodos/")
graph.show_graph()
graph.save()

graphic_graph(
    "../doc/500-nodos/Grafo-Malla-No-Dirigido-n=500-m=2.dot",
    "../doc/500-nodos/Grafo-Malla-No-Dirigido-n=500-m=2",
    profile="mesh",
)


print("\nGRAFO ERDOS - RENYI")

graph = erdos_renyi_graph(m=150, n=50, path_to_save="../doc/50-nodos/")
graph.show_graph()
graph.save()

graphic_graph(
    "../doc/50-nodos/Grafo-Erdos-Renyi-No-Dirigido-n=50-m=150.dot",
    "../doc/50-nodos/Grafo-Erdos-Renyi-No-Dirigido-n=50-m=150",
)

graph = erdos_renyi_graph(m=400, n=200, path_to_save="../doc/200-nodos/")
graph.show_graph()
graph.save()

graphic_graph(
    "../doc/200-nodos/Grafo-Erdos-Renyi-No-Dirigido-n=200-m=400.dot",
    "../doc/200-nodos/Grafo-Erdos-Renyi-No-Dirigido-n=200-m=400",
)

graph = erdos_renyi_graph(m=900, n=500, path_to_save="../doc/500-nodos/")
graph.show_graph()
graph.save()

graphic_graph(
    "../doc/500-nodos/Grafo-Erdos-Renyi-No-Dirigido-n=500-m=900.dot",
    "../doc/500-nodos/Grafo-Erdos-Renyi-No-Dirigido-n=500-m=900",
)


print("\nGRAFO GILBERT")

graph = gilbert_graph(n=50, p=0.1, path_to_save="../doc/50-nodos/")
graph.show_graph()
graph.save()

graphic_graph(
    "../doc/50-nodos/Grafo-Gilbert-No-Dirigido-n=50-p=0.1.dot",
    "../doc/50-nodos/Grafo-Gilbert-No-Dirigido-n=50-p=0.1",
)

graph = gilbert_graph(n=200, p=0.03, path_to_save="../doc/200-nodos/")
graph.show_graph()
graph.save()

graphic_graph(
    "../doc/200-nodos/Grafo-Gilbert-No-Dirigido-n=200-p=0.03.dot",
    "../doc/200-nodos/Grafo-Gilbert-No-Dirigido-n=200-p=0.03",
)

graph = gilbert_graph(n=500, p=0.001, path_to_save="../doc/500-nodos/")
graph.show_graph()
graph.save()

graphic_graph(
    "../doc/500-nodos/Grafo-Gilbert-No-Dirigido-n=500-p=0.001.dot",
    "../doc/500-nodos/Grafo-Gilbert-No-Dirigido-n=500-p=0.001",
)


print("\nGRAFO GEOGRÁFICO")

graph = geografic_graph(n=50, r=0.25, path_to_save="../doc/50-nodos/")
graph.show_graph()
graph.save()

graphic_graph(
    "../doc/50-nodos/Grafo-Geográfico-No-Dirigido-n=50-r=0.25.dot",
    "../doc/50-nodos/Grafo-Geográfico-No-Dirigido-n=50-r=0.25",
)

graph = geografic_graph(n=200, r=0.13, path_to_save="../doc/200-nodos/")
graph.show_graph()
graph.save()

graphic_graph(
    "../doc/200-nodos/Grafo-Geográfico-No-Dirigido-n=200-r=0.13.dot",
    "../doc/200-nodos/Grafo-Geográfico-No-Dirigido-n=200-r=0.13",
)

graph = geografic_graph(n=500, r=0.05, path_to_save="../doc/500-nodos/")
graph.show_graph()
graph.save()

graphic_graph(
    "../doc/500-nodos/Grafo-Geográfico-No-Dirigido-n=500-r=0.05.dot",
    "../doc/500-nodos/Grafo-Geográfico-No-Dirigido-n=500-r=0.05",
)


print("\nGRAFO BARABASI - ALBERT")

graph = barabasi_albert_graph(n=50, d=3, path_to_save="../doc/50-nodos/")
graph.show_graph()
graph.save()

graphic_graph(
    "../doc/50-nodos/Grafo-Barabási-Albert-No-Dirigido-n=50-d=3.dot",
    "../doc/50-nodos/Grafo-Barabási-Albert-No-Dirigido-n=50-d=3",
)

graph = barabasi_albert_graph(n=200, d=4, path_to_save="../doc/200-nodos/")
graph.show_graph()
graph.save()

graphic_graph(
    "../doc/200-nodos/Grafo-Barabási-Albert-No-Dirigido-n=200-d=4.dot",
    "../doc/200-nodos/Grafo-Barabási-Albert-No-Dirigido-n=200-d=4",
)

graph = barabasi_albert_graph(n=300, d=5, path_to_save="../doc/500-nodos/")
graph.show_graph()
graph.save()

graphic_graph(
    "../doc/500-nodos/Grafo-Barabási-Albert-No-Dirigido-n=300-d=5.dot",
    "../doc/500-nodos/Grafo-Barabási-Albert-No-Dirigido-n=300-d=5",
)


print("\nGRAFO DOROGOVTSEV - MENDES")

graph = dorogovtsev_mendes_graph(n=50, path_to_save="../doc/50-nodos/")
graph.show_graph()
graph.save()

graphic_graph(
    "../doc/50-nodos/Grafo-Dorogovtsev-Mendes-No-Dirigido-n=50.dot",
    "../doc/50-nodos/Grafo-Dorogovtsev-Mendes-No-Dirigido-n=50",
)

graph = dorogovtsev_mendes_graph(n=200, path_to_save="../doc/200-nodos/")
graph.show_graph()
graph.save()

graphic_graph(
    "../doc/200-nodos/Grafo-Dorogovtsev-Mendes-No-Dirigido-n=200.dot",
    "../doc/200-nodos/Grafo-Dorogovtsev-Mendes-No-Dirigido-n=200",
)

graph = dorogovtsev_mendes_graph(n=400, path_to_save="../doc/500-nodos/")
graph.show_graph()
graph.save()

graphic_graph(
    "../doc/500-nodos/Grafo-Dorogovtsev-Mendes-No-Dirigido-n=400.dot",
    "../doc/500-nodos/Grafo-Dorogovtsev-Mendes-No-Dirigido-n=400",
)
