from graph_types.malla_graph import malla_graph
from graph_types.erdos_renyi_graph import erdos_renyi_graph
from graph_types.gilbert_graph import gilbert_graph
from graph_types.geografic_graph import geografic_graph
from graph_types.barabasi_albert_graph import barabasi_albert_graph
from graph_types.dorogovtsev_mendes_graph import dorogovtsev_mendes_graph

from utils.graphic_tree import graphic_tree
from utils.graphic_graph import graphic_graph


# region PROYECTO 1

# region GRAFO MALLA

# print("GRAFO MALLA")

# graph = malla_graph(m=2, n=50, path_to_save="../doc/50-nodos/")
# graph.show_graph()
# graph.save()

# graphic_graph(
#     "../doc/50-nodos/Grafo-Malla-No-Dirigido-n=50-m=2.dot",
#     "../doc/50-nodos/Grafo-Malla-No-Dirigido-n=50-m=2",
#     profile="mesh",
# )

# graph = malla_graph(m=2, n=200, path_to_save="../doc/200-nodos/")
# graph.show_graph()
# graph.save()

# graphic_graph(
#     "../doc/200-nodos/Grafo-Malla-No-Dirigido-n=200-m=2.dot",
#     "../doc/200-nodos/Grafo-Malla-No-Dirigido-n=200-m=2",
#     profile="mesh",
# )

# graph = malla_graph(m=2, n=500, path_to_save="../doc/500-nodos/")
# graph.show_graph()
# graph.save()

# graphic_graph(
#     "../doc/500-nodos/Grafo-Malla-No-Dirigido-n=500-m=2.dot",
#     "../doc/500-nodos/Grafo-Malla-No-Dirigido-n=500-m=2",
#     profile="mesh",
# )

# endregion


# region GRAFO ERDOS - RENYI

# print("\nGRAFO ERDOS - RENYI")

# graph = erdos_renyi_graph(m=150, n=50, path_to_save="../doc/50-nodos/")
# graph.show_graph()
# graph.save()

# graphic_graph(
#     "../doc/50-nodos/Grafo-Erdos-Renyi-No-Dirigido-n=50-m=150.dot",
#     "../doc/50-nodos/Grafo-Erdos-Renyi-No-Dirigido-n=50-m=150",
# )

# graph = erdos_renyi_graph(m=400, n=200, path_to_save="../doc/200-nodos/")
# graph.show_graph()
# graph.save()

# graphic_graph(
#     "../doc/200-nodos/Grafo-Erdos-Renyi-No-Dirigido-n=200-m=400.dot",
#     "../doc/200-nodos/Grafo-Erdos-Renyi-No-Dirigido-n=200-m=400",
# )

# graph = erdos_renyi_graph(m=900, n=500, path_to_save="../doc/500-nodos/")
# graph.show_graph()
# graph.save()

# graphic_graph(
#     "../doc/500-nodos/Grafo-Erdos-Renyi-No-Dirigido-n=500-m=900.dot",
#     "../doc/500-nodos/Grafo-Erdos-Renyi-No-Dirigido-n=500-m=900",
# )

# endregion


# region GRAFO GILBERT

# print("\nGRAFO GILBERT")

# graph = gilbert_graph(n=50, p=0.1, path_to_save="../doc/50-nodos/")
# graph.show_graph()
# graph.save()

# graphic_graph(
#     "../doc/50-nodos/Grafo-Gilbert-No-Dirigido-n=50-p=0.1.dot",
#     "../doc/50-nodos/Grafo-Gilbert-No-Dirigido-n=50-p=0.1",
# )

# graph = gilbert_graph(n=200, p=0.03, path_to_save="../doc/200-nodos/")
# graph.show_graph()
# graph.save()

# graphic_graph(
#     "../doc/200-nodos/Grafo-Gilbert-No-Dirigido-n=200-p=0.03.dot",
#     "../doc/200-nodos/Grafo-Gilbert-No-Dirigido-n=200-p=0.03",
# )

# graph = gilbert_graph(n=500, p=0.001, path_to_save="../doc/500-nodos/")
# graph.show_graph()
# graph.save()

# graphic_graph(
#     "../doc/500-nodos/Grafo-Gilbert-No-Dirigido-n=500-p=0.001.dot",
#     "../doc/500-nodos/Grafo-Gilbert-No-Dirigido-n=500-p=0.001",
# )

# endregion


# region GRAFO GEOGRÁFICO

# print("\nGRAFO GEOGRÁFICO")

# graph = geografic_graph(n=50, r=0.25, path_to_save="../doc/50-nodos/")
# graph.show_graph()
# graph.save()

# graphic_graph(
#     "../doc/50-nodos/Grafo-Geográfico-No-Dirigido-n=50-r=0.25.dot",
#     "../doc/50-nodos/Grafo-Geográfico-No-Dirigido-n=50-r=0.25",
# )

# graph = geografic_graph(n=200, r=0.13, path_to_save="../doc/200-nodos/")
# graph.show_graph()
# graph.save()

# graphic_graph(
#     "../doc/200-nodos/Grafo-Geográfico-No-Dirigido-n=200-r=0.13.dot",
#     "../doc/200-nodos/Grafo-Geográfico-No-Dirigido-n=200-r=0.13",
# )

# graph = geografic_graph(n=500, r=0.05, path_to_save="../doc/500-nodos/")
# graph.show_graph()
# graph.save()

# graphic_graph(
#     "../doc/500-nodos/Grafo-Geográfico-No-Dirigido-n=500-r=0.05.dot",
#     "../doc/500-nodos/Grafo-Geográfico-No-Dirigido-n=500-r=0.05",
# )

# endregion


# region GRAFO BARÁBASI - ALBERT

# print("\nGRAFO BARÁBASI - ALBERT")

# graph = barabasi_albert_graph(n=50, d=3, path_to_save="../doc/50-nodos/")
# graph.show_graph()
# graph.save()

# graphic_graph(
#     "../doc/50-nodos/Grafo-Barabási-Albert-No-Dirigido-n=50-d=3.dot",
#     "../doc/50-nodos/Grafo-Barabási-Albert-No-Dirigido-n=50-d=3",
# )

# graph = barabasi_albert_graph(n=200, d=4, path_to_save="../doc/200-nodos/")
# graph.show_graph()
# graph.save()

# graphic_graph(
#     "../doc/200-nodos/Grafo-Barabási-Albert-No-Dirigido-n=200-d=4.dot",
#     "../doc/200-nodos/Grafo-Barabási-Albert-No-Dirigido-n=200-d=4",
# )

