from ..services.maze_service import MazeService
from ..models.graph import Graph

class GameController:
    def __init__(self, maze_service: MazeService):
        self.maze_service = maze_service
        self.graph: Graph = None
        self.start_node: str = ''
        self.end_node: str = ''

    def initialize_game(self, size: int):
        self.graph, self.start_node, self.end_node = self.maze_service.create_maze(size)
        return self.graph, self.start_node, self.end_node

    def get_available_moves(self, current_node_id: str):
        return self.maze_service.get_available_moves(self.graph, current_node_id)

    def is_game_end(self, current_node_id: str) -> bool:
        return current_node_id == self.end_node

    def get_start_node(self) -> str:
        return self.start_node

    def get_end_node(self) -> str:
        return self.end_node
