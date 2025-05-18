import networkx as nx

# Crear el grafo dirigido
G = nx.DiGraph()

# Definir nodos
nodes = [
    "Annihilation (2006)", "Prologo Annihilation", "Nova Annihilation",
    "Silver Surfer Annihilation", "Super-Skrull Annihilation",
    "Annihilation: Conquest (2007)", "Prologo Conquest", "Quasar Conquest",
    "Starlord Conquest", "Wraith Conquest", "Nova Conquest",
    "War of Kings (2009)", "Secret Invasion WoK", "Ascension WoK",
    "Guardianes WoK", "Darkhawk WoK", "Sakaar WoK", "Warriors WoK",
    "Realm of Kings (2009)", "Imperial Guard RoK", "Hulk RoK",
    "The Thanos Imperative (2010)", "Ignition Thanos", "Devastation Thanos"
]

# Definir aristas
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

# Agregar nodos y aristas
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Asignar ratings
ratings = {
    "Annihilation (2006)": 9.2, "Prologo Annihilation": 7.9, "Nova Annihilation": 8.6,
    "Silver Surfer Annihilation": 8.0, "Super-Skrull Annihilation": 7.6,
    "Annihilation: Conquest (2007)": 8.4, "Prologo Conquest": 7.5, "Quasar Conquest": 7.7,
    "Starlord Conquest": 8.2, "Wraith Conquest": 7.3, "Nova Conquest": 8.2,
    "War of Kings (2009)": 8.5, "Secret Invasion WoK": 8.1, "Ascension WoK": 7.0,
    "Guardianes WoK": 8.0, "Darkhawk WoK": 6.8, "Sakaar WoK": 7.3, "Warriors WoK": 5.8,
    "Realm of Kings (2009)": 6.7, "Imperial Guard RoK": 6.8, "Hulk RoK": 8.4,
    "The Thanos Imperative (2010)": 8.2, "Ignition Thanos": 7.8, "Devastation Thanos": 7.6
}

nx.set_node_attributes(G, ratings, name='rating')

# --- Cálculo de métricas de centralidad ---

# 1. Centralidad de grado
print("\nIn-degree (entrantes):")
for node, degree in sorted(G.in_degree(), key=lambda x: x[1], reverse=True)[:5]:
    print(f"{node}: {degree}")

print("\nOut-degree (salientes):")
for node, degree in sorted(G.out_degree(), key=lambda x: x[1], reverse=True)[:5]:
    print(f"{node}: {degree}")

# 2. Centralidad de intermediación
betweenness = nx.betweenness_centrality(G)
print("\nCentralidad de intermediación (betweenness):")
for node, bc in sorted(betweenness.items(), key=lambda x: x[1], reverse=True)[:5]:
    print(f"{node}: {bc:.4f}")

# 3. Centralidad de cercanía
closeness = nx.closeness_centrality(G)
print("\nCentralidad de cercanía (closeness):")
for node, cc in sorted(closeness.items(), key=lambda x: x[1], reverse=True)[:5]:
    print(f"{node}: {cc:.4f}")

# 4. Centralidad de eigenvector
try:
    eigenvector = nx.eigenvector_centrality(G, max_iter=1000)
    print("\nCentralidad de eigenvector:")
    for node, ec in sorted(eigenvector.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"{node}: {ec:.4f}")
except nx.PowerIterationFailedConvergence:
    print("\nError: La centralidad de eigenvector no convergió.")

# 5. PageRank
pagerank = nx.pagerank(G)
print("\nPageRank:")
for node, pr in sorted(pagerank.items(), key=lambda x: x[1], reverse=True)[:5]:
    print(f"{node}: {pr:.4f}")

# --- Relación rating vs centralidad ---
print("\nRelación entre rating y betweenness centrality:")
for node in G.nodes:
    rating = G.nodes[node].get('rating', None)
    if rating is not None:
        print(f"{node}: Rating {rating}, Betweenness {betweenness[node]:.4f}")
