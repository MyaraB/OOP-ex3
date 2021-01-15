from src.NodeData import Node
from dataclasses import dataclass


@dataclass(order=True)
class PrioritizedNode:
    priority: float
    item: object = Node

    def __init__(self, weight, node):
        self.priority = weight
        self.item = node

    def get_node(self):
        return self.item
