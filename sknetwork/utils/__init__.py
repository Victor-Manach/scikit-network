"""utils module"""
from sknetwork.utils.check import is_symmetric
from sknetwork.utils.co_neighbor import co_neighbor_graph
from sknetwork.utils.format import *
from sknetwork.utils.kmeans import KMeansDense
from sknetwork.utils.knn import KNNDense, CNNDense
from sknetwork.utils.membership import membership_matrix
from sknetwork.utils.parse import edgelist2adjacency, edgelist2biadjacency
from sknetwork.utils.simplex import projection_simplex, projection_simplex_array, projection_simplex_csr
from sknetwork.utils.ward import WardDense


class Bunch(dict):
    """Container object for datasets.
    Dictionary-like object that exposes its keys as attributes.

    This code is taken from scikit-learn.
    >>> b = Bunch(a=1, b=2)
    >>> b['b']
    2
    >>> b.b
    2
    >>> b.a = 3
    >>> b['a']
    3
    >>> b.c = 6
    >>> b['c']
    6
    """

    def __init__(self, **kwargs):
        super().__init__(kwargs)

    def __setattr__(self, key, value):
        self[key] = value

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key)
