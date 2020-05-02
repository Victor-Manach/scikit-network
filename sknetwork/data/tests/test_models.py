# -*- coding: utf-8 -*-
# tests for toy_graphs.py
"""authors:
Thomas Bonald <bonald@enst.fr>
Quentin Lutz <qlutz@enst.fr>"""

import unittest

from sknetwork.data.models import *


class TestModels(unittest.TestCase):

    def test_shape(self):
        n = 5
        for model in [linear_graph, linear_digraph, cyclic_graph, cyclic_digraph, watts_strogatz]:
            adjacency = model(n)
            graph = model(n, metadata=True)
            self.assertEqual(adjacency.shape, (n, n))
            self.assertEqual(graph.adjacency.shape, (n, n))

        adjacency = erdos_renyie(n)
        self.assertEqual(adjacency.shape, (n, n))

        adjacency = albert_barabasi(n, 2)
        self.assertEqual(adjacency.shape, (n, n))

        n1 = 4
        n2 = 6
        n = n1 * n2
        adjacency = grid(n1, n2)
        self.assertEqual(adjacency.shape, (n, n))
        graph = grid(n1, n2, metadata=True)
        self.assertEqual(graph.adjacency.shape, (n, n))

    def test_SBM(self):
        graph = block_model(np.array([4, 5, 6]), np.array([0.5, 0.3, 0.2]), 0.1, metadata=True)
        adjacency = graph.adjacency
        labels = graph.labels
        self.assertEqual(adjacency.shape, (15, 15))
        self.assertEqual(len(labels), 15)

        with self.assertRaises(ValueError):
            block_model(np.array([4, 5, 6]), 0.05, 0.2)
