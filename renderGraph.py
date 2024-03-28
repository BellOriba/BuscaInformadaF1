import networkx as nx
import matplotlib.pyplot as plt
from calendarGraph import G
# Seu código para criar o grafo aqui...

# Desenhar o grafo
pos = nx.get_node_attributes(G, 'pos')
continent = nx.get_node_attributes(G, 'continent')

# Dividir os nós por continente
continent_colors = {
    "Ásia": "red",
    "Japão": "red",
    "Oceania": "blue",
    "Oceania (Austrália)": "blue",
    "Oceania (Indonésia)": "blue",
    "Europa": "green",
    "América do Norte": "orange",
    "América do Sul": "purple",
    "Oriente Médio": "yellow",
    "Oriente Médio (Cáucaso)": "yellow"
}

node_colors = [continent_colors[continent[n]] for n in G.nodes()]

nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=500, font_size=5)

# Montar as legendas do Grafo
for continent, color in continent_colors.items():
    plt.scatter([], [], c=color, label=continent)

# Desenhar as legendas do Grafo
#plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='Continentes')

plt.show()
