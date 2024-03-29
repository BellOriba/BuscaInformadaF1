import networkx as nx
from geopy.distance import geodesic

GRAPH = nx.Graph()

# Nome: (Latitude, Longitude, Continente)
circuits = {
    "Bahrein": (26.03288514680618, 50.51081429999999, "Oriente Médio"),
    "Arábia Saudita": (21.631873729375275, 39.10450086704199, "Oriente Médio"),
    "Austrália": (-37.85007951144554, 144.97000625379565, "Oceania (Austrália)"),
    "Japão": (34.84576960179215, 136.5389629288498, "Japão"),
    "China": (31.340287058028128, 121.22168091534262, "Ásia"),
    "Estados Unidos (Miami)": (25.956903301155435, -80.23625591534264, "América do Norte"),
    "Itália (Imola)": (44.34599235422704, 11.715721853972134, "Europa"),
    "Mônaco": (43.7346632414474, 7.421832230685241, "Europa"),
    "Canadá": (45.50192808026555, -73.5226492, "América do Norte"),
    "Espanha": (41.569852653168546, 2.257588223286894, "Europa"),
    "Áustria": (47.22044080699094, 14.764855607944272, "Europa"),
    "Reino Unido": (52.069766634990955, -1.0214415153426208, "Europa"),
    "Hungria": (47.580323604645145, 19.247244338629518, "Europa"),
    "Bélgica": (50.44469788636203, 5.965629309605444, "Europa"),
    "Holanda": (52.390464847902216, 4.541560821034714, "Europa"),
    "Itália (Monza)": (45.618105511568125, 9.281507015342621, "Europa"),
    "Azerbeijão": (40.37381720158659, 49.853396176713105, "Oriente Médio (Cáucaso)"),
    "Singapura": (1.2916571483181536, 103.86389897109073, "Oceania (Indonésia)"),
    "Estados Unidos (Austin)": (30.13336712741263, -97.6404876, "América do Norte"),
    "México": (19.406232052079446, -99.09239453862952, "América do Norte"),
    "Brasil": (-23.70403404896427, -46.69910125397213, "América do Sul"),
    "Estados Unidos (Las Vegas)": (36.11312217727239, -115.16241563251907, "América do Norte"),
    "Catar": (25.48941461198835, 51.4504998, "Oriente Médio"),
    "Emirados Árabes Unidos": (24.470558762968516, 54.605744530685236, "Oriente Médio")
}

for circuito, (lat, long, continente) in circuits.items():
    if -90 <= lat <= 90 and -180 <= long <= 180:
        GRAPH.add_node(circuito, pos=(long, lat), continent=continente) # Adiciona nó ao grafo
    else:
        print(f"As coordenadas do circuito {circuito} estão fora do intervalo válido.")

for circuito1, data1 in circuits.items():
    for circuito2, data2 in circuits.items():
        if circuito1 != circuito2:
            dist = geodesic((data1[0], data1[1]), (data2[0], data2[1])).kilometers
            # Adiciona arestas entre dois nós com distância como atributo
            GRAPH.add_edge(circuito1, circuito2, weight=dist)

if __name__ == "__main__":
    circuito1 = "Brasil"
    circuito2 = "México"
    distancia = nx.shortest_path_length(GRAPH, circuito1, circuito2, weight='weight')
    distancia2 = nx.shortest_path_length(GRAPH, "Brasil", "Estados Unidos (Miami)", weight='weight')
    print(f"A distância entre {circuito1} e {circuito2} é de aproximadamente {distancia:.2f} Km.")
    print(f"A distância entre {circuito1} e Miami é de aproximadamente {distancia2:.2f} Km.")