# graph = barabasi_albert_graph(n=300, d=5, path_to_save="../doc/500-nodos/")
# graph.show_graph()
# graph.save()

# graphic_graph(
#     "../doc/500-nodos/Grafo-Barabási-Albert-No-Dirigido-n=300-d=5.dot",
#     "../doc/500-nodos/Grafo-Barabási-Albert-No-Dirigido-n=300-d=5",
# )

# endregion


# region GRAFO DOROGOVTSEV - MENDES

# print("\nGRAFO DOROGOVTSEV - MENDES")

# graph = dorogovtsev_mendes_graph(n=50, path_to_save="../doc/50-nodos/")
# graph.show_graph()
# graph.save()

# graphic_graph(
#     "../doc/50-nodos/Grafo-Dorogovtsev-Mendes-No-Dirigido-n=50.dot",
#     "../doc/50-nodos/Grafo-Dorogovtsev-Mendes-No-Dirigido-n=50",
# )

# graph = dorogovtsev_mendes_graph(n=200, path_to_save="../doc/200-nodos/")
# graph.show_graph()
# graph.save()

# graphic_graph(
#     "../doc/200-nodos/Grafo-Dorogovtsev-Mendes-No-Dirigido-n=200.dot",
#     "../doc/200-nodos/Grafo-Dorogovtsev-Mendes-No-Dirigido-n=200",
# )

# graph = dorogovtsev_mendes_graph(n=400, path_to_save="../doc/500-nodos/")
# graph.show_graph()
# graph.save()

# graphic_graph(
#     "../doc/500-nodos/Grafo-Dorogovtsev-Mendes-No-Dirigido-n=400.dot",
#     "../doc/500-nodos/Grafo-Dorogovtsev-Mendes-No-Dirigido-n=400",
# )

# endregion

# endregion


# region PROYECTO 2

# region GRAFO MALLA

# print("GRAFO MALLA")

# graph = malla_graph(m=2, n=30, path_to_save="../doc/30-nodos/")
# graph.show_graph()
# graph.save()
# graphic_graph(
#     "../doc/30-nodos/Grafo-Malla-No-Dirigido-n=30-m=2.dot",
#     "../doc/30-nodos/Grafo-Malla-No-Dirigido-n=30-m=2",
#     profile="mesh",
# )

# graph.load("../doc/30-nodos/Grafo-Malla-No-Dirigido-n=30-m=2.dot")

# tree = graph.bfs(
#     source=graph._nodes[0],
#     path_to_save="../doc/30-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/30-nodos/BFS-Grafo-Malla-No-Dirigido-n=30-m=2.dot",
#     "../doc/30-nodos/BFS-Grafo-Malla-No-Dirigido-n=30-m=2",
#     profile="mesh",
# )

# tree = graph.dfs_recursive(
#     source=graph._nodes[0],
#     path_to_save="../doc/30-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/30-nodos/DFS-Recursive-Grafo-Malla-No-Dirigido-n=30-m=2.dot",
#     "../doc/30-nodos/DFS-Recursive-Grafo-Malla-No-Dirigido-n=30-m=2",
#     profile="mesh",
# )

# tree = graph.dfs_iterative(
#     source=graph._nodes[0],
#     path_to_save="../doc/30-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/30-nodos/DFS-Iterative-Grafo-Malla-No-Dirigido-n=30-m=2.dot",
#     "../doc/30-nodos/DFS-Iterative-Grafo-Malla-No-Dirigido-n=30-m=2",
#     profile="mesh",
# )

# graph = malla_graph(m=2, n=100, path_to_save="../doc/100-nodos/")
# graph.show_graph()
# graph.save()
# graphic_graph(
#     "../doc/100-nodos/Grafo-Malla-No-Dirigido-n=100-m=2.dot",
#     "../doc/100-nodos/Grafo-Malla-No-Dirigido-n=100-m=2",
#     profile="mesh",
# )

# graph.load("../doc/100-nodos/Grafo-Malla-No-Dirigido-n=100-m=2.dot")

# tree = graph.bfs(
#     source=graph._nodes[0],
#     path_to_save="../doc/100-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/100-nodos/BFS-Grafo-Malla-No-Dirigido-n=100-m=2.dot",
#     "../doc/100-nodos/BFS-Grafo-Malla-No-Dirigido-n=100-m=2",
#     profile="mesh",
# )

# tree = graph.dfs_recursive(
#     source=graph._nodes[0],
#     path_to_save="../doc/100-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/100-nodos/DFS-Recursive-Grafo-Malla-No-Dirigido-n=100-m=2.dot",
#     "../doc/100-nodos/DFS-Recursive-Grafo-Malla-No-Dirigido-n=100-m=2",
#     profile="mesh",
# )

# tree = graph.dfs_iterative(
#     source=graph._nodes[0],
#     path_to_save="../doc/100-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/100-nodos/DFS-Iterative-Grafo-Malla-No-Dirigido-n=100-m=2.dot",
#     "../doc/100-nodos/DFS-Iterative-Grafo-Malla-No-Dirigido-n=100-m=2",
#     profile="mesh",
# )

# graph = malla_graph(m=1, n=500, path_to_save="../doc/500-nodos/")
# graph.show_graph()
# graph.save()
# graphic_graph(
#     "../doc/500-nodos/Grafo-Malla-No-Dirigido-n=500-m=1.dot",
#     "../doc/500-nodos/Grafo-Malla-No-Dirigido-n=500-m=1",
#     profile="mesh",
# )

# graph.load("../doc/500-nodos/Grafo-Malla-No-Dirigido-n=500-m=1.dot")

# tree = graph.bfs(
#     source=graph._nodes[0],
#     path_to_save="../doc/500-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/500-nodos/BFS-Grafo-Malla-No-Dirigido-n=500-m=1.dot",
#     "../doc/500-nodos/BFS-Grafo-Malla-No-Dirigido-n=500-m=1",
#     profile="mesh",
# )

# tree = graph.dfs_recursive(
#     source=graph._nodes[0],
#     path_to_save="../doc/500-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/500-nodos/DFS-Recursive-Grafo-Malla-No-Dirigido-n=500-m=1.dot",
#     "../doc/500-nodos/DFS-Recursive-Grafo-Malla-No-Dirigido-n=500-m=1",
#     profile="mesh",
# )

