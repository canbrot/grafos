import networkx as nx
import community.community_louvain as community_louvain
import matplotlib.pyplot as plt
import random

def create_simplified_graph_for_louvain():
    """Crea un grafo no dirigido simplificado para el algoritmo de Louvain."""
    G = nx.Graph()

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

def run_louvain_community_detection(G):
    """Ejecuta el algoritmo de Louvain para detectar comunidades."""
    partition = community_louvain.best_partition(G)
    return partition

def visualize_communities(G, partition):
    """Visualiza el grafo con los nodos coloreados según la comunidad."""
    plt.figure(figsize=(18, 12))
    pos = nx.spring_layout(G, seed=42)
    cmap = plt.cm.get_cmap('viridis', max(partition.values()) + 1)
    nx.draw_networkx_nodes(G, pos, list(partition.keys()), node_size=500,
                           cmap=cmap, node_color=list(partition.values()))
    nx.draw_networkx_edges(G, pos, alpha=0.5)
    labels = {node: node for node in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels, font_size=8, font_weight='bold')
    plt.title("Detección de Comunidades con el Algoritmo de Louvain", fontsize=16)
    plt.axis('off')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    graph_louvain = create_simplified_graph_for_louvain()
    communities_partition = run_louvain_community_detection(graph_louvain)

    print("Comunidades detectadas:")
    for node, community_id in communities_partition.items():
        print(f"Nodo '{node}': Comunidad {community_id}")

    visualize_communities(graph_louvain, communities_partition)
