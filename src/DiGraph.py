from src.NodeData import Node
import copy
from src.GraphInterface import GraphInterface


class DiGraph(GraphInterface):
    node_size = 0
    edge_size = 0
    mc_counter = 0
    nodes = dict({int: Node})
    edges = dict({int: {int: float}})
    opposite_edges = dict({int: {int: float}})

    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.node_size = 0
        self.edge_size = 0
        self.opposite_edges = {}

    def digraph(self, graph):
        self.nodes = copy.deepcopy(graph.get_all_v())
        self.edges = copy.deepcopy(graph.get_edges())
        self.opposite_edges = copy.deepcopy(graph.get_opposite_edges())

    def __eq__(self, other: object):
        return self.nodes.keys() == other.nodes.keys() and self.edges.keys() == other.edges.keys() \
               and self.opposite_edges.keys() == other.opposite_edges.keys() and self.node_size == other.node_size \
               and self.edge_size == other.edge_size

    def get_edges(self):
        return self.edges.values()

    def get_opposite_edges(self):
        return self.opposite_edges.values()

    def v_size(self) -> int:

        return self.node_size

    """
    Returns the number of vertices in this graph
    @return: The number of vertices in this graph
    """

    def e_size(self) -> int:
        return self.edge_size

    """
    Returns the number of edges in this graph
    @return: The number of edges in this graph
    """

    def get_all_v(self) -> dict:
        if self is not None:
            return self.nodes
        else:
            return None

    """return a dictionary of all the nodes in the Graph, each node is represented using a pair
     (node_id, node_data)
    """

    def all_in_edges_of_node(self, id1: int) -> dict:
        if id1 in self.opposite_edges.keys():
            return self.opposite_edges[id1]
        else:
            return None

    """return a dictionary of all the nodes connected to (into) node_id ,
    each node is represented using a pair (other_node_id, weight)
     """

    def all_out_edges_of_node(self, id1: int) -> dict:
        if id1 in self.edges.keys():
            return self.edges[id1]
        else:
            return None

    """return a dictionary of all the nodes connected from node_id , each node is represented using a pair
    (other_node_id, weight)
    """

    def get_mc(self) -> int:
        return self.mc_counter

    """
    Returns the current version of this graph,
    on every change in the graph state - the MC should be increased
    @return: The current version of this graph.
    """

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if weight < 0:
            return False
        n1 = self.nodes.get(id1)
        n2 = self.nodes.get(id2)
        if id1 == id2:
            return False
        if n1 is not None and n2 is not None:
            if id1 not in self.edges.keys():
                self.edges[id1] = dict()
                if id2 not in self.opposite_edges.keys():
                    self.opposite_edges[id2] = dict()
                self.edges[id1][id2] = weight
                self.opposite_edges[id2][id1] = weight
                self.edge_size += 1
                self.mc_counter += 1
                return True
            elif id2 not in self.edges[id1]:
                if id2 not in self.opposite_edges.keys():
                    self.opposite_edges[id2] = dict()
                self.edges[id1][id2] = weight
                self.opposite_edges[id2][id1] = weight
                self.edge_size += 1
                self.mc_counter += 1
                return True

        else:
            return False

    """
    Adds an edge to the graph.
    @param id1: The start node of the edge
    @param id2: The end node of the edge
    @param weight: The weight of the edge
    @return: True if the edge was added successfully, False o.w.
    Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
    """

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id < 0:
            return False
        if node_id not in self.nodes.keys():
            self.nodes.update({node_id: Node(node_id, pos)})
            self.node_size += 1
            self.mc_counter += 1
            if node_id in self.nodes.keys():
                return True
        else:
            return False

    """
    Adds a node to the graph.
    @param node_id: The node ID
    @param pos: The position of the node
    @return: True if the node was added successfully, False o.w.
    Note: if the node id already exists the node will not be added
    """

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.nodes:
            for key in self.opposite_edges.keys():
                if node_id in self.opposite_edges[key].keys():
                    self.remove_edge(key, node_id)
                    self.mc_counter -= 1
            for key in self.edges.keys():
                if key in self.edges[node_id].keys():
                    self.remove_edge(node_id, key)
                    self.mc_counter -= 1
            del self.nodes[node_id]
            self.node_size -= 1
            self.mc_counter += 1
            return True
        else:
            return False

    """
    Removes a node from the graph.
    @param node_id: The node ID
    @return: True if the node was removed successfully, False o.w.
    Note: if the node id does not exists the function will do nothing
    """

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 in self.edges:
            for keys, items in self.edges.items():
                if keys == node_id1:
                    for key in items:
                        if key == node_id2:
                            del self.edges[keys][key]
                            try:
                                if self.opposite_edges[key][keys]:
                                    del self.opposite_edges[key][keys]
                            except KeyError:
                                pass
                            self.edge_size -= 1
                            self.mc_counter += 1
                            return True
        else:
            return False

    """
    Removes an edge from the graph.
    @param node_id1: The start node of the edge
    @param node_id2: The end node of the edge
    @return: True if the edge was removed successfully, False o.w.
    Note: If such an edge does not exists the function will do nothing
    """