# tree = graph.dfs_iterative(
#     source=graph._nodes[0],
#     path_to_save="../doc/500-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/500-nodos/DFS-Iterative-Grafo-Malla-No-Dirigido-n=500-m=1.dot",
#     "../doc/500-nodos/DFS-Iterative-Grafo-Malla-No-Dirigido-n=500-m=1",
#     profile="mesh",
# )

# endregion


# region GRAFO ERDOS - RENYI

# print("GRAFO ERDOS - RENYI")

# graph = erdos_renyi_graph(m=150, n=30, path_to_save="../doc/30-nodos/")
# graph.show_graph()
# graph.save()
# graphic_graph(
#     "../doc/30-nodos/Grafo-Erdos-Renyi-No-Dirigido-n=30-m=150.dot",
#     "../doc/30-nodos/Grafo-Erdos-Renyi-No-Dirigido-n=30-m=150",
#     profile="mesh",
# )

# graph.load("../doc/30-nodos/Grafo-Erdos-Renyi-No-Dirigido-n=30-m=150.dot")

# tree = graph.bfs(
#     source=graph._nodes[0],
#     path_to_save="../doc/30-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/30-nodos/BFS-Grafo-Erdos-Renyi-No-Dirigido-n=30-m=150.dot",
#     "../doc/30-nodos/BFS-Grafo-Erdos-Renyi-No-Dirigido-n=30-m=150",
#     profile="mesh",
# )

# tree = graph.dfs_recursive(
#     source=graph._nodes[0],
#     path_to_save="../doc/30-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/30-nodos/DFS-Recursive-Grafo-Erdos-Renyi-No-Dirigido-n=30-m=150.dot",
#     "../doc/30-nodos/DFS-Recursive-Grafo-Erdos-Renyi-No-Dirigido-n=30-m=150",
#     profile="mesh",
# )

# tree = graph.dfs_iterative(
#     source=graph._nodes[0],
#     path_to_save="../doc/30-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/30-nodos/DFS-Iterative-Grafo-Erdos-Renyi-No-Dirigido-n=30-m=150.dot",
#     "../doc/30-nodos/DFS-Iterative-Grafo-Erdos-Renyi-No-Dirigido-n=30-m=150",
#     profile="mesh",
# )

# graph = erdos_renyi_graph(m=250, n=100, path_to_save="../doc/100-nodos/")
# graph.show_graph()
# graph.save()
# graphic_graph(
#     "../doc/100-nodos/Grafo-Erdos-Renyi-No-Dirigido-n=100-m=250.dot",
#     "../doc/100-nodos/Grafo-Erdos-Renyi-No-Dirigido-n=100-m=250",
#     profile="mesh",
# )

# graph.load("../doc/100-nodos/Grafo-Erdos-Renyi-No-Dirigido-n=100-m=250.dot")

# tree = graph.bfs(
#     source=graph._nodes[0],
#     path_to_save="../doc/100-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/100-nodos/BFS-Grafo-Erdos-Renyi-No-Dirigido-n=100-m=250.dot",
#     "../doc/100-nodos/BFS-Grafo-Erdos-Renyi-No-Dirigido-n=100-m=250",
#     profile="mesh",
# )

# tree = graph.dfs_recursive(
#     source=graph._nodes[0],
#     path_to_save="../doc/100-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/100-nodos/DFS-Recursive-Grafo-Erdos-Renyi-No-Dirigido-n=100-m=250.dot",
#     "../doc/100-nodos/DFS-Recursive-Grafo-Erdos-Renyi-No-Dirigido-n=100-m=250",
#     profile="mesh",
# )

# tree = graph.dfs_iterative(
#     source=graph._nodes[0],
#     path_to_save="../doc/100-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/100-nodos/DFS-Iterative-Grafo-Erdos-Renyi-No-Dirigido-n=100-m=250.dot",
#     "../doc/100-nodos/DFS-Iterative-Grafo-Erdos-Renyi-No-Dirigido-n=100-m=250",
#     profile="mesh",
# )

# graph = erdos_renyi_graph(m=750, n=500, path_to_save="../doc/500-nodos/")
# graph.show_graph()
# graph.save()
# graphic_graph(
#     "../doc/500-nodos/Grafo-Erdos-Renyi-No-Dirigido-n=500-m=750.dot",
#     "../doc/500-nodos/Grafo-Erdos-Renyi-No-Dirigido-n=500-m=750",
#     profile="mesh",
# )

# graph.load("../doc/500-nodos/Grafo-Erdos-Renyi-No-Dirigido-n=500-m=750.dot")

# tree = graph.bfs(
#     source=graph._nodes[0],
#     path_to_save="../doc/500-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/500-nodos/BFS-Grafo-Erdos-Renyi-No-Dirigido-n=500-m=750.dot",
#     "../doc/500-nodos/BFS-Grafo-Erdos-Renyi-No-Dirigido-n=500-m=750",
#     profile="mesh",
# )

# tree = graph.dfs_recursive(
#     source=graph._nodes[0],
#     path_to_save="../doc/500-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/500-nodos/DFS-Recursive-Grafo-Erdos-Renyi-No-Dirigido-n=500-m=750.dot",
#     "../doc/500-nodos/DFS-Recursive-Grafo-Erdos-Renyi-No-Dirigido-n=500-m=750",
#     profile="mesh",
# )

# tree = graph.dfs_iterative(
#     source=graph._nodes[0],
#     path_to_save="../doc/500-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/500-nodos/DFS-Iterative-Grafo-Erdos-Renyi-No-Dirigido-n=500-m=750.dot",
#     "../doc/500-nodos/DFS-Iterative-Grafo-Erdos-Renyi-No-Dirigido-n=500-m=750",
#     profile="mesh",
# )

# endregion


# region GRAFO GILBERT

# print("GRAFO GILBERT")

# graph = gilbert_graph(n=30, p=0.1, path_to_save="../doc/30-nodos/")
# graph.show_graph()
# graph.save()
# graphic_graph(
#     "../doc/30-nodos/Grafo-Gilbert-No-Dirigido-n=30-p=0.1.dot",
#     "../doc/30-nodos/Grafo-Gilbert-No-Dirigido-n=30-p=0.1",
#     profile="mesh",
# )

# graph.load("../doc/30-nodos/Grafo-Gilbert-No-Dirigido-n=30-p=0.1.dot")

# tree = graph.bfs(
#     source=graph._nodes[0],
#     path_to_save="../doc/30-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/30-nodos/BFS-Grafo-Gilbert-No-Dirigido-n=30-p=0.1.dot",
#     "../doc/30-nodos/BFS-Grafo-Gilbert-No-Dirigido-n=30-p=0.1",
#     profile="mesh",
# )

