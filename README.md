# Safety and Rollback Mechanisms for Objective Misinterpretation in Agentic AI Systems

### An Experimental Benchmark for Objective Uncertainty, Risk-Aware Decisions, and Rollback-Based Recovery

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![NumPy](https://img.shields.io/badge/NumPy-2.4.6-blue?logo=numpy)
![Pandas](https://img.shields.io/badge/Pandas-2.2.3-green?logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.10-orange?logo=python)
![Research](https://img.shields.io/badge/Project-Research%20Implementation-purple)

---

## 1. Project Overview

Agentic AI systems can make decisions and execute actions with limited human intervention. However, these systems may misunderstand user objectives, act on incomplete information, or select actions that produce unintended consequences.

This project investigates how objective uncertainty, action impact, reversibility, and rollback mechanisms can be considered together when evaluating the safety of AI-driven decisions.

The project implements a controlled simulation benchmark to compare three decision-making policies:

1. Fixed-threshold decision-making with rollback.
2. Fixed-threshold decision-making without rollback.
3. Risk-aware decision-making with rollback.

The objective is to study how these policies affect residual harm, intervention frequency, and false-positive rates under simulated conditions.

**Important:** This is an experimental simulation-based research implementation. It does not claim to provide a production-ready safety mechanism for real-world autonomous agents.

## 2. Research Problem

An AI agent may correctly execute an action while incorrectly interpreting the objective behind the user's instruction.

For example, an agent asked to clean up a computer system might delete files that the user actually intended to preserve.

Such situations raise three important questions:

- How should an agent account for uncertainty about the intended objective?
- Should the potential impact and reversibility of an action influence its risk assessment?
- Can rollback mechanisms reduce the harm caused by an unsafe decision?

This project explores these questions through a reproducible experimental benchmark.

## 3. Research Objectives

The main objectives are:

- Model uncertainty in interpreting an intended objective.
- Incorporate action impact and reversibility into a risk calculation.
- Implement multiple decision-making policies.
- Simulate harmful outcomes and rollback-based recovery.
- Compare policies using quantitative evaluation metrics.
- Analyze the trade-off between reducing harm and avoiding unnecessary interventions.

## 4. Risk Assessment Model

The project uses the following composite risk equation:

\[
R(a)=I(a)\times U(a)\times(1-\rho(a))
\]

Where:

| Symbol | Meaning |
|---|---|
| \(I(a)\) | Impact of the action |
| \(U(a)\) | Objective uncertainty |
| \(\rho(a)\) | Reversibility of the action |
| \(R(a)\) | Estimated action risk |

All three input values are normalized between 0 and 1.

A high-impact action with high objective uncertainty and low reversibility receives a higher risk score.

The risk score is used by the risk-aware policy to decide whether intervention is required.

## 5. Rollback and Recovery Model

The simulator models initial harm and the effect of rollback.

**Initial harm:**

\[
H_{\text{initial}}=I\times Y
\]

**Recovered harm:**

\[
H_{\text{recovered}}=
H_{\text{initial}}\times f\times\rho
\]

**Residual harm:**

\[
H_{\text{residual}}=
H_{\text{initial}}-H_{\text{recovered}}
\]

Where:

- \(Y\) represents the simulated harmful outcome.
- \(f\) represents the assumed recovery fraction.
- \(\rho\) represents action reversibility.

The recovery fraction is set to 0.80 in the simulator. This is an experimental assumption, not a measured real-world recovery rate.

## 6. Decision-Making Policies

The implementation compares three policies.

| Policy | Risk assessment | Rollback |
|---|---|---|
| Fixed threshold with rollback | Uncertainty score | Enabled |
| Fixed threshold without rollback | Uncertainty score | Disabled |
| Risk-aware with rollback | Composite risk score | Enabled |

Each policy is evaluated using the same experimental dataset and evaluation framework.

## 7. Dataset and Experimental Setup

The project uses a synthetic benchmark containing 600 simulated episodes across six scenario families.

The dataset is divided into:

| Dataset split | Episodes |
|---|---:|
| Development | 360 |
| Validation | 120 |
| Test | 120 |
| **Total** | **600** |

The partitions are grouped by scenario templates to prevent template overlap between splits.

The benchmark includes:

- Episode identifiers
- Action impact
- Objective uncertainty
- Action reversibility
- Simulated harmful outcomes

The dataset is synthetic and should not be interpreted as evidence of real-world agent performance.

## 8. Evaluation Metrics

The following metrics are used to compare the policies:

**Mean Residual Harm:** Measures the average harm remaining after any simulated recovery.

**Intervention Rate:** Measures the proportion of episodes in which a policy triggers intervention.

**False-Positive Rate:** Measures the proportion of non-harmful episodes that trigger intervention.

**Rollback Rate:** Measures the proportion of episodes in which rollback is attempted.

These metrics help evaluate the trade-off between safety and unnecessary intervention.

## 9. Experimental Results

The following results were obtained on the 120-episode test split.

| Policy | Mean Residual Harm | Intervention Rate | False-Positive Rate |
|---|---:|---:|---:|
| Fixed threshold with rollback | 0.0568 | 46.67% | 44.76% |
| Fixed threshold without rollback | 0.0644 | 46.67% | 44.76% |
| Risk-aware with rollback | 0.0621 | 38.33% | 36.19% |

### Key Observations

1. Fixed-threshold decision-making with rollback achieved the lowest mean residual harm.
2. Risk-aware decision-making reduced intervention frequency.
3. Risk-aware decision-making also achieved a lower false-positive rate.
4. Rollback reduced residual harm compared with the corresponding fixed-threshold policy without rollback.

### Interpretation

The results indicate a trade-off between minimizing residual harm and reducing unnecessary interventions.

The fixed-threshold policy with rollback achieved the lowest residual harm, while the risk-aware policy achieved lower intervention and false-positive rates.

Therefore, no single policy can be considered universally superior based on these experiments.

These findings are descriptive results from one synthetic test split, not statistical proof of general performance.

## 10. Repository Structure

```text
AITR_Lab02_Objective_Uncertainty/
│
├── README.md
├── requirements.txt
├── .gitignore
├── SUBMISSION_CHECKLIST.md
│
├── configs/
│   └── experiment.json
│
├── data/
│   ├── README.md
│   ├── generated/
│   │   └── scenarios.csv
│   └── splits/
│       ├── development.csv
│       ├── validation.csv
│       └── test.csv
│
├── notebooks/
│   └── ATR.ipynb
│
├── src/
│   ├── simulator.py
│   ├── policies.py
│   └── evaluation.py
│
├── scripts/
│   ├── check_dataset.py
│   ├── run_experiment.py
│   └── generate_figures.py
│
├── tests/
│   └── test_benchmark.py
│
├── results/
│   ├── raw/
│   ├── summary/
│   ├── reproduced/
│   └── figures/
│
├── paper/
│   ├── FINAL_PROMPTS_01_18_AND_SUBMISSION_REPORT.md
│   ├── FINAL_PROMPTS_01_18_AND_SUBMISSION_REPORT.pdf
│   ├── objective_uncertainty_results_report.pdf
│   └── research_decisions.md
│
└── docs/
    ├── ai_assistance_log.md
    ├── baseline_validation.md
    └── prompt_outputs_01_18.md
```

## 11. Technologies Used

- **Python:** Main implementation language.
- **NumPy:** Numerical operations.
- **Pandas:** Dataset processing and analysis.
- **Matplotlib:** Experimental result visualization.
- **Jupyter Notebook:** Interactive experimentation.
- **Unit Testing:** Validation of benchmark functionality.
- **Git and GitHub:** Version control and project documentation.

## 12. Installation and Execution

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Navigate to the project folder

```bash
cd AITR_Lab02_Objective_Uncertainty
```

### Step 3: Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### Step 4: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Validate the dataset

```bash
python scripts/check_dataset.py
```

### Step 6: Run the experiments

```bash
python scripts/run_experiment.py
```

### Step 7: Generate result visualizations

```bash
python scripts/generate_figures.py
```

### Step 8: Run unit tests

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

The scripts use the prepared dataset and saved experimental thresholds. Running them reproduces the evaluation and figures; it does not independently regenerate the original synthetic dataset or repeat the original threshold-selection process.

## 13. Project Limitations

This project has several limitations:

- The experiments use synthetic data rather than real-world agent interaction logs.
- The recovery fraction of 0.80 is an assumed simulation parameter.
- Only three decision-making policies are compared.
- The test set contains 120 episodes.
- Results are descriptive and require further statistical evaluation.
- The experiment does not demonstrate integration with a production agent or an actual rollback infrastructure.
- The test results were viewed during the research workflow; therefore, the test set should not be described as completely untouched.

These limitations define important directions for future work.

## 14. Future Scope

Possible future improvements include:

- Testing the framework with real agent environments.
- Developing more realistic objective-misinterpretation scenarios.
- Implementing adaptive risk thresholds.
- Exploring uncertainty estimation using machine learning models.
- Evaluating rollback under partial and irreversible failures.
- Conducting repeated experiments with multiple random seeds.
- Adding statistical significance testing and confidence intervals.
- Integrating the framework with an actual agent execution environment.

## 15. Research Contribution

This implementation provides a controlled experimental comparison of decision policies that consider objective uncertainty, action impact, reversibility, and rollback-based recovery.

Its primary contribution is an experimental framework for studying the relationship between residual harm and intervention costs under different safety policies.

The findings provide a starting point for further research into safer decision-making in agentic AI systems.

## 16. Author and Academic Information

**Project Title:** Safety and Rollback Mechanisms for Objective Misinterpretation in Agentic AI Systems

**Course:** AI Tools for Research

**Project Type:** Research Implementation and Experimental Evaluation

**Repository:** Objective Uncertainty and Rollback Benchmark

---

*This repository is intended for academic research, experimentation, and educational purposes. Results should be interpreted within the limitations of the synthetic benchmark.*
