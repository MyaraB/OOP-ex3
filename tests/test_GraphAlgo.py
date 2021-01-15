from unittest import TestCase
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
from typing import List

class TestGraphAlgo(TestCase):
    def test_get_graph(self):
        graph = DiGraph()
        graph_algo = GraphAlgo(graph)
        self.assertEqual(graph.e_size(), 0)
        self.assertEqual(graph.v_size(), 0)
        self.assertEqual(graph_algo.connected_components(), [])
        self.assertTrue(graph_algo.save_to_json('../data/hello'))
        self.assertTrue((graph_algo.load_from_json('../data/hello')))
        self.assertEqual(graph_algo.get_graph().e_size(), 0)
        self.assertEqual(graph_algo.get_graph().v_size(), 0)

    def test_load_from_json(self):
        self.fail()

    def test_save_to_json(self):
        self.graph = DiGraph()
        for i in range(7):
            self.graph.add_node(i, (1, 5, 7))
        self.graph.add_edge(5, 6, 4)
        self.graph.add_edge(3, 4, 3)
        self.graph.add_edge(4, 5, 2)
        self.graph.add_edge(4, 6, 5)
        self.graph.add_edge(4, 3, 2)
        self.graph.add_edge(4, 3, 2)
        graph_algo = GraphAlgo(self.graph)
        graph_algo.save_to_json("test.json")

    def test_min_neighbor(self):
        self.fail()

    def test_shortest_path_dist(self):
        self.fail()

    def test_shortest_path(self):
        self.graph = DiGraph()
        graph_algo = GraphAlgo(self.graph)
        self.assertEqual((float('inf'), []), graph_algo.shortest_path(0, 1))
        for i in range(7):
            self.graph.add_node(i, (1, 5, 7))
        self.graph.add_edge(5, 6, 4)
        self.graph.add_edge(3, 4, 3)
        self.graph.add_edge(4, 5, 2)
        self.graph.add_edge(4, 6, 5)
        self.graph.add_edge(4, 3, 2)
        self.graph.add_edge(4, 3, 2)
        self.assertEqual((0, [3]), graph_algo.shortest_path(3, 3))
        shortest_path: List[list] = graph_algo.shortest_path(3, 6)
        self.assertEqual((8, [3, 4, 6]), shortest_path)

    def test_bfs(self):
        self.fail()

    def test_connected_component(self):
        self.graph = DiGraph()
        galg = GraphAlgo(self.graph)
        self.assertEqual((float('inf'), []), galg.shortest_path(0, 1))
        for i in range(7):
            self.graph.add_node(i, (1, 5, 7))
        self.graph.add_edge(5, 6, 4)
        self.graph.add_edge(3, 4, 3)
        self.graph.add_edge(4, 5, 2)
        self.graph.add_edge(4, 6, 5)
        self.graph.add_edge(4, 3, 2)
        self.graph.add_edge(6, 3, 2)
        self.assertEqual([1], galg.connected_component(1))
        self.assertEqual([4, 3, 6, 5], galg.connected_component(4))
        self.assertEqual([5, 4, 3, 6], galg.connected_component(5))
        self.assertEqual([2], galg.connected_component(2))
        self.assertEqual([1], galg.connected_component(1))



    def test_connected_components(self):
        self.graph = DiGraph()
        galg = GraphAlgo(self.graph)
        for i in range(7):
            self.graph.add_node(i, (1, 5, 7))
        ans = [[0], [1], [2], [3], [4], [5], [6]]
        self.assertEqual(ans, galg.connected_components())
        self.graph.add_edge(5, 6, 4)
        self.graph.add_edge(3, 4, 3)
        self.graph.add_edge(4, 5, 2)
        self.graph.add_edge(4, 6, 5)
        self.graph.add_edge(4, 3, 2)
        self.graph.add_edge(6, 3, 2)
        ans = galg.connected_components()
        self.assertTrue([0] in ans)
        self.assertTrue([1] in ans)
        self.assertTrue([3, 4, 6, 5] in ans)


    def test_plot_graph(self):
        self.fail()
