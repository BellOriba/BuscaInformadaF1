import networkx as nx
import matplotlib.pyplot as plt
from calendarGraph import GRAPH

pos = nx.get_node_attributes(GRAPH, 'pos')
continent = nx.get_node_attributes(GRAPH, 'continent')

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

node_colors = [continent_colors[continent[n]] for n in GRAPH.nodes()]

nx.draw(GRAPH, pos, with_labels=True, node_color=node_colors, node_size=500, font_size=5)

for continent, color in continent_colors.items():
    plt.scatter([], [], c=color, label=continent)

#plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='Continentes')

if __name__ == "__main__":
    plt.show()
    