# tree = graph.dfs_recursive(
#     source=graph._nodes[0],
#     path_to_save="../doc/30-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/30-nodos/DFS-Recursive-Grafo-Gilbert-No-Dirigido-n=30-p=0.1.dot",
#     "../doc/30-nodos/DFS-Recursive-Grafo-Gilbert-No-Dirigido-n=30-p=0.1",
#     profile="mesh",
# )

# tree = graph.dfs_iterative(
#     source=graph._nodes[0],
#     path_to_save="../doc/30-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/30-nodos/DFS-Iterative-Grafo-Gilbert-No-Dirigido-n=30-p=0.1.dot",
#     "../doc/30-nodos/DFS-Iterative-Grafo-Gilbert-No-Dirigido-n=30-p=0.1",
#     profile="mesh",
# )

# graph = gilbert_graph(n=100, p=0.03, path_to_save="../doc/100-nodos/")
# graph.show_graph()
# graph.save()
# graphic_graph(
#     "../doc/100-nodos/Grafo-Gilbert-No-Dirigido-n=100-p=0.03.dot",
#     "../doc/100-nodos/Grafo-Gilbert-No-Dirigido-n=100-p=0.03",
#     profile="mesh",
# )

# graph.load("../doc/100-nodos/Grafo-Gilbert-No-Dirigido-n=100-p=0.03.dot")

# tree = graph.bfs(
#     source=graph._nodes[0],
#     path_to_save="../doc/100-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/100-nodos/BFS-Grafo-Gilbert-No-Dirigido-n=100-p=0.03.dot",
#     "../doc/100-nodos/BFS-Grafo-Gilbert-No-Dirigido-n=100-p=0.03",
#     profile="mesh",
# )

# tree = graph.dfs_recursive(
#     source=graph._nodes[0],
#     path_to_save="../doc/100-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/100-nodos/DFS-Recursive-Grafo-Gilbert-No-Dirigido-n=100-p=0.03.dot",
#     "../doc/100-nodos/DFS-Recursive-Grafo-Gilbert-No-Dirigido-n=100-p=0.03",
#     profile="mesh",
# )

# tree = graph.dfs_iterative(
#     source=graph._nodes[0],
#     path_to_save="../doc/100-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/100-nodos/DFS-Iterative-Grafo-Gilbert-No-Dirigido-n=100-p=0.03.dot",
#     "../doc/100-nodos/DFS-Iterative-Grafo-Gilbert-No-Dirigido-n=100-p=0.03",
#     profile="mesh",
# )

# graph = gilbert_graph(n=500, p=0.005, path_to_save="../doc/500-nodos/")
# graph.show_graph()
# graph.save()
# graphic_graph(
#     "../doc/500-nodos/Grafo-Gilbert-No-Dirigido-n=500-p=0.005.dot",
#     "../doc/500-nodos/Grafo-Gilbert-No-Dirigido-n=500-p=0.005",
#     profile="mesh",
# )

# graph.load("../doc/500-nodos/Grafo-Gilbert-No-Dirigido-n=500-p=0.005.dot")

# tree = graph.bfs(
#     source=graph._nodes[0],
#     path_to_save="../doc/500-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/500-nodos/BFS-Grafo-Gilbert-No-Dirigido-n=500-p=0.005.dot",
#     "../doc/500-nodos/BFS-Grafo-Gilbert-No-Dirigido-n=500-p=0.005",
#     profile="mesh",
# )

# tree = graph.dfs_recursive(
#     source=graph._nodes[0],
#     path_to_save="../doc/500-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/500-nodos/DFS-Recursive-Grafo-Gilbert-No-Dirigido-n=500-p=0.005.dot",
#     "../doc/500-nodos/DFS-Recursive-Grafo-Gilbert-No-Dirigido-n=500-p=0.005",
#     profile="mesh",
# )

# tree = graph.dfs_iterative(
#     source=graph._nodes[0],
#     path_to_save="../doc/500-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/500-nodos/DFS-Iterative-Grafo-Gilbert-No-Dirigido-n=500-p=0.005.dot",
#     "../doc/500-nodos/DFS-Iterative-Grafo-Gilbert-No-Dirigido-n=500-p=0.005",
#     profile="mesh",
# )

# endregion


# region GRAFO GEOGRÁFICO

# print("GRAFO GEOGRÁFICO")

# graph = geografic_graph(n=30, r=0.35, path_to_save="../doc/30-nodos/")
# graph.show_graph()
# graph.save()
# graphic_graph(
#     "../doc/30-nodos/Grafo-Geográfico-No-Dirigido-n=30-r=0.35.dot",
#     "../doc/30-nodos/Grafo-Geográfico-No-Dirigido-n=30-r=0.35",
#     profile="mesh",
# )

# graph.load("../doc/30-nodos/Grafo-Geográfico-No-Dirigido-n=30-r=0.35.dot")

# tree = graph.bfs(
#     source=graph._nodes[0],
#     path_to_save="../doc/30-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/30-nodos/BFS-Grafo-Geográfico-No-Dirigido-n=30-r=0.35.dot",
#     "../doc/30-nodos/BFS-Grafo-Geográfico-No-Dirigido-n=30-r=0.35",
#     profile="mesh",
# )

# tree = graph.dfs_recursive(
#     source=graph._nodes[0],
#     path_to_save="../doc/30-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/30-nodos/DFS-Recursive-Grafo-Geográfico-No-Dirigido-n=30-r=0.35.dot",
#     "../doc/30-nodos/DFS-Recursive-Grafo-Geográfico-No-Dirigido-n=30-r=0.35",
#     profile="mesh",
# )

# tree = graph.dfs_iterative(
#     source=graph._nodes[0],
#     path_to_save="../doc/30-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/30-nodos/DFS-Iterative-Grafo-Geográfico-No-Dirigido-n=30-r=0.35.dot",
#     "../doc/30-nodos/DFS-Iterative-Grafo-Geográfico-No-Dirigido-n=30-r=0.35",
#     profile="mesh",
# )

# graph = geografic_graph(n=100, r=0.25, path_to_save="../doc/100-nodos/")
# graph.show_graph()
# graph.save()
# graphic_graph(
#     "../doc/100-nodos/Grafo-Geográfico-No-Dirigido-n=100-r=0.25.dot",
#     "../doc/100-nodos/Grafo-Geográfico-No-Dirigido-n=100-r=0.25",
#     profile="mesh",
# )

# graph.load("../doc/100-nodos/Grafo-Geográfico-No-Dirigido-n=100-r=0.25.dot")

