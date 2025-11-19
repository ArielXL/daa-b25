import graphviz

from pathlib import Path


def graphic_tree(input_gv: str | Path, output_img: str | Path):
    """
    SUMMARY
    -------
    Esta función se encarga de renderizar un archivo de grafo en formato
    .gv o .dot y guardar la imagen resultante en la ruta especificada,
    respetando los estilos definidos en el archivo de entrada.

    PARAMETERS
    ----------
    input_gv : str | Path
        Ruta del archivo .gv o .dot de entrada.
    output_img : str | Path
        Ruta de salida donde se guardará la imagen.

    RETURNS
    -------
    Path
        Ruta absoluta de la imagen generada.
    """

    gv_path = Path(input_gv).resolve()
    out_path = Path(output_img).resolve()

    if not gv_path.exists():
        raise FileNotFoundError(f"No se encontró el fichero: {gv_path}")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    fmt = out_path.suffix.lstrip(".").lower() or "png"

    src = graphviz.Source.from_file(str(gv_path))
    binary = src.pipe(format=fmt)
    out_path.write_bytes(binary)

    return out_path
