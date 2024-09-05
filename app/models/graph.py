from typing import Dict
from .node import Node

class Graph:
    def __init__(self):
        self.nodes: Dict[str, Node] = {}

    def add_node(self, node_id: str) -> Node:
        node = Node(node_id)
        self.nodes[node_id] = node
        return node

    def get_node(self, node_id: str) -> Node:
        return self.nodes.get(node_id)

    def connect_nodes(self, id1: str, id2: str):
        node1 = self.get_node(id1)
        node2 = self.get_node(id2)
        if node1 and node2:
            node1.add_neighbor(node2)
            node2.add_neighbor(node1)