# tree = graph.bfs(
#     source=graph._nodes[0],
#     path_to_save="../doc/100-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/100-nodos/BFS-Grafo-Geográfico-No-Dirigido-n=100-r=0.25.dot",
#     "../doc/100-nodos/BFS-Grafo-Geográfico-No-Dirigido-n=100-r=0.25",
#     profile="mesh",
# )

# tree = graph.dfs_recursive(
#     source=graph._nodes[0],
#     path_to_save="../doc/100-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/100-nodos/DFS-Recursive-Grafo-Geográfico-No-Dirigido-n=100-r=0.25.dot",
#     "../doc/100-nodos/DFS-Recursive-Grafo-Geográfico-No-Dirigido-n=100-r=0.25",
#     profile="mesh",
# )

# tree = graph.dfs_iterative(
#     source=graph._nodes[0],
#     path_to_save="../doc/100-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/100-nodos/DFS-Iterative-Grafo-Geográfico-No-Dirigido-n=100-r=0.25.dot",
#     "../doc/100-nodos/DFS-Iterative-Grafo-Geográfico-No-Dirigido-n=100-r=0.25",
#     profile="mesh",
# )

# graph = geografic_graph(n=500, r=0.073, path_to_save="../doc/500-nodos/")
# graph.show_graph()
# graph.save()
# graphic_graph(
#     "../doc/500-nodos/Grafo-Geográfico-No-Dirigido-n=500-r=0.073.dot",
#     "../doc/500-nodos/Grafo-Geográfico-No-Dirigido-n=500-r=0.073",
#     profile="mesh",
# )

# graph.load("../doc/500-nodos/Grafo-Geográfico-No-Dirigido-n=500-r=0.073.dot")

# tree = graph.bfs(
#     source=graph._nodes[0],
#     path_to_save="../doc/500-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/500-nodos/BFS-Grafo-Geográfico-No-Dirigido-n=500-r=0.073.dot",
#     "../doc/500-nodos/BFS-Grafo-Geográfico-No-Dirigido-n=500-r=0.073",
#     profile="mesh",
# )

# tree = graph.dfs_recursive(
#     source=graph._nodes[0],
#     path_to_save="../doc/500-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/500-nodos/DFS-Recursive-Grafo-Geográfico-No-Dirigido-n=500-r=0.073.dot",
#     "../doc/500-nodos/DFS-Recursive-Grafo-Geográfico-No-Dirigido-n=500-r=0.073",
#     profile="mesh",
# )

# tree = graph.dfs_iterative(
#     source=graph._nodes[0],
#     path_to_save="../doc/500-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/500-nodos/DFS-Iterative-Grafo-Geográfico-No-Dirigido-n=500-r=0.073.dot",
#     "../doc/500-nodos/DFS-Iterative-Grafo-Geográfico-No-Dirigido-n=500-r=0.073",
#     profile="mesh",
# )

# endregion


# region GRAFO BARÁBASI - ALBERT

# print("GRAFO BARÁBASI - ALBERT")

# graph = barabasi_albert_graph(n=30, d=3, path_to_save="../doc/30-nodos/")
# graph.show_graph()
# graph.save()
# graphic_graph(
#     "../doc/30-nodos/Grafo-Barabási-Albert-No-Dirigido-n=30-d=3.dot",
#     "../doc/30-nodos/Grafo-Barabási-Albert-No-Dirigido-n=30-d=3",
#     profile="mesh",
# )

# graph.load("../doc/30-nodos/Grafo-Barabási-Albert-No-Dirigido-n=30-d=3.dot")

# tree = graph.bfs(
#     source=graph._nodes[0],
#     path_to_save="../doc/30-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/30-nodos/BFS-Grafo-Barabási-Albert-No-Dirigido-n=30-d=3.dot",
#     "../doc/30-nodos/BFS-Grafo-Barabási-Albert-No-Dirigido-n=30-d=3",
#     profile="mesh",
# )

# tree = graph.dfs_recursive(
#     source=graph._nodes[0],
#     path_to_save="../doc/30-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/30-nodos/DFS-Recursive-Grafo-Barabási-Albert-No-Dirigido-n=30-d=3.dot",
#     "../doc/30-nodos/DFS-Recursive-Grafo-Barabási-Albert-No-Dirigido-n=30-d=3",
#     profile="mesh",
# )

# tree = graph.dfs_iterative(
#     source=graph._nodes[0],
#     path_to_save="../doc/30-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/30-nodos/DFS-Iterative-Grafo-Barabási-Albert-No-Dirigido-n=30-d=3.dot",
#     "../doc/30-nodos/DFS-Iterative-Grafo-Barabási-Albert-No-Dirigido-n=30-d=3",
#     profile="mesh",
# )

# graph = barabasi_albert_graph(n=100, d=4, path_to_save="../doc/100-nodos/")
# graph.show_graph()
# graph.save()
# graphic_graph(
#     "../doc/100-nodos/Grafo-Barabási-Albert-No-Dirigido-n=100-d=4.dot",
#     "../doc/100-nodos/Grafo-Barabási-Albert-No-Dirigido-n=100-d=4",
#     profile="mesh",
# )

# graph.load("../doc/100-nodos/Grafo-Barabási-Albert-No-Dirigido-n=100-d=4.dot")

# tree = graph.bfs(
#     source=graph._nodes[0],
#     path_to_save="../doc/100-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/100-nodos/BFS-Grafo-Barabási-Albert-No-Dirigido-n=100-d=4.dot",
#     "../doc/100-nodos/BFS-Grafo-Barabási-Albert-No-Dirigido-n=100-d=4",
#     profile="mesh",
# )

# tree = graph.dfs_recursive(
#     source=graph._nodes[0],
#     path_to_save="../doc/100-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/100-nodos/DFS-Recursive-Grafo-Barabási-Albert-No-Dirigido-n=100-d=4.dot",
#     "../doc/100-nodos/DFS-Recursive-Grafo-Barabási-Albert-No-Dirigido-n=100-d=4",
#     profile="mesh",
# )

# tree = graph.dfs_iterative(
#     source=graph._nodes[0],
#     path_to_save="../doc/100-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/100-nodos/DFS-Iterative-Grafo-Barabási-Albert-No-Dirigido-n=100-d=4.dot",
#     "../doc/100-nodos/DFS-Iterative-Grafo-Barabási-Albert-No-Dirigido-n=100-d=4",
#     profile="mesh",
# )

