# Nearest-Neighbor Heuristic
from calendarGraph import GRAPH, circuits 
import networkx as nx
import time

def nearest_neighbor_tour(start_circuit):
    tour = [start_circuit]
    current_circuit = start_circuit
    remaining_circuits = set(circuits.keys())
    remaining_circuits.remove(start_circuit)
    total_distance = 0

    while remaining_circuits:
        nearest_circuit = min(remaining_circuits, key=lambda x: GRAPH[current_circuit][x]['weight'])
        tour.append(nearest_circuit)
        total_distance += GRAPH[current_circuit][nearest_circuit]['weight']
        remaining_circuits.remove(nearest_circuit)
        current_circuit = nearest_circuit

    total_distance += GRAPH[tour[-1]][start_circuit]['weight']
    return tour, total_distance

if __name__ == "__main__":
    start_circuit = "Singapura"

    num_executions = 1000
    total_execution_time = 0

    for _ in range(num_executions):
        start_time = time.time()
        tour, total_distance = nearest_neighbor_tour(start_circuit)
        end_time = time.time()

        execution_time = (end_time - start_time) * 1000
        total_execution_time += execution_time

    average_execution_time = total_execution_time / num_executions

    print("Nearest Neighbor Tour:")
    print(" -> ".join(tour))
    print("Distância total percorrida:", total_distance)
    print("Tempo médio de execução (", num_executions, " execuções):", average_execution_time, "milissegundos")
