import numpy as np
from connectome_plasma.reservoir import run_reservoir

def test_reservoir_shape():
    states = run_reservoir(np.eye(4), np.ones((5, 1)), np.ones((4, 1)))
    assert states.shape == (5, 4)
    assert np.isfinite(states).all()
