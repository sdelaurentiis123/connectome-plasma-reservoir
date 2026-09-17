import networkx as nx
import numpy as np
from sklearn.linear_model import Ridge
from reservoir import normalized_adjacency, run_reservoir


def main() -> None:
    rng = np.random.default_rng(7)
    graph = nx.gn_graph(64, seed=7).reverse(copy=True)
    nx.set_edge_attributes(graph, 1.0, "weight")
    nodes = list(graph.nodes)
    adjacency = normalized_adjacency(graph, nodes)
    signal = np.sin(np.linspace(0, 20, 800))[:, None]
    weights = rng.normal(scale=0.2, size=(len(nodes), 1))
    states = run_reservoir(adjacency, signal[:-1], weights)
    split = 600
    model = Ridge(alpha=1e-3).fit(states[:split], signal[1:split + 1])
    rmse = np.sqrt(np.mean((model.predict(states[split:]) - signal[split + 1:]) ** 2))
    print(f"held-out RMSE: {rmse:.4f}")

if __name__ == "__main__":
    main()
