from unittest import TestCase
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
from typing import List

class TestGraphAlgo(TestCase):
    def test_get_graph(self):
        graph = DiGraph()
        graph_algo = GraphAlgo(graph)
        self.assertEqual(graph.v_size(), 0)
        self.assertEqual(graph.e_size(), 0)
        self.assertEqual(graph_algo.shortest_path(0, 0), (None, None))
        self.assertEqual(graph_algo.connected_component(1), [])
        self.assertEqual(graph_algo.connected_components(), [])
        self.assertTrue(graph_algo.save_to_json('../data/empty_graph'))
        self.assertTrue((graph_algo.load_from_json('../data/empty_graph')))
        self.assertEqual(graph_algo.get_graph().v_size(), 0)
        self.assertEqual(graph_algo.get_graph().e_size(), 0)

    def test_load_from_json(self):
        self.graph = DiGraph()
        for i in range(4):
            self.graph.add_node(i, (1, 2, 3))
        self.graph.add_edge(0, 1, 1)
        self.graph.add_edge(1, 0, 1.1)
        self.graph.add_edge(1, 2, 1.3)
        self.graph.add_edge(1, 3, 1.8)
        self.graph.add_edge(2, 3, 1.1)
        graph_algo = GraphAlgo(self.graph)

        graph_algo.save_to_json("to_load.json")
        graph_algo2 = GraphAlgo()
        graph_algo2.load_from_json('../data/TO')


    def test_save_to_json(self):
        self.fail()

    def test_min_neighbor(self):
        self.fail()

    def test_shortest_path_dist(self):
        self.fail()

    def test_shortest_path(self):
        self.graph = DiGraph()
        graph_algo = GraphAlgo(self.graph)
        self.assertEqual((float('inf'), []), graph_algo.shortest_path(1, 2))
        """empty graph"""

        for i in range(4):
            self.graph.add_node(i)
        self.graph.add_edge(0, 1, 1)
        self.graph.add_edge(1, 0, 1.1)
        self.graph.add_edge(1, 2, 1.3)
        self.graph.add_edge(2, 3, 0.5)

        self.assertEqual((0, [1]), graph_algo.shortest_path(1, 1))

        shortest_path: List[list] = graph_algo.shortest_path(1, 3)

        self.assertEqual((1.8, [1, 2, 3]), shortest_path)
        self.graph.add_edge(1, 3, 1.8)
        shortest_path: List[list] = graph_algo.shortest_path(1, 3)
        self.assertEqual((1.8, [1, 3]), shortest_path)

        self.graph = DiGraph()
        for i in range(4):
            self.graph.add_node(i)
        self.graph.add_edge(0, 1, 1)
        self.graph.add_edge(1, 0, 1.1)
        self.graph.add_edge(1, 2, 1.3)
        self.graph.add_edge(1, 3, 1.8)
        self.graph.add_edge(2, 3, 1.1)
        self.graph.add_node(4)
        graph_algo = GraphAlgo(self.graph)
        shortest_path: List[list] = graph_algo.shortest_path(1, 4)
        self.assertEqual((float('inf'), []), shortest_path)


    def test_bfs(self):
        self.fail()

    def test_connected_component(self):
        self.graph = DiGraph()
        algo_g = GraphAlgo(self.graph)

        self.assertEqual([], algo_g.connected_component(1))

        for i in range(6):
            self.graph.add_node(i)

        self.assertEqual([1], algo_g.connected_component(1))

        self.graph.add_edge(0, 1, 2)
        self.graph.add_edge(1, 0, 0.2)
        self.graph.add_edge(0, 3, 0.2)
        self.graph.add_edge(3, 1, 0.2)

        self.assertEqual([0, 1, 3], algo_g.connected_component(0))
        self.assertEqual([1, 3, 0], algo_g.connected_component(1))
        self.assertEqual([3, 0, 1], algo_g.connected_component(3))
        self.assertEqual([2], algo_g.connected_component(2))
        self.assertEqual([4], algo_g.connected_component(4))
        self.assertEqual([5], algo_g.connected_component(5))

        self.graph.remove_edge(3, 1)
        self.graph.remove_edge(0, 3)

        self.assertEqual([0, 1], algo_g.connected_component(0))
        self.assertEqual([1, 0], algo_g.connected_component(1))
        self.assertEqual([3], algo_g.connected_component(3))
        self.assertEqual([2], algo_g.connected_component(2))
        self.assertEqual([4], algo_g.connected_component(4))
        self.assertEqual([5], algo_g.connected_component(5))

        # 0 <--> 1, 2 <--> 4, 3, 5
        self.graph.add_edge(2, 4, 0.5)
        self.graph.add_edge(4, 2, 0.5)

        self.assertEqual([0, 1], algo_g.connected_component(0))
        self.assertEqual([0, 1], algo_g.connected_component(1))
        self.assertEqual([3], algo_g.connected_component(3))
        self.assertEqual([2, 4], algo_g.connected_component(2))
        self.assertEqual([2, 4], algo_g.connected_component(4))
        self.assertEqual([5], algo_g.connected_component(5))

    def test_connected_components(self):
        self.graph = DiGraph()
        algo_g = GraphAlgo(self.graph)

        self.assertEqual([], algo_g.connected_components())
        # 1, 2, 3, 4, 5
        for i in range(6):
            self.graph.add_node(i)

        ans = [[0], [1], [2], [3], [4], [5]]

        self.assertEqual(ans, algo_g.connected_components())

        # 0 <--> 1 <--> 3, 2, 4, 5
        self.graph.add_edge(0, 1, 2)
        self.graph.add_edge(1, 0, 0.2)
        self.graph.add_edge(0, 3, 0.2)
        self.graph.add_edge(3, 1, 0.2)

        scc = algo_g.connected_components()

        self.assertTrue([5] in scc)
        self.assertTrue([4] in scc)
        self.assertTrue([2] in scc)
        self.assertTrue([0, 1, 3] in scc)

        scc.clear()

        # 0 <--> 1, 2,3,4
        self.graph.remove_edge(3, 1)
        self.graph.remove_edge(0, 3)

        scc = algo_g.connected_components()

        self.assertTrue([5] in scc)
        self.assertTrue([4] in scc)
        self.assertTrue([2] in scc)
        self.assertTrue([3] in scc)
        self.assertTrue([0, 1] in scc)

        scc.clear()

        # 0 <--> 1, 2 <--> 4, 3, 5
        self.graph.add_edge(2, 4, 0.5)
        self.graph.add_edge(4, 2, 0.5)

        scc = algo_g.connected_components()

        self.assertTrue([5] in scc)
        self.assertTrue([2, 4] in scc)
        self.assertTrue([3] in scc)
        self.assertTrue([0, 1] in scc)

    def test_plot_graph(self):
        self.fail()