# graph = barabasi_albert_graph(n=500, d=7, path_to_save="../doc/500-nodos/")
# graph.show_graph()
# graph.save()
# graphic_graph(
#     "../doc/500-nodos/Grafo-Barabási-Albert-No-Dirigido-n=500-d=7.dot",
#     "../doc/500-nodos/Grafo-Barabási-Albert-No-Dirigido-n=500-d=7",
#     profile="mesh",
# )

# graph.load("../doc/500-nodos/Grafo-Barabási-Albert-No-Dirigido-n=500-d=7.dot")

# tree = graph.bfs(
#     source=graph._nodes[0],
#     path_to_save="../doc/500-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/500-nodos/BFS-Grafo-Barabási-Albert-No-Dirigido-n=500-d=7.dot",
#     "../doc/500-nodos/BFS-Grafo-Barabási-Albert-No-Dirigido-n=500-d=7",
#     profile="mesh",
# )

# tree = graph.dfs_recursive(
#     source=graph._nodes[0],
#     path_to_save="../doc/500-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/500-nodos/DFS-Recursive-Grafo-Barabási-Albert-No-Dirigido-n=500-d=7.dot",
#     "../doc/500-nodos/DFS-Recursive-Grafo-Barabási-Albert-No-Dirigido-n=500-d=7",
#     profile="mesh",
# )

# tree = graph.dfs_iterative(
#     source=graph._nodes[0],
#     path_to_save="../doc/500-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/500-nodos/DFS-Iterative-Grafo-Barabási-Albert-No-Dirigido-n=500-d=7.dot",
#     "../doc/500-nodos/DFS-Iterative-Grafo-Barabási-Albert-No-Dirigido-n=500-d=7",
#     profile="mesh",
# )

# endregion


# region GRAFO DOROGOVTSEV - MENDES

# print("GRAFO DOROGOVTSEV - MENDES")

# graph = dorogovtsev_mendes_graph(n=30, path_to_save="../doc/30-nodos/")
# graph.show_graph()
# graph.save()
# graphic_graph(
#     "../doc/30-nodos/Grafo-Dorogovtsev-Mendes-No-Dirigido-n=30.dot",
#     "../doc/30-nodos/Grafo-Dorogovtsev-Mendes-No-Dirigido-n=30",
#     profile="mesh",
# )

# graph.load("../doc/30-nodos/Grafo-Dorogovtsev-Mendes-No-Dirigido-n=30.dot")

# tree = graph.bfs(
#     source=graph._nodes[0],
#     path_to_save="../doc/30-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/30-nodos/BFS-Grafo-Dorogovtsev-Mendes-No-Dirigido-n=30.dot",
#     "../doc/30-nodos/BFS-Grafo-Dorogovtsev-Mendes-No-Dirigido-n=30",
#     profile="mesh",
# )

# tree = graph.dfs_recursive(
#     source=graph._nodes[0],
#     path_to_save="../doc/30-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/30-nodos/DFS-Recursive-Grafo-Dorogovtsev-Mendes-No-Dirigido-n=30.dot",
#     "../doc/30-nodos/DFS-Recursive-Grafo-Dorogovtsev-Mendes-No-Dirigido-n=30",
#     profile="mesh",
# )

# tree = graph.dfs_iterative(
#     source=graph._nodes[0],
#     path_to_save="../doc/30-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/30-nodos/DFS-Iterative-Grafo-Dorogovtsev-Mendes-No-Dirigido-n=30.dot",
#     "../doc/30-nodos/DFS-Iterative-Grafo-Dorogovtsev-Mendes-No-Dirigido-n=30",
#     profile="mesh",
# )

# graph = dorogovtsev_mendes_graph(n=100, path_to_save="../doc/100-nodos/")
# graph.show_graph()
# graph.save()
# graphic_graph(
#     "../doc/100-nodos/Grafo-Dorogovtsev-Mendes-No-Dirigido-n=100.dot",
#     "../doc/100-nodos/Grafo-Dorogovtsev-Mendes-No-Dirigido-n=100",
#     profile="mesh",
# )

# graph.load("../doc/100-nodos/Grafo-Dorogovtsev-Mendes-No-Dirigido-n=100.dot")

# tree = graph.bfs(
#     source=graph._nodes[0],
#     path_to_save="../doc/100-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/100-nodos/BFS-Grafo-Dorogovtsev-Mendes-No-Dirigido-n=100.dot",
#     "../doc/100-nodos/BFS-Grafo-Dorogovtsev-Mendes-No-Dirigido-n=100",
#     profile="mesh",
# )

# tree = graph.dfs_recursive(
#     source=graph._nodes[0],
#     path_to_save="../doc/100-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/100-nodos/DFS-Recursive-Grafo-Dorogovtsev-Mendes-No-Dirigido-n=100.dot",
#     "../doc/100-nodos/DFS-Recursive-Grafo-Dorogovtsev-Mendes-No-Dirigido-n=100",
#     profile="mesh",
# )

# tree = graph.dfs_iterative(
#     source=graph._nodes[0],
#     path_to_save="../doc/100-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/100-nodos/DFS-Iterative-Grafo-Dorogovtsev-Mendes-No-Dirigido-n=100.dot",
#     "../doc/100-nodos/DFS-Iterative-Grafo-Dorogovtsev-Mendes-No-Dirigido-n=100",
#     profile="mesh",
# )

# graph = dorogovtsev_mendes_graph(n=500, path_to_save="../doc/500-nodos/")
# graph.show_graph()
# graph.save()
# graphic_graph(
#     "../doc/500-nodos/Grafo-Dorogovtsev-Mendes-No-Dirigido-n=500.dot",
#     "../doc/500-nodos/Grafo-Dorogovtsev-Mendes-No-Dirigido-n=500",
#     profile="mesh",
# )

# graph.load("../doc/500-nodos/Grafo-Dorogovtsev-Mendes-No-Dirigido-n=500.dot")

# tree = graph.bfs(
#     source=graph._nodes[0],
#     path_to_save="../doc/500-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/500-nodos/BFS-Grafo-Dorogovtsev-Mendes-No-Dirigido-n=500.dot",
#     "../doc/500-nodos/BFS-Grafo-Dorogovtsev-Mendes-No-Dirigido-n=500",
#     profile="mesh",
# )

# tree = graph.dfs_recursive(
#     source=graph._nodes[0],
#     path_to_save="../doc/500-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/500-nodos/DFS-Recursive-Grafo-Dorogovtsev-Mendes-No-Dirigido-n=500.dot",
#     "../doc/500-nodos/DFS-Recursive-Grafo-Dorogovtsev-Mendes-No-Dirigido-n=500",
#     profile="mesh",
# )

