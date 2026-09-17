# Connectome Plasma Reservoir

Research scaffold for testing whether a fixed biological connectome is a useful recurrent reservoir for plasma time-series prediction.

## Question

Does a tractable subgraph of the *Drosophila* male CNS connectome provide more useful memory, nonlinear separation, or robustness than matched random reservoirs on plasma signals?

This repository does **not** simulate a fly brain. The connectome supplies directed graph structure and synapse counts. Neuron dynamics, edge signs, decay, input mapping, and readout are modeling assumptions that must be tested.

## First experiments

1. Validate the pipeline on Lorenz-63 and a synthetic regime-switching signal.
2. Query a named sensory-to-descending-neuron subgraph from `male-cns:v1.0` through neuPrint.
3. Run a leaky recurrent reservoir over that fixed graph and train only a ridge/linear readout.
4. Compare against:
   - degree-preserving rewires,
   - Erdős-Rényi graphs,
   - echo-state networks matched for node/edge count and spectral radius.
5. Move to a public plasma diagnostic dataset and test next-step prediction plus transition/disruption classification.

## Evaluation

- walk-forward or shot-held-out splits
- NRMSE and prediction horizon for forecasting
- AUROC/AUPRC plus lead time for transitions
- linear memory capacity
- robustness to edge deletion, input noise, and uncertain edge signs
- parameter count, compute, and sensitivity to spectral-radius scaling

A positive result requires consistent out-of-sample gains over null graphs. A negative result is informative if the comparison is controlled.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
pytest
python -m connectome_plasma.demo
```

To query neuPrint, set `NEUPRINT_TOKEN` in your environment. Never commit the token.

## ESP32 display

Modeling runs on a laptop/server. A reduced activity field or graph mode can be streamed over serial/WebSocket to an ESP32 driving a 16x16 WS2812B matrix. The display is instrumentation, not the compute engine.

## Status

Cold-start scaffold. The demo is deliberately small and runnable; connectome and plasma data loaders are interfaces, not fabricated datasets.

## Data credit

Male CNS data: FlyEM at HHMI Janelia, Cambridge Connectomics Group, Google Research, and collaborators. See https://male-cns.janelia.org/ and follow dataset citation/license terms.

## License

MIT for code in this repository. External datasets retain their own terms.
