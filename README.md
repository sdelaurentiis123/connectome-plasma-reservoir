# Connectome Plasma Reservoir

Research scaffold for testing whether a fixed biological connectome is a useful recurrent reservoir for plasma time-series prediction.

## 30-second picture

```text
plasma diagnostic history -> fixed connectome reservoir -> linear readout -> forecast / transition score
                                  |
                                  +-> compare with rewired, random and standard ESN reservoirs
```

The connectome is only the recurrent wiring prior. It is not a simulated fly mind. The experiment asks one clean question: under identical inputs, readout capacity and tuning budget, does that wiring generalize across held-out plasma shots better than honest null graphs?

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
pip install -e ".[dev]"
pytest
python demo.py
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

## Non-negotiable design constraints

1. **Independent N means whole experiments.** Replication and final validation use held-out plasma shots or independent acquisition periods, not windows cut from one trajectory. A time split of one shot is not evidence of cross-shot generalization.
2. **No pseudo-replication.** Re-running deterministic code does not create seeds. State the independent unit and vary genuinely stochastic initializations, graph draws, shots, or campaigns.
3. **Keep physical variables physical.** Geometry-sensitive inputs retain their metric/Jacobian, diagnostic channels use causal timestamps, and no transform may erase units or physical meaning without an explicit test.
4. **Prove state sufficiency before architecture search.** Establish that the chosen diagnostic history contains predictive information for the target before tuning reservoir topology.
5. **Null models are the experiment.** Persistence, linear autoregression/readouts, matched echo-state networks, degree-preserving rewires, and matched random graphs receive the same tuning budget and evaluation.
6. **Fail closed numerically.** NaNs, infinities, singular fits, and undefined metrics invalidate the run. Never zero-fill or clip them and keep a headline metric.
7. **Tests test the math.** Tests check causality, split isolation, reservoir updates, fills, accounting, invariants, and failure modes, not only file existence or schema shape.
8. **One canonical definition per result.** Each target, split, fill, PnL field, and headline metric has one implementation and one recorded provenance.
9. **Launchers are immutable and non-destructive.** Runs write versioned outputs and fail safely. No broad or unconditional `rm -f`; raw data and prior results stay immutable.
10. **A clean clone must reproduce the run.** `requirements-lock.txt` records the exact tested environment. Dependency changes require a new lock and clean-environment test.
11. **Code stays proportional to evidence.** Add infrastructure only when an experiment needs it; do not bury an untested idea under production-shaped code.
12. **Claims track evidence.** Until repeated held-out evidence exists, call this a scaffold or a paper-trading experiment, not an advantage, alpha, or validated biological mechanism.
