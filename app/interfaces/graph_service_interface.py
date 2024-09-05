from abc import ABC, abstractmethod
from ..models.graph import Graph

class IGraphService(ABC):
    @abstractmethod
    def generate_random_graph(self, size: int) -> Graph:
        pass