# tree = graph.dfs_iterative(
#     source=graph._nodes[0],
#     path_to_save="../doc/500-nodos/",
# )
# tree.show_graph()
# tree.save()
# graphic_graph(
#     "../doc/500-nodos/DFS-Iterative-Grafo-Dorogovtsev-Mendes-No-Dirigido-n=500.dot",
#     "../doc/500-nodos/DFS-Iterative-Grafo-Dorogovtsev-Mendes-No-Dirigido-n=500",
#     profile="mesh",
# )

# endregion

# endregion


# region PROYECTO 3

# region GRAFO MALLA

print("GRAFO MALLA")

graph = malla_graph(m=2, n=30, path_to_save="../doc/30-nodos/")
graph.show_graph()
graph.save()
graphic_graph(
    "../doc/30-nodos/Grafo-Malla-No-Dirigido-n=30-m=2.dot",
    "../doc/30-nodos/Grafo-Malla-No-Dirigido-n=30-m=2",
    profile="mesh",
)

graph.load("../doc/30-nodos/Grafo-Malla-No-Dirigido-n=30-m=2.dot")

graph.assign_weight()
tree = graph.dijkstra(source=graph._nodes[0])
tree.show_graph()
tree.save_with_labels_and_color(last=graph._nodes[0]._name)
graphic_tree(
    "../doc/30-nodos/Dijkstra-Grafo-Malla-No-Dirigido-n=30-m=2.gv",
    "../doc/30-nodos/Dijkstra-Grafo-Malla-No-Dirigido-n=30-m=2.png",
)

graph = malla_graph(m=2, n=200, path_to_save="../doc/200-nodos/")
graph.show_graph()
graph.save()
graphic_graph(
    "../doc/200-nodos/Grafo-Malla-No-Dirigido-n=200-m=2.dot",
    "../doc/200-nodos/Grafo-Malla-No-Dirigido-n=200-m=2",
    profile="mesh",
)

graph.load("../doc/200-nodos/Grafo-Malla-No-Dirigido-n=200-m=2.dot")

graph.assign_weight()
tree = graph.dijkstra(source=graph._nodes[0])
tree.show_graph()
tree.save_with_labels_and_color(last=graph._nodes[0]._name)
graphic_tree(
    "../doc/200-nodos/Dijkstra-Grafo-Malla-No-Dirigido-n=200-m=2.gv",
    "../doc/200-nodos/Dijkstra-Grafo-Malla-No-Dirigido-n=200-m=2.png",
)

# endregion


# region ERDOS - RENYI

print("GRAFO ERDOS - RENYI")

graph = erdos_renyi_graph(m=90, n=30, path_to_save="../doc/30-nodos/")
graph.show_graph()
graph.save()
graphic_graph(
    "../doc/30-nodos/Grafo-Erdos-Renyi-No-Dirigido-n=30-m=90.dot",
    "../doc/30-nodos/Grafo-Erdos-Renyi-No-Dirigido-n=30-m=90",
    profile="mesh",
)

graph.load("../doc/30-nodos/Grafo-Erdos-Renyi-No-Dirigido-n=30-m=90.dot")

graph.assign_weight()
tree = graph.dijkstra(source=graph._nodes[0])
tree.show_graph()
tree.save_with_labels_and_color(last=graph._nodes[0]._name)
graphic_tree(
    "../doc/30-nodos/Dijkstra-Grafo-Erdos-Renyi-No-Dirigido-n=30-m=90.gv",
    "../doc/30-nodos/Dijkstra-Grafo-Erdos-Renyi-No-Dirigido-n=30-m=90.png",
)

graph = erdos_renyi_graph(m=400, n=200, path_to_save="../doc/200-nodos/")
graph.show_graph()
graph.save()
graphic_graph(
    "../doc/200-nodos/Grafo-Erdos-Renyi-No-Dirigido-n=200-m=400.dot",
    "../doc/200-nodos/Grafo-Erdos-Renyi-No-Dirigido-n=200-m=400",
    profile="mesh",
)

graph.load("../doc/200-nodos/Grafo-Erdos-Renyi-No-Dirigido-n=200-m=400.dot")

graph.assign_weight()
tree = graph.dijkstra(source=graph._nodes[0])
tree.show_graph()
tree.save_with_labels_and_color(last=graph._nodes[0]._name)
graphic_tree(
    "../doc/200-nodos/Dijkstra-Grafo-Erdos-Renyi-No-Dirigido-n=200-m=400.gv",
    "../doc/200-nodos/Dijkstra-Grafo-Erdos-Renyi-No-Dirigido-n=200-m=400.png",
)

# endregion


# region GILBERT

print("GRAFO GILBERT")

graph = gilbert_graph(n=30, p=0.1, path_to_save="../doc/30-nodos/")
graph.show_graph()
graph.save()
graphic_graph(
    "../doc/30-nodos/Grafo-Gilbert-No-Dirigido-n=30-p=0.1.dot",
    "../doc/30-nodos/Grafo-Gilbert-No-Dirigido-n=30-p=0.1",
    profile="mesh",
)

graph.load("../doc/30-nodos/Grafo-Gilbert-No-Dirigido-n=30-p=0.1.dot")

graph.assign_weight()
tree = graph.dijkstra(source=graph._nodes[0])
tree.show_graph()
tree.save_with_labels_and_color(last=graph._nodes[0]._name)
graphic_tree(
    "../doc/30-nodos/Dijkstra-Grafo-Gilbert-No-Dirigido-n=30-p=0.1.gv",
    "../doc/30-nodos/Dijkstra-Grafo-Gilbert-No-Dirigido-n=30-p=0.1.png",
)

graph = gilbert_graph(n=200, p=0.03, path_to_save="../doc/200-nodos/")
graph.show_graph()
graph.save()
graphic_graph(
    "../doc/200-nodos/Grafo-Gilbert-No-Dirigido-n=200-p=0.03.dot",
    "../doc/200-nodos/Grafo-Gilbert-No-Dirigido-n=200-p=0.03",
    profile="mesh",
)

graph.load("../doc/200-nodos/Grafo-Gilbert-No-Dirigido-n=200-p=0.03.dot")

graph.assign_weight()
tree = graph.dijkstra(source=graph._nodes[0])
tree.show_graph()
tree.save_with_labels_and_color(last=graph._nodes[0]._name)
graphic_tree(
    "../doc/200-nodos/Dijkstra-Grafo-Gilbert-No-Dirigido-n=200-p=0.03.gv",
    "../doc/200-nodos/Dijkstra-Grafo-Gilbert-No-Dirigido-n=200-p=0.03.png",
)

