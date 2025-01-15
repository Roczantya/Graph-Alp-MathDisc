import networkx as nx
import matplotlib.pyplot as plt

class Graf:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_node(self, node):
        self.graph.add_node(node)

    def add_edge(self, source, target, weight):
        self.graph.add_edge(source, target, weight=weight)

    def visualize_graph(self):
        pos = nx.spring_layout(self.graph)
        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=10)
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)
        plt.title("Graph Visualization")
        plt.show()

    def shortest_path(self, start, end):
        try:
            path = nx.shortest_path(self.graph, source=start, target=end, weight='weight')
            return path
        except nx.NetworkXNoPath:
            return None

    def visual_shortest_path(self, start, end):
        path = self.shortest_path(start, end)
        if not path:
            print("No path found.")
            return

        edge_colors = [
            'red' if (path[i], path[i + 1]) in self.graph.edges else 'black'
            for i in range(len(path) - 1)
        ]
        
        pos = nx.spring_layout(self.graph)
        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=10, edge_color=edge_colors)
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)
        plt.title("Shortest Path Visualization")
        plt.show()

    # Additional Methods
    def longest_path(self):
        try:
            longest_path = nx.dag_longest_path(self.graph, weight='weight')
            return longest_path
        except nx.NetworkXUnfeasible:
            return None

    def visual_longest_path(self):
        path = self.longest_path()
        if not path:
            print("No longest path available.")
            return

        edge_colors = [
            'blue' if (path[i], path[i + 1]) in self.graph.edges else 'black'
            for i in range(len(path) - 1)
        ]

        pos = nx.spring_layout(self.graph)
        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw(self.graph, pos, with_labels=True, node_color='lightgreen', node_size=700, font_size=10, edge_color=edge_colors)
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)
        plt.title("Longest Path Visualization")
        plt.show()

    def node_degree(self, node):
        return self.graph.degree[node]

    def edge_weights(self):
        return nx.get_edge_attributes(self.graph, 'weight')

    def all_paths(self, start, end):
        try:
            paths = list(nx.all_simple_paths(self.graph, source=start, target=end))
            return paths
        except nx.NetworkXNoPath:
            return []

    def is_connected(self):
        return nx.is_weakly_connected(self.graph)

    def connected_components(self):
        if not self.is_connected():
            components = list(nx.weakly_connected_components(self.graph))
            return components
        return [list(self.graph.nodes)]

    def graph_diameter(self):
        if nx.is_strongly_connected(self.graph):
            return nx.diameter(self.graph.to_undirected())
        return None

    def has_cycle(self):
        return nx.is_directed_acyclic_graph(self.graph) == False

    def find_circuits(self):
        try:
            circuits = list(nx.simple_cycles(self.graph))
            return circuits
        except:
            return []

    def length_of_circuits(self):
        circuits = self.find_circuits()
        return [len(circuit) for circuit in circuits]

    def shortest_path_through_circuits(self):
        circuits = self.find_circuits()
        if not circuits:
            return None

        shortest_path = None
        shortest_length = float('inf')

        for circuit in circuits:
            for i in range(len(circuit)):
                path = nx.shortest_path(self.graph, source=circuit[i], target=circuit[(i + 1) % len(circuit)], weight='weight')
                path_length = sum(self.graph[u][v]['weight'] for u, v in zip(path, path[1:]))

                if path_length < shortest_length:
                    shortest_length = path_length
                    shortest_path = path

        return shortest_path

# Example Implementation
graph = Graf()
graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
graph.add_node(4)
graph.add_node(5)

graph.add_edge(1, 2, weight=4.5)
graph.add_edge(1, 3, weight=3.2)
graph.add_edge(2, 4, weight=2.7)
graph.add_edge(3, 4, weight=1.8)
graph.add_edge(1, 4, weight=6.7)
graph.add_edge(3, 5, weight=2.7)

graph.visualize_graph()

print("Shortest Path:", graph.shortest_path(1, 5))
graph.visual_shortest_path(1, 5)

print("Longest Path:", graph.longest_path())
graph.visual_longest_path()

print("Node Degree of 1:", graph.node_degree(1))
print("Edge Weights:", graph.edge_weights())
print("All Paths from 1 to 5:", graph.all_paths(1, 5))

print("Is Graph Connected:", graph.is_connected())
print("Connected Components:", graph.connected_components())
print("Graph Diameter:", graph.graph_diameter())
print("Has Cycle:", graph.has_cycle())
print("Circuits:", graph.find_circuits())  # Now this should return a cycle
print("Length of Circuits:", graph.length_of_circuits())
print("Shortest Path Through Circuits:", graph.shortest_path_through_circuits())
