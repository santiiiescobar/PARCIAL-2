import networkx as nx

G = nx.Graph()

characters = ["Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", "C-3PO", "Leia", "Rey", "Kylo Ren", "Chewbacca", "Han Solo", "R2-D2", "BB-8"]

for character in characters:
    G.add_node(character)

G.add_edge("Luke Skywalker", "Leia", episodes=5)
G.add_edge("Luke Skywalker", "Han Solo", episodes=6)
G.add_edge("Luke Skywalker", "Yoda", episodes=3)
G.add_edge("Leia", "Han Solo", episodes=4)
G.add_edge("Leia", "Yoda", episodes=2)
G.add_edge("Han Solo", "Yoda", episodes=1)
G.add_edge("Darth Vader", "Boba Fett", episodes=2)
G.add_edge("Darth Vader", "Leia", episodes=3)
G.add_edge("C-3PO", "R2-D2", episodes=7)
G.add_edge("Chewbacca", "Han Solo", episodes=5)
G.add_edge("Rey", "Kylo Ren", episodes=4)
G.add_edge("BB-8", "Rey", episodes=3)
G.add_edge("BB-8", "Poe Dameron", episodes=3)

#Punto A
minimum_spanning_tree = nx.minimum_spanning_tree(G)

# Punto B
contains_yoda = "Yoda" in minimum_spanning_tree.nodes

# Punto C
max_shared_episodes = max([G[u][v]['episodes'] for u, v in G.edges()])

print("Árbol de expansión mínimo:")
print(minimum_spanning_tree.edges)
print("¿Contiene a Yoda?", contains_yoda)
print("Número máximo de episodios compartidos:", max_shared_episodes)
