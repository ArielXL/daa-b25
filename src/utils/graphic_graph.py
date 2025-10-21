import os
import pydot
import graphviz


def graphic_graph(
    dot_path: str,
    output_basename: str = "salida",
    fmt: str = "png",
    engine: str | None = None,
    node_width: float = 0.05,
    edge_penwidth: float = 0.5,
    profile: str | None = None,
    seed: int | None = 42,
    maxiter_mesh: int = 1200,
) -> str:
    """
    Lee un fichero DOT, aplica estilo y renderiza con Graphviz.
    - profile="mesh": rápido y estable para mallas (recto, aristas rectas).
    - profile="organic": estilo por fuerzas para grafos generales.
    Devuelve la ruta del archivo generado (p.ej. 'salida.png').
    """
    graphs = pydot.graph_from_dot_file(dot_path)
    if not graphs:
        raise ValueError(f"No pude leer '{dot_path}' como DOT.")
    g = graphs[0]

    def _count_nodes(pg: pydot.Dot) -> int:
        return sum(
            1 for n in pg.get_nodes() if n.get_name() not in ("node", "edge", "graph")
        )

    n_nodes = _count_nodes(g)

    name_lower = (
        getattr(g, "get_name", lambda: "")() or os.path.basename(dot_path)
    ).lower()
    if profile is None:
        profile = "mesh" if "malla" in name_lower or "grid" in name_lower else "organic"

    if engine is None:
        if profile == "mesh":
            engine = "neato"
        else:
            engine = "neato" if (n_nodes and n_nodes < 100) else "sfdp"

    if profile == "mesh":
        graph_attrs = {
            "layout": engine,
            "mode": "KK",
            "overlap": "false",
            "splines": "false",
            "maxiter": str(maxiter_mesh),
            "pack": "true",
            "sep": "+0.05",
        }
        if seed is not None:
            graph_attrs["seed"] = str(seed)
    else:
        graph_attrs = {
            "layout": engine,
            "overlap": "false",
            "splines": "true",
            "sep": "+0.1",
            "bgcolor": "white",
        }
        if engine != "dot":
            graph_attrs.update(
                {
                    "K": "1.0",
                    "repulsiveforce": "2",
                }
            )
        graph_attrs["mode"] = (
            "ipsep" if engine == "neato" else graph_attrs.get("mode", "")
        )

    for k, v in graph_attrs.items():
        g.set(k, v)

    g.set_node_defaults(
        shape="point",
        width=str(node_width),
        fixedsize="true",
        style="filled",
        fillcolor="black",
        color="black",
    )
    g.set_edge_defaults(
        color="gray50",
        penwidth=str(edge_penwidth),
    )

    styled_dot = f"{output_basename}_styled.dot"
    g.write(styled_dot)

    src = graphviz.Source.from_file(styled_dot)
    src.format = fmt
    src.engine = engine
    out_path = src.render(filename=output_basename, cleanup=True)

    try:
        os.remove(styled_dot)
    except OSError:
        pass

    return out_path
