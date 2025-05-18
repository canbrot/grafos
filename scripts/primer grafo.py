import networkx as nx
import matplotlib.pyplot as plt

def create_simplified_graph():
    """Crea un grafo con nombres de nodos simplificados."""
    G = nx.DiGraph()

    nodes = [
        "Annihilation (2006)",
        "Prologo Annihilation",
        "Nova Annihilation",
        "Silver Surfer Annihilation",
        "Super-Skrull Annihilation",
        "Annihilation: Conquest (2007)",
        "Prologo Conquest",
        "Quasar Conquest",
        "Starlord Conquest",
        "Wraith Conquest",
        "Nova Conquest",
        "War of Kings (2009)",
        "Secret Invasion WoK",
        "Ascension WoK",
        "Guardianes WoK",
        "Darkhawk WoK",
        "Sakaar WoK",
        "Warriors WoK",
        "Realm of Kings (2009)",
        "Imperial Guard RoK",
        "Hulk RoK",
        "The Thanos Imperative (2010)",
        "Ignition Thanos",
        "Devastation Thanos"
    ]

    edges = [
        ("Prologo Annihilation", "Annihilation (2006)"),
        ("Annihilation (2006)", "Nova Annihilation"),
        ("Annihilation (2006)", "Silver Surfer Annihilation"),
        ("Annihilation (2006)", "Super-Skrull Annihilation"),

        ("Annihilation (2006)", "Annihilation: Conquest (2007)"),
        ("Annihilation: Conquest (2007)", "Prologo Conquest"),
        ("Annihilation: Conquest (2007)", "Quasar Conquest"),
        ("Annihilation: Conquest (2007)", "Starlord Conquest"),
        ("Annihilation: Conquest (2007)", "Wraith Conquest"),
        ("Annihilation: Conquest (2007)", "Nova Conquest"),

        ("Annihilation: Conquest (2007)", "War of Kings (2009)"),
        ("War of Kings (2009)", "Secret Invasion WoK"),
        ("War of Kings (2009)", "Ascension WoK"),
        ("War of Kings (2009)", "Guardianes WoK"),
        ("War of Kings (2009)", "Darkhawk WoK"),
        ("War of Kings (2009)", "Sakaar WoK"),
        ("War of Kings (2009)", "Warriors WoK"),
        ("War of Kings (2009)", "Realm of Kings (2009)"),

        ("Realm of Kings (2009)", "Imperial Guard RoK"),
        ("Realm of Kings (2009)", "Hulk RoK"),
        ("Realm of Kings (2009)", "The Thanos Imperative (2010)"),
        ("The Thanos Imperative (2010)", "Ignition Thanos"),
        ("The Thanos Imperative (2010)", "Devastation Thanos")
    ]

    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    return G

def assign_ratings(G, ratings_dict):
    """Asigna ratings como peso a cada nodo del grafo."""
    for node, rating in ratings_dict.items():
        if node in G:
            G.nodes[node]['rating'] = rating
        else:
            print(f"Advertencia: el nodo '{node}' no existe en el grafo.")

def get_node_color(rating):
    """Devuelve un color según el rango del rating."""
    if rating >= 9.1:
        return 'yellow'  # Para nodos con rating entre 10 y 9.1
    elif rating >= 8.1:
        return 'royalblue'  # Para nodos con rating entre 9 y 8.1
    elif rating >= 7.1:
        return 'lightblue'  # Para nodos con rating entre 8 y 7.1
    elif rating >= 6.1:
        return 'lightgreen'  # Para nodos con rating entre 7 y 6.1
    else:
        return 'gray'  # Para nodos con rating entre 6 y 5.1

def plot_graph_with_fixed_positions(G):
    """Grafica el grafo con posiciones más separadas y tamaños basados en ratings."""
    
    plt.figure(figsize=(28, 16))

    pos = {
        "Annihilation (2006)": (-12, 8),
        "Prologo Annihilation": (-16, 4),
        "Nova Annihilation": (-12, 4),
        "Silver Surfer Annihilation": (-8, 4),
        "Super-Skrull Annihilation": (-4, 4),

        "Annihilation: Conquest (2007)": (-6, 0),
        "Prologo Conquest": (-12, -4),
        "Quasar Conquest": (-9, -4),
        "Starlord Conquest": (-6, -4),
        "Wraith Conquest": (-3, -4),
        "Nova Conquest": (0, -4),

        "War of Kings (2009)": (6, 0),
        "Secret Invasion WoK": (3, 4),
        "Ascension WoK": (6, 4),
        "Guardianes WoK": (9, 4),
        "Darkhawk WoK": (3, -4),
        "Sakaar WoK": (6, -4),
        "Warriors WoK": (9, -4),

        "Realm of Kings (2009)": (14, 8),
        "Imperial Guard RoK": (17, 4),
        "Hulk RoK": (17, 6),

        "The Thanos Imperative (2010)": (14, 0),
        "Ignition Thanos": (17, -4),
        "Devastation Thanos": (14, -4),
    }

    sizes = [G.nodes[n].get('rating', 1) * 300 for n in G.nodes]
    labels = {n: f"{n}\n({G.nodes[n].get('rating', '?')})" for n in G.nodes}

    node_colors = [get_node_color(G.nodes[n].get('rating', 0)) for n in G.nodes]

    nx.draw(
        G, pos,
        with_labels=False,
        node_color=node_colors,
        node_size=sizes,
        font_size=10, font_weight='bold',
        arrowsize=20
    )

    nx.draw_networkx_labels(G, pos, labels=labels, font_size=8, font_weight='bold', font_color='black')
    plt.title("Grafo narrativo Marvel con ratings por nodo", fontsize=14)
    plt.axis('off')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    G = create_simplified_graph()

    ratings = {
        "Annihilation (2006)": 9.2,
        "Prologo Annihilation": 7.9,
        "Nova Annihilation": 8.6,
        "Silver Surfer Annihilation": 8.0,
        "Super-Skrull Annihilation": 7.6,
        "Annihilation: Conquest (2007)": 8.4,
        "Prologo Conquest": 7.5,
        "Quasar Conquest": 7.7,
        "Starlord Conquest": 8.2,
        "Wraith Conquest": 7.3,
        "Nova Conquest": 8.2,
        "War of Kings (2009)": 8.5,
        "Secret Invasion WoK": 8.1,
        "Ascension WoK": 7.0,
        "Guardianes WoK": 8.0,
        "Darkhawk WoK": 6.8,
        "Sakaar WoK": 7.3,
        "Warriors WoK": 5.8,
        "Realm of Kings (2009)": 6.7,
        "Imperial Guard RoK": 6.8,
        "Hulk RoK": 8.4,
        "The Thanos Imperative (2010)": 8.2,
        "Ignition Thanos": 7.8,
        "Devastation Thanos": 7.6
    }

    assign_ratings(G, ratings)
    plot_graph_with_fixed_positions(G)
