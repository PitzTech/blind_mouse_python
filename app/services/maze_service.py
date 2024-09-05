from typing import Tuple
from ..models.graph import Graph
from ..interfaces.graph_service_interface import IGraphService
from ..interfaces.maze_service_interface import IMazeService

class MazeService(IMazeService):
    def __init__(self, graph_service: IGraphService):
        self.graph_service = graph_service
        self.start_node: str = ''
        self.end_node: str = ''

    def create_maze(self, size: int) -> Tuple[Graph, str, str]:
        graph = self.graph_service.generate_random_graph(size)
        nodes = list(graph.nodes.keys())
        self.start_node = nodes[0]
        self.end_node = nodes[-1]
        return graph, self.start_node, self.end_node

    def get_available_moves(self, graph: Graph, current_node_id: str):
        current_node = graph.get_node(current_node_id)
        if current_node:
            return [neighbor.id for neighbor in current_node.neighbors]
        return []
