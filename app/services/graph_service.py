import random
from ..models.graph import Graph
from ..interfaces.graph_service_interface import IGraphService

class GraphService(IGraphService):
    def generate_random_graph(self, size: int) -> Graph:
        graph = Graph()

        # Adicionar nós
        for i in range(size):
            graph.add_node(f"Node_{i}")

        nodes = list(graph.nodes.values())

        # Conexão linear para garantir que todos os nós estejam conectados
        for i in range(len(nodes) - 1):
            graph.connect_nodes(nodes[i].id, nodes[i + 1].id)

        # Conexões extras para múltiplos caminhos
        for node in nodes:
            random_neighbor = random.choice(nodes)
            if node != random_neighbor and random_neighbor not in node.neighbors:
                graph.connect_nodes(node.id, random_neighbor.id)

        return graph
