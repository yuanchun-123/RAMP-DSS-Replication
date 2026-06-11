# Output Mapping

| Manuscript element | Output file | Description |
|---|---|---|
| Table: Sample Construction | `outputs/tables/table1_sample_construction.csv` | Rows retained through the benchmark sample construction steps |
| Table: Selection-Adjusted Benchmark | `outputs/tables/table2_main_ate_24h.csv` | Main 24-hour selection-adjusted benchmark summary |
| Table: Reliability Diagnostics | `outputs/tables/table3_overlap_diagnostics.csv` | Propensity overlap and benchmark support diagnostics |
| Table: Nuisance Diagnostics | `outputs/tables/table4_nuisance_diagnostics.csv` | Predictive checks for nuisance components used by the benchmark |
| Table: Horizon Robustness | `outputs/tables/table5_horizon_robustness.csv` | Diagnostic sensitivity across alternative evaluation horizons |
| Table: Trim Robustness | `outputs/tables/table6_trim_robustness.csv` | Diagnostic sensitivity to overlap trimming rules |
| Table: Campaign Reprioritization | `outputs/tables/table_dss_reprioritization_metrics.csv` | Rank correlations, rank shifts, and top-k overlap metrics |
| Figure: Propensity Overlap | `outputs/figures/figure_propensity_overlap_24h.png` | Estimated click-propensity distribution for the benchmark sample |
| Figure: Diagnostic vs Last-Touch Ranking | `outputs/figures/fig_dss_rank_scatter_diagnostic_vs_last_touch.png` | Scatter plot comparing diagnostic and last-touch rankings |
| Figure: Diagnostic vs Click Ranking | `outputs/figures/fig_dss_rank_scatter_diagnostic_vs_click.png` | Scatter plot comparing diagnostic and click-based rankings |
| Figure: Diagnostic vs Exposure Ranking | `outputs/figures/fig_dss_rank_scatter_diagnostic_vs_exposure.png` | Scatter plot comparing diagnostic and exposure-based rankings |
| Table: Diagnostic Gate Funnel | `outputs/tables/table_dss_gate_funnel.csv` | Campaign screening funnel |
| Figure: Diagnostic Gate Funnel | `outputs/figures/fig_dss_gate_funnel.png` | Visualization of screening attrition |
| Table: Decision-Risk Classification | `outputs/tables/table_dss_decision_risk_classification.csv` | Campaign-level risk classes from diagnostic disagreement |
| Figure: Decision-Risk Matrix | `outputs/figures/fig_dss_decision_risk_matrix.png` | Visual summary of diagnostic disagreement and campaign decision risk |
| Table: Time-Split Decision Simulation | `outputs/tables/table_dss_time_split_decision_simulation.csv` | Future-period diagnostic evaluation |
| Figure: Time-Split Decision Simulation | `outputs/figures/fig_dss_time_split_decision_simulation.png` | Visualization of future diagnostic performance |

The table files are generated locally and are ignored by default because they
are CSV outputs derived from the Criteo data. Figure files may be included when
they do not expose row-level raw data.