# endregion


# region GEOGRÁFICO

print("GRAFO GEOGRÁFICO")

graph = geografic_graph(n=30, r=0.3, path_to_save="../doc/30-nodos/")
graph.show_graph()
graph.save()
graphic_graph(
    "../doc/30-nodos/Grafo-Geográfico-No-Dirigido-n=30-r=0.3.dot",
    "../doc/30-nodos/Grafo-Geográfico-No-Dirigido-n=30-r=0.3",
    profile="mesh",
)

graph.load("../doc/30-nodos/Grafo-Geográfico-No-Dirigido-n=30-r=0.3.dot")

graph.assign_weight()
tree = graph.dijkstra(source=graph._nodes[0])
tree.show_graph()
tree.save_with_labels_and_color(last=graph._nodes[0]._name)
graphic_tree(
    "../doc/30-nodos/Dijkstra-Grafo-Geográfico-No-Dirigido-n=30-r=0.3.gv",
    "../doc/30-nodos/Dijkstra-Grafo-Geográfico-No-Dirigido-n=30-r=0.3.png",
)

graph = geografic_graph(n=200, r=0.13, path_to_save="../doc/200-nodos/")
graph.show_graph()
graph.save()
graphic_graph(
    "../doc/200-nodos/Grafo-Geográfico-No-Dirigido-n=200-r=0.13.dot",
    "../doc/200-nodos/Grafo-Geográfico-No-Dirigido-n=200-r=0.13",
    profile="mesh",
)

graph.load("../doc/200-nodos/Grafo-Geográfico-No-Dirigido-n=200-r=0.13.dot")

graph.assign_weight()
tree = graph.dijkstra(source=graph._nodes[0])
tree.show_graph()
tree.save_with_labels_and_color(last=graph._nodes[0]._name)
graphic_tree(
    "../doc/200-nodos/Dijkstra-Grafo-Geográfico-No-Dirigido-n=200-r=0.13.gv",
    "../doc/200-nodos/Dijkstra-Grafo-Geográfico-No-Dirigido-n=200-r=0.13.png",
)

# endregion


# region BARÁBASI - ALBERT

print("GRAFO BARÁBASI - ALBERT")

graph = barabasi_albert_graph(n=30, d=3, path_to_save="../doc/30-nodos/")
graph.show_graph()
graph.save()
graphic_graph(
    "../doc/30-nodos/Grafo-Barabási-Albert-No-Dirigido-n=30-d=3.dot",
    "../doc/30-nodos/Grafo-Barabási-Albert-No-Dirigido-n=30-d=3",
    profile="mesh",
)

graph.load("../doc/30-nodos/Grafo-Barabási-Albert-No-Dirigido-n=30-d=3.dot")

graph.assign_weight()
tree = graph.dijkstra(source=graph._nodes[0])
tree.show_graph()
tree.save_with_labels_and_color(last=graph._nodes[0]._name)
graphic_tree(
    "../doc/30-nodos/Dijkstra-Grafo-Barabási-Albert-No-Dirigido-n=30-d=3.gv",
    "../doc/30-nodos/Dijkstra-Grafo-Barabási-Albert-No-Dirigido-n=30-d=3.png",
)

graph = barabasi_albert_graph(n=200, d=4, path_to_save="../doc/200-nodos/")
graph.show_graph()
graph.save()
graphic_graph(
    "../doc/200-nodos/Grafo-Barabási-Albert-No-Dirigido-n=200-d=4.dot",
    "../doc/200-nodos/Grafo-Barabási-Albert-No-Dirigido-n=200-d=4",
    profile="mesh",
)

graph.load("../doc/200-nodos/Grafo-Barabási-Albert-No-Dirigido-n=200-d=4.dot")

graph.assign_weight()
tree = graph.dijkstra(source=graph._nodes[0])
tree.show_graph()
tree.save_with_labels_and_color(last=graph._nodes[0]._name)
graphic_tree(
    "../doc/200-nodos/Dijkstra-Grafo-Barabási-Albert-No-Dirigido-n=200-d=4.gv",
    "../doc/200-nodos/Dijkstra-Grafo-Barabási-Albert-No-Dirigido-n=200-d=4.png",
)

# endregion


# region DOROGOVTSEV - MENDES

print("GRAFO DOROGOVTSEV - MENDES")

graph = dorogovtsev_mendes_graph(n=30, path_to_save="../doc/30-nodos/")
graph.show_graph()
graph.save()
graphic_graph(
    "../doc/30-nodos/Grafo-Dorogovtsev-Mendes-No-Dirigido-n=30.dot",
    "../doc/30-nodos/Grafo-Dorogovtsev-Mendes-No-Dirigido-n=30",
    profile="mesh",
)

graph.load("../doc/30-nodos/Grafo-Dorogovtsev-Mendes-No-Dirigido-n=30.dot")

graph.assign_weight()
tree = graph.dijkstra(source=graph._nodes[0])
tree.show_graph()
tree.save_with_labels_and_color(last=graph._nodes[0]._name)
graphic_tree(
    "../doc/30-nodos/Dijkstra-Grafo-Dorogovtsev-Mendes-No-Dirigido-n=30.gv",
    "../doc/30-nodos/Dijkstra-Grafo-Dorogovtsev-Mendes-No-Dirigido-n=30.png",
)

graph = dorogovtsev_mendes_graph(n=200, path_to_save="../doc/200-nodos/")
graph.show_graph()
graph.save()
graphic_graph(
    "../doc/200-nodos/Grafo-Dorogovtsev-Mendes-No-Dirigido-n=200.dot",
    "../doc/200-nodos/Grafo-Dorogovtsev-Mendes-No-Dirigido-n=200",
    profile="mesh",
)

graph.load("../doc/200-nodos/Grafo-Dorogovtsev-Mendes-No-Dirigido-n=200.dot")

graph.assign_weight()
tree = graph.dijkstra(source=graph._nodes[0])
tree.show_graph()
tree.save_with_labels_and_color(last=graph._nodes[0]._name)
graphic_tree(
    "../doc/200-nodos/Dijkstra-Grafo-Dorogovtsev-Mendes-No-Dirigido-n=200.gv",
    "../doc/200-nodos/Dijkstra-Grafo-Dorogovtsev-Mendes-No-Dirigido-n=200.png",
)

# endregion

# endregion
