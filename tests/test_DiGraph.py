from unittest import TestCase

from src.DiGraph import DiGraph

class TestDiGraph(TestCase):
    def test_digraph(self):
        self.fail()

    def test_get_edges(self):
        self.fail()

    def test_get_opposite_edges(self):
        self.fail()

    def test_v_size(self):
        self.fail()

    def test_e_size(self):
        self.fail()

    def test_get_all_v(self):
        self.fail()

    def test_all_in_edges_of_node(self):
        self.fail()

    def test_all_out_edges_of_node(self):
        graph = DiGraph()
        self.assertTrue(graph.add_node(2))
        self.assertTrue(graph.add_node(3))
        self.assertTrue(graph.add_node(4))
        self.assertTrue(graph.add_edge(2, 3, 0))
        self.assertTrue(graph.add_edge(3, 4, 1))
        edge = graph.all_out_edges_of_node(3)
        self.assertEqual(edge[3], 1)


    def test_get_mc(self):
        self.fail()

    def test_add_edge(self):
        graph = DiGraph()
        self.assertTrue(graph.add_node(4))
        self.assertTrue(graph.add_node(7))
        self.assertTrue(graph.add_node(8))
        self.assertTrue(graph.add_node(3, (7, 8, 0)))
        self.assertTrue(graph.add_edge(8, 7, 1))
        self.assertTrue(graph.add_edge(4, 7, 0))
        self.assertTrue(graph.add_edge(7, 8, 0))
        self.assertTrue(graph.add_edge(4, 8, 0))
        self.assertFalse(graph.add_edge(3, 3, 0))
        self.assertFalse(graph.add_edge(4, 3, -4))
        self.assertFalse(graph.add_edge(4, 8, 50))
        self.assertEqual(graph.e_size(), 4)


    def test_add_node(self):
        graph = DiGraph()
        self.assertEqual(graph.v_size(), 0)
        self.assertTrue(graph.add_node(0))
        self.assertTrue(graph.add_node(1))
        self.assertTrue(graph.add_node(2))
        self.assertEqual(graph.v_size(), 3)
        self.assertTrue(graph.add_node(3))
        self.assertEqual(graph.v_size(), 4)


    def test_remove_node(self):
        graph = DiGraph()
        self.assertTrue(graph.add_node(1), (345.11, 7.74, 0))
        self.assertTrue(graph.add_node(0, (345.11, 7.74, 0)))
        graph1 = DiGraph()
        self.assertTrue(graph1.add_node(1), (345.11, 7.74, 0))
        self.assertTrue(graph1.add_node(0, (345.11, 7.74, 0)))
        self.assertEqual(len(graph.get_all_v()), len(graph1.get_all_v()))
        graph.add_edge(2, 6, 0)
        self.assertNotEqual(graph.get_all_v(), graph1.get_all_v())
        graph1.add_edge(2, 6, 0)
        self.assertEqual(graph.get_all_v(), graph1.get_all_v())
        self.assertEqual(graph, graph1)
        graph1.add_edge(6, 2, 0.9)
        self.assertNotEqual(graph1, graph)


    def test_remove_edge(self):
        graph = DiGraph()
        self.assertTrue(graph.add_node(3))
        self.assertTrue(graph.add_node(4))
        self.assertTrue(graph.add_node(5))
        self.assertTrue(graph.add_node(6))
        self.assertTrue(graph.add_node(7))
        self.assertTrue(graph.add_edge(6, 5, 1))
        self.assertTrue(graph.add_edge(5, 6, 0))
        self.assertTrue(graph.add_edge(4, 5, 0))
        self.assertTrue(graph.add_edge(4, 6, 0))
        self.assertEqual(len(graph.all_out_edges_of_node(4)), 2)
        self.assertTrue(graph.remove_edge(4, 6))
        self.assertFalse(graph.remove_edge(4, 6))
        self.assertFalse(graph.remove_edge(4, 6))
        self.assertEqual(len(graph.all_out_edges_of_node(4)), 1)
        self.assertEqual(graph.v_size(), 5)
        self.assertEqual(graph.e_size(), 3)
        self.assertTrue(graph.remove_edge(4, 5))
        self.assertEqual(graph.get_mc(), 11)
