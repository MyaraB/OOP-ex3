import matplotlib.pyplot as print_graph
from typing import List
import json
import math
from src.NodeData import Node
from collections import deque
from src.PrioritizedNode import PrioritizedNode
from queue import PriorityQueue
from src.DiGraph import DiGraph
from src.GraphInterface import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface


class GraphAlgo(GraphAlgoInterface):
    graph = DiGraph()
    gl = {}

    def __init__(self, graph: DiGraph = None):
        self.graph = graph

    """This abstract class represents an interface of a graph."""

    def get_graph(self) -> GraphInterface:
        return self.graph

    """
        return: the directed graph on which the algorithm works on.
    """

    def load_from_json(self, file_name: str) -> bool:
        with open(file_name) as file:
            self.graph = DiGraph()
            graph_file = json.load(file)
            node_loader = graph_file.get("Nodes")
            edge_loader = graph_file.get("Edges")
            for itr in node_loader:
                if itr.get("pos") is None:
                    self.graph.add_node(itr.get("id"))
                else:
                    geo = str(itr.get("pos")).split(",")
                    self.graph.add_node(itr.get("id"))
                    self.graph.nodes[itr.get("id")].set_location(float(geo[0]), float(geo[1]), 0)

            for itrs in edge_loader:
                src = itrs.get("src")
                dest = itrs.get("dest")
                weight = itrs.get("w")
                self.graph.add_edge(src, dest, weight)

            return True

    """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """

    def save_to_json(self, file_name: str) -> bool:
        with open(file_name, 'w') as file:
            if self.graph is not None:
                files = dict()
                files["Nodes"] = list()
                files["Edges"] = list()
                for nod in self.graph.nodes.values():
                    if nod.geo_location is not None:
                        files["Nodes"].append({"pos": nod.geo_location, "id": nod.key})
                    else:
                        files["Nodes"].append({"id": nod.key})
                for save in self.graph.edges.keys():
                    for key, items in self.graph.all_out_edges_of_node(save).items():
                        files["Edges"].append({"src": save, "w": items, "dest": key})
                json.dump(files, file)
                return True
            else:
                return False

    """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """

    def min_neighbor(self, id1) -> int:
        neigh = self.graph.all_in_edges_of_node(id1)
        all_nodes = self.graph.get_all_v()
        min_weight = all_nodes[id1].get_weight()
        min_key = id1
        for key in neigh.keys():
            if all_nodes[key].get_weight() != -1:
                if all_nodes[key].get_weight() < min_weight and \
                        all_nodes[key].get_weight() + neigh[key] == all_nodes[id1].get_weight():
                    min_key = key
                    min_weight = all_nodes[key].get_weight()
        return min_key

    def shortest_path_dist(self, id1: int, id2: int) -> (float):
        if id1 not in self.graph.nodes.keys() or id2 not in self.graph.nodes.keys():
            return -1
        if id1 == id2:
            return 0
        all_edge = self.graph.all_out_edges_of_node(id1)
        if all_edge is None:
            return -1
        total_edge = self.graph.edges
        all_node = self.graph.get_all_v()
        for node in all_node.keys():
            all_node[node].set_weight(-1)
        all_node[id1].set_weight(0)
        adjacent = PriorityQueue()
        for nod in all_edge.keys():
            if nod != id1:
                all_node[nod].set_weight(all_edge[nod])
                adjacent.put(PrioritizedNode(all_node[nod].get_weight(), all_node[nod]))
        while adjacent.qsize() != 0:
            current_adjacent = adjacent.get()
            current_node = current_adjacent.get_node()
            if current_node == all_node[id2]:
                return all_node[id2].get_weight()
            all_edge = self.graph.all_out_edges_of_node(current_node.get_key())
            if all_edge is not None:
                for key in all_edge.keys():
                    if all_node[key].get_weight() == -1 or all_edge[key] + current_node.get_weight() < all_node[
                        key].get_weight():
                        all_node[key].set_weight(all_edge[key] + current_node.get_weight())
                        adjacent.put(PrioritizedNode(all_node[key].get_weight(), all_node[key]))
        return all_node[id2].get_weight()

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if self.graph is not None:
            dis = self.shortest_path_dist(id1, id2)
            if dis == -1:
                return math.inf, []
            path = [id1]
            if dis == 0:
                return 0, path
            path.remove(id1)
            current_node = id2
            while current_node != id1:
                path.append(current_node)
                current_node = self.min_neighbor(current_node)
            path.append(current_node)
            final_path = list(reversed(path))
            return dis, final_path
        else:
            return math.inf, None

        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through
        Example:
#      >>> from GraphAlgo import GraphAlgo
#       >>> g_algo = GraphAlgo()
#        >>> g_algo.addNode(0)
#        >>> g_algo.addNode(1)
#        >>> g_algo.addNode(2)
#        >>> g_algo.addEdge(0,1,1)
#        >>> g_algo.addEdge(1,2,4)
#        >>> g_algo.shortestPath(0,1)
#        (1, [0, 1])
#        >>> g_algo.shortestPath(0,2)
#        (5, [0, 1, 2])
        Notes:
        If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """

    def bfs(self, id1: int) -> (list, dict):
        node = self.graph.nodes[id1]
        list1 = []
        list2 = {}
        q = deque()
        node.set_tag(2)
        list2[node.key] = node
        list1.append(node.key)
        self.gl[id1] = id1
        if node.get_key() in self.graph.edges.keys():
            for key in self.graph.edges[node.get_key()].keys():
                temp = self.graph.nodes[key]
                temp.set_tag(1)
                list2[key] = temp
                q.append(temp.key)
        while q:
            nodes = q.popleft()
            if nodes in self.graph.edges.keys():
                for keys in self.graph.edges[nodes].keys():
                    temp3 = self.graph.nodes[keys]
                    if temp3.get_tag() == 0:
                        temp3.set_tag(1)
                        list2[temp3.get_key()] = temp3
                        q.append(temp3.key)
        if node.get_key() in self.graph.opposite_edges.keys():
            for nod in self.graph.opposite_edges[node.key].keys():
                temp4 = self.graph.nodes[nod]
                if temp4.get_tag() == 1:
                    q.append(temp4.key)
        while q:
            node = q.popleft()
            if self.graph.nodes[node].get_tag() == 1:
                self.graph.nodes[node].set_tag(2)
                list2[node] = self.graph.nodes[node]
                list1.append(node)
                self.gl[node] = node
                for i in self.graph.opposite_edges[node].keys():
                    temp3 = self.graph.nodes[i]
                    q.append(temp3.key)
        return list1, list2

    def connected_component(self, id1: int) -> list:
        if self.graph is None:
            return []
        if id1 not in self.graph.nodes.keys():
            return []
        lista = self.bfs(id1)
        for key in lista[1]:
            lista[1][key].set_tag(0)
        return lista[0]

    def connected_components(self) -> List[list]:
        self.gl.clear()
        if self.graph is None:
            return []
        ans = []
        for key in self.graph.nodes:
            if key not in self.gl:
                ans.append(self.connected_component(key))
        return ans

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
