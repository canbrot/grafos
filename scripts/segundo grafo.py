import networkx as nx
import matplotlib.pyplot as plt

# Crear grafo no dirigido
G = nx.Graph()

# Datos de cómics con rating
comics_raw = {
    "Annihilation (2006)": 9.2,
    "Annihilation: Conquest (2007)": 8.4,
    "War of Kings (2009)": 8.5,
    "Realm of Kings (2009)": 6.7,
    "The Thanos Imperative (2010)": 8.2
}

# Crear versiones con label de rating
comics_labeled = {f"{k}\nRating: {v}": v for k, v in comics_raw.items()}
comics_nodes = list(comics_labeled.keys())

# Escritores y dibujantes
escritores = [
    "Keith Giffen",
    "Michael Hoskin",
    "Dan Abnett",
    "Andy Lanning"
]

dibujantes = [
    "Gabriele Dell'Otto",
    "Aleksi Briclot",
    "Frank Cho",
    "Clint Langley"
]

# Agregar nodos
G.add_nodes_from(comics_nodes)
G.add_nodes_from(escritores)
G.add_nodes_from(dibujantes)

# Mapa auxiliar para hacer las conexiones
comic_map = {
    "Annihilation (2006)": f"Annihilation (2006)\nRating: {comics_raw['Annihilation (2006)']}",
    "Annihilation: Conquest (2007)": f"Annihilation: Conquest (2007)\nRating: {comics_raw['Annihilation: Conquest (2007)']}",
    "War of Kings (2009)": f"War of Kings (2009)\nRating: {comics_raw['War of Kings (2009)']}",
    "Realm of Kings (2009)": f"Realm of Kings (2009)\nRating: {comics_raw['Realm of Kings (2009)']}",
    "The Thanos Imperative (2010)": f"The Thanos Imperative (2010)\nRating: {comics_raw['The Thanos Imperative (2010)']}"
}

# Conexiones con escritores
G.add_edge("Keith Giffen", comic_map["Annihilation (2006)"])
G.add_edge("Michael Hoskin", comic_map["Annihilation (2006)"])
G.add_edge("Dan Abnett", comic_map["Annihilation: Conquest (2007)"])
G.add_edge("Andy Lanning", comic_map["Annihilation: Conquest (2007)"])
G.add_edge("Dan Abnett", comic_map["War of Kings (2009)"])
G.add_edge("Andy Lanning", comic_map["War of Kings (2009)"])
G.add_edge("Dan Abnett", comic_map["Realm of Kings (2009)"])
G.add_edge("Andy Lanning", comic_map["Realm of Kings (2009)"])
G.add_edge("Dan Abnett", comic_map["The Thanos Imperative (2010)"])
G.add_edge("Andy Lanning", comic_map["The Thanos Imperative (2010)"])

# Conexiones con dibujantes
G.add_edge(comic_map["Annihilation (2006)"], "Gabriele Dell'Otto")
G.add_edge(comic_map["Annihilation: Conquest (2007)"], "Aleksi Briclot")
G.add_edge(comic_map["The Thanos Imperative (2010)"], "Aleksi Briclot")
G.add_edge(comic_map["War of Kings (2009)"], "Frank Cho")
G.add_edge(comic_map["Realm of Kings (2009)"], "Clint Langley")

# Reorganización estética del grafo en 3 columnas escalonadas

pos = {}

# Configuración general
x_writer = -10
x_comic = 0
x_artist = 10

# Distribución con offsets verticales para evitar que se vean lineales
for i, writer in enumerate(escritores):
    pos[writer] = (x_writer, i * -3)

for i, comic in enumerate(comics_nodes):
    pos[comic] = (x_comic, i * -2.5 + 3)  # Más cerca entre cómics, ligeramente más alto

for i, artist in enumerate(dibujantes):
    pos[artist] = (x_artist, i * -3 + 1.5)  # Corrimiento para que no estén alineados con escritores

# Tamaño y color de nodos
sizes = [comics_labeled.get(n, 1) * 300 if n in comics_labeled else 1000 for n in G.nodes()]
colors = []
for node in G.nodes():
    if node in comics_labeled:
        colors.append('skyblue')
    elif node in escritores:
        colors.append('lightgreen')
    else:
        colors.append('lightcoral')

# Dibujar el grafo
plt.figure(figsize=(14, 10))
nx.draw(G, pos, with_labels=True, node_size=sizes, node_color=colors,
        font_size=8.5, font_weight='bold', edge_color='gray')

plt.title("Relación entre cómics, escritores y dibujantes (con ratings)", fontsize=14)
plt.axis('off')
plt.tight_layout()
plt.show()
