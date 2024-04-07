from calendarGraph import GRAPH
import networkx as nx
import time
import random

class ACO:
    def __init__(self, graph, ants, evaporation_rate, alpha, beta, iterations):
        self.graph = graph
        self.ants = ants
        self.evaporation_rate = evaporation_rate
        self.alpha = alpha
        self.beta = beta
        self.iterations = iterations
        self.pheromones = {(node1, node2): 1 for node1 in graph.nodes() for node2 in graph.nodes() if node1 != node2}

    def construct_solution(self, ant):
        current_node = random.choice(list(self.graph.nodes()))
        path = [current_node]
        visited = set([current_node])
        while len(visited) < len(self.graph.nodes()):
            next_node = self.select_next_node(ant, current_node, visited)
            path.append(next_node)
            visited.add(next_node)
            current_node = next_node
        return path

    def select_next_node(self, ant, current_node, visited):
        neighbors = list(self.graph.neighbors(current_node))
        unvisited_neighbors = [n for n in neighbors if n not in visited]
        if not unvisited_neighbors:
            return current_node
        probabilities = [self.calculate_probability(ant, current_node, neighbor) for neighbor in unvisited_neighbors]
        next_node = random.choices(unvisited_neighbors, weights=probabilities)[0]
        return next_node

    def calculate_probability(self, ant, current_node, next_node):
        pheromone = self.pheromones[(current_node, next_node)]
        distance = self.graph[current_node][next_node]['weight']
        return (pheromone ** self.alpha) * ((1 / distance) ** self.beta)


    def update_pheromones(self, solutions):
        for edge in self.graph.edges():
            self.pheromones[edge] *= (1 - self.evaporation_rate)
        for solution in solutions:
            for i in range(len(solution) - 1):
                current_node = solution[i]
                next_node = solution[i + 1]
                self.pheromones[(current_node, next_node)] += 1 / self.graph[current_node][next_node]['weight']

    def optimize(self):
        best_distance = float('inf')
        best_solution = None
        for _ in range(self.iterations):
            solutions = [self.construct_solution(ant) for ant in range(self.ants)]
            distances = [sum([self.graph[solution[i]][solution[i + 1]]['weight'] for i in range(len(solution) - 1)]) for solution in solutions]
            best_ant_index = distances.index(min(distances))
            if distances[best_ant_index] < best_distance:
                best_distance = distances[best_ant_index]
                best_solution = solutions[best_ant_index]
            self.update_pheromones(solutions)
        return best_solution, best_distance

if __name__ == "__main__":
    start_time = time.time()
    aco = ACO(GRAPH, ants=5000, evaporation_rate=0.5, alpha=1, beta=2, iterations=100)
    best_solution, best_distance = aco.optimize()
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Tempo de execução: {execution_time} segundos")
    print(f"Melhor solução: {best_solution}")
    print(f"Distância total percorrida: {best_distance:.2f} Km")