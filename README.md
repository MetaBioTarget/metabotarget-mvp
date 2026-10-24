# MetaBioTarget AI Platform (MVP)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/your-username/metabotarget-mvp/blob/main/notebooks/MetaBioTarget_QuickStart.ipynb)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)]()

> **Autonomous Multi-Scale Target-Based Drug Discovery & Translational AI Platform.**
> Give it any human target (UniProt Accession or Gene Symbol) $\rightarrow$ get back live multi-scale biophysics, context-adapted predictions, dynamic clinical indications, and virtual human population trials.

---

## 🌟 Key Highlights

- **Zero Hardcoded Data Dictionaries**: Live API queries to **UniProt**, **Human Protein Atlas (HPA)**, **RCSB PDB**, and **Open Targets Platform GraphQL** with transparent offline SQLite caching.
- **Layer 1: The 4 Multi-Scale Biology Levels**:
  - *Level 1 (Molecular)*: Henderson-Hasselbalch charge titration, isoelectric point (pI), cavity geometry, Debye-Hückel potential.
  - *Level 2 (Cellular/Pathway)*: Stiff non-linear Radau ODE numerical integration of second-messenger and receptor trafficking fluxes.
  - *Level 3 (Tissue & Cell-Type)*: Whole-body $n\text{TPM} \to B_{\text{max}}$ expression mapping across human tissues.
  - *Level 4 (Organ PBPK)*: Allometric clearance, steady-state distribution volume, and vascular permeability.
- **Layer 1 Component 2**: 7-Factor Vectorized Context Adapters (Species, Cell Type, Donor, Genotype, Microenvironment, Dose, Timepoint).
- **Layer 1 Component 3**: Gradient-Based Meta-Learner (MAML/Reptile inner/outer loop) with Cross-Species Causal Alignment & Epistemic Uncertainty.
- **Layer 1 Component 4**: Dynamic Multi-Label Indication Classifier with mathematically derived logistic sigmoid scoring ($P = \sigma(Wx + b)$).
- **Phase 9**: Monte Carlo Virtual Human Population PK Trial ($N=150$ to $N=1,000$ virtual subjects) and Dose Regimen Optimization.
- **Phase 12**: Two-Cycle Stress-Testing Closed-Loop Engine (Cycle 1 stress-tests Layer 1; Cycle 2 ingests discrepancy feedback to nail the objective in max 2 cycles).

---

## 🚀 Quick Start in Google Colab (1 Click)

Click the **Open in Colab** badge above or open `notebooks/MetaBioTarget_QuickStart.ipynb`.
The notebook is self-contained, requires **zero GPU**, and runs end-to-end in under 2 minutes on the free tier.

---

## 💻 Local Installation & Usage

### 1. Clone & Install
```bash
git clone https://github.com/your-username/metabotarget-mvp.git
cd metabotarget-mvp
pip install -e .
```

### 2. Command-Line Interface (CLI)

#### Profile a Target (Component 1 Multi-Scale Biology)
```bash
metabotarget profile --target P43220
# Or by gene symbol:
metabotarget profile --target GLP1R
```

#### Run Layer 1 Full Discovery Pipeline
```bash
metabotarget run --target P43220 --threshold 0.45
```

#### Run 2-Cycle Stress-Testing Closed-Loop Discovery
```bash
metabotarget discover --target P43220 --cohort 150
```

#### Run Multi-Target Cross-Indication Portfolio Analysis
```bash
metabotarget portfolio --targets P43220 P02786 P01375 --csv portfolio_ranking.csv
```

---

## 🧪 Automated Test Suite

Run the full automated test suite locally:
```bash
pytest tests/
```

---

## 📁 Repository Structure

```
metabotarget-mvp/
├── src/
│   ├── ingestion/             # Live API connectors (UniProt, HPA, PDB, OpenTargets) + Cache
│   ├── meta_learning/         # Component 1 (4-Scale Engine), Component 2 (FiLM), Component 4 (Classifier)
│   ├── agents/                # Multi-Agent Governance & Non-Placeholder Enforcement
│   ├── translational/         # Virtual Human Population PK & Dose Optimization
│   ├── portfolio/             # Multi-target Pareto ranking & comparative exports
│   ├── orchestration/         # Phase 12 Two-Cycle Stress-Testing Discovery Engine
│   ├── cli.py                 # Unified CLI (`metabotarget`)
│   └── __main__.py            # Module entrypoint (`python -m src`)
├── notebooks/
│   └── MetaBioTarget_QuickStart.ipynb  # Interactive Google Colab Notebook
├── tests/                     # Unit & integration tests
├── pyproject.toml             # Modern PEP 621 packaging
├── setup.py                   # Setup script
├── requirements.txt           # Clean dependencies
├── LICENSE                    # MIT License
└── README.md
```

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
