from rich.console import Console
from rich.table import Column, Table

console = Console()

table = Table(show_header=True, header_style="bold magenta")
table.add_column("Característica")
table.add_column("Lista")
table.add_column("Array")
table.add_column("Tupla")
table.add_column("Conjunto (Set)")

table.add_row(
    "Definicion",
    "Una colección de elementos ordenados y modificables",
    "Un conjunto de elementos homogéneos ordenados y modificables",
    "Una colección de elementos ordenados e inmutables",
    "Una colección de elementos únicos e inmutables",
)

table.add_row(
    "Sintaxis",
    "mi_lista = [1, 2, 3]",
    "mi_array = np.array([1, 2, 3])",
    "mi_tupla = (1, 2, 3)",
    "mi_set = {1, 2, 3}",
)

table.add_row(
    "Indices",
    "Sí",
    "Sí",
    "Sí",
    "No",
)

table.add_row(
    "Modificable",
    "Sí",
    "Sí",
    "No",
    "Sí",
)

table.add_row(
    "Homogeneidad",
    "No",
    "Sí",
    "No",
    "No",
)

table.add_row(
    "Tamaño fijo",
    "No",
    "Sí",
    "Sí",
    "No",
)

table.add_row(
    "Únicos",
    "No",
    "No",
    "No",
    "Sí",
)

table.add_row(
    "Iterables",
    "Sí",
    "Sí",
    "Sí",
    "Sí",
)

console.print(table)