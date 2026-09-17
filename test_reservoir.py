import networkx as nx
import numpy as np
from reservoir import normalized_adjacency, run_reservoir

def test_reservoir_shape():
    states = run_reservoir(np.eye(4), np.ones((5, 1)), np.ones((4, 1)))
    assert states.shape == (5, 4)
    assert np.isfinite(states).all()


def test_nonfinite_input_fails_closed():
    g = nx.DiGraph([(0, 1), (1, 0)])
    nx.set_edge_attributes(g, 1.0, "weight")
    a = normalized_adjacency(g, [0, 1])
    x = np.array([[0.0], [np.nan]])
    with np.testing.assert_raises(ValueError):
        run_reservoir(a, x, np.ones((2, 1)))
