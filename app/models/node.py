from typing import List

class Node:
    def __init__(self, node_id: str):
        self.id = node_id
        self.neighbors: List['Node'] = []

    def add_neighbor(self, node: 'Node'):
        self.neighbors.append(node)
