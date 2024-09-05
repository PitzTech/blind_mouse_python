from abc import ABC, abstractmethod
from typing import Tuple
from ..models.graph import Graph

class IMazeService(ABC):
    @abstractmethod
    def create_maze(self, size: int) -> Tuple[Graph, str, str]:
        pass

    @abstractmethod
    def get_available_moves(self, graph: Graph, current_node_id: str):
        pass
