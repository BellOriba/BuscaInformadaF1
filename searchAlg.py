# Nearest-Neighbor Heuristic
from calendarGraph import GRAPH, circuits 
import networkx as nx

def nearest_neighbor_tour(start_circuit):
    tour = [start_circuit]
    current_circuit = start_circuit
    remaining_circuits = set(circuits.keys())
    remaining_circuits.remove(start_circuit)

    while remaining_circuits:
        nearest_circuit = min(remaining_circuits, key=lambda x: GRAPH[current_circuit][x]['weight'])
        tour.append(nearest_circuit)
        remaining_circuits.remove(nearest_circuit)
        current_circuit = nearest_circuit

    return tour

if __name__ == "__main__":
    start_circuit = "Brasil"
    tour = nearest_neighbor_tour(start_circuit)
    print("Nearest Neighbor Tour:")
    print(" -> ".join(tour))
