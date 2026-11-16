# Healthcare Access and Affordability in India

**An exploratory health-economics research project using official Indian public data**

This repository examines national health financing, state-level public health budgets, rural primary-care staffing, infant mortality and government hospital-bed availability. It combines National Health Accounts time series with state-level fiscal, workforce, socioeconomic and health-outcome indicators.

> **Research boundary:** this is a secondary-data, descriptive and correlational study. It does not estimate causal effects. National out-of-pocket expenditure (OOPE) shares are financing aggregates, not direct household-level measures of catastrophic health expenditure.

## Key findings

- India's OOPE share of total health expenditure fell from **64.2% in 2013–14 to 42.7% in 2023–24** (−21.5 percentage points). The government health expenditure share rose from **28.6% to 43.5%** (+14.9 percentage points).
- Across 31 states/UTs, the 2024–25 Revised Estimate for Medical and Public Health and Family Welfare averaged **6.1% of aggregate expenditure** (median 5.9%). This is a budget-composition measure, not spending per person or health-system performance.
- In the 2023 rural PHC staffing table, **10 of 34 matched states/UTs** with a calculable staffing ratio were below the reported doctor requirement; 24 were at or above it. The median in-position-to-required ratio was **1.38**.
- In the full 34-state/UT bivariate sample, the staffing ratio and 2023 infant mortality had Pearson r = **−0.538** and Spearman rho = **−0.562**. Excluding observations with fewer than 50 required PHC doctors (27 observations) gives Pearson r = **−0.498** and Spearman rho = **−0.368**.
- **Adjusted workforce–IMR association (32 complete cases): results depend on specification.** With the original unlogged staffing ratio and socioeconomic controls, the coefficient is **−3.40** (HC3 p = 0.211). Using the log staffing ratio as the main specification gives **−7.62** (HC3 p = 0.0345; 95% CI −14.68 to −0.56). In the restricted sample with at least 50 required PHC doctors (n = 27), the log-ratio coefficient is **−10.87** (p = 0.0076), while the corresponding linear-ratio coefficient is **−7.79** (p = 0.0042). Jointly excluding Goa and Delhi from the full log-ratio model gives **−11.25** (n = 30; p = 0.0021). Leave-one-state/UT-out log-ratio estimates range from **−9.07 to −5.77**; some exclusions make the p-value exceed 0.05. The log specification is preferred because the raw staffing ratio is heavily right-skewed, but functional form and sample composition matter. These are exploratory associations, not causal effects.
- Government hospital beds per 1,000 projected population (NHP-2023 bed counts, 31 Dec 2022, divided by NHP projected population as of 1 Mar 2021) have a state/UT median of **0.949** and mean of **1.285**. This is government-sector capacity only and uses a population denominator about 21 months earlier.

## Research questions and evidence coverage

| Research question | Evidence in this repository | Status |
|---|---|---|
| How has India's healthcare financing mix changed? | NHA national time series, 2013–14 to 2023–24 | Answered descriptively |
| How do states differ in public health budget priority? | RBI state expenditure shares, 2023–24 and 2024–25 RE | Answered descriptively |
| How does rural PHC doctor staffing compare with the stated requirement? | RBI Table 16, 2023 | Answered descriptively |
| Is rural PHC doctor staffing associated with infant mortality? | Same-year 2023 staffing and SRS IMR, 34 matched states/UTs | Bivariate and exploratory adjusted analysis |
| Does the staffing association persist after socioeconomic controls? | 2021–22 per-capita NSDP and NFHS-5 female literacy, 2019–21; linear/log staffing ratio and influence sensitivities | Exploratory; direction is negative, but magnitude and significance depend on specification and sample |
| How do government hospital beds vary after population adjustment? | NHP-2023 bed counts and 2021 projected population | Answered descriptively; timing/source consistency caveats |
| What is the household incidence of catastrophic health expenditure? | Not measured by NHA aggregates | Not answered; requires household microdata |
| How do rural and urban households differ in utilisation and affordability? | Not measured in current state aggregates | Not answered; requires household/facility-level data |

## Conceptual framework

Healthcare financing affects resources available to providers and the extent of financial risk borne by households. Health-system capacity (including rural PHC staffing and hospital beds) is one channel through which resources may translate into service availability. Population health outcomes such as infant mortality are also shaped by nutrition, sanitation, maternal education, income, fertility, transport and wider state capacity.

This framework motivates the empirical comparisons but does not imply that the available data identify each causal pathway.

## Data sources

| Dataset | Period / unit | Source and role |
|---|---|---|
| National Health Accounts indicators | India, FY2013–14 to FY2023–24 | NHSRC / MoHFW; financing mix and OOPE |
| State public health expenditure share | 31 states/UTs, FY2023–24 and FY2024–25 RE | RBI *State Finances: A Study of Budgets 2025–26*, Statement 27 |
| Infant mortality rate | State/UT, calendar 2023 | SRS, reproduced in RBI *Handbook of Statistics on Indian States 2024–25*, Table 4 |
| Rural PHC doctor staffing | State/UT, calendar 2023 | RBI *Handbook of Statistics on Indian States 2024–25*, Table 16 |
| Per-capita NSDP | State/UT, FY2021–22, current prices | RBI *Handbook of Statistics on Indian States 2023–24*, Table 26 |
| Female literacy | Women aged 15–49, NFHS-5 2019–21 | IIPS / MoHFW, NFHS-5 India Report, Table 3.4.1 |
| Government hospital beds | State/UT, 31 Dec 2022 | CBHI, *National Health Profile 2023*, Table 6.2.2 |
| Population denominator for beds | State/UT, projected 1 Mar 2021 | CBHI, *National Health Profile 2023*, Table 1.1.2(d) |

Official references:
- [National Health Accounts, NHSRC](https://nhsrcindia.org/national-health-accounts-records)
- [RBI State Finances 2025–26, Statement 27](https://www.rbi.org.in/scripts/PublicationsView.aspx?id=23736)
- [RBI Handbook 2024–25, Table 4: Infant Mortality Rate](https://www.rbi.org.in/scripts/PublicationsView.aspx?id=23453)
- [RBI Handbook 2024–25, Table 16: Doctors and Specialists](https://www.rbi.org.in/Scripts/PublicationsView.aspx?id=23465)
- [RBI Handbook 2023–24, Table 26: Per-capita NSDP](https://nhm.tn.gov.in/wp-content/uploads/2026/Key_Statistics/RBI/RBI%20Statistics%20Handbook%202023-24.pdf)
- [NFHS-5 India Report, Table 3.4.1](https://dhsprogram.com/pubs/pdf/FR375/FR375.pdf)
- [National Health Profile 2023, CBHI](https://cbhidghs.mohfw.gov.in/sites/default/files/NHP/NHP-2023-Last-Final.pdf)

## Analysis and visualisations

### 1. National healthcare financing, 2013–14 to 2023–24

![Government and out-of-pocket shares](Visualisations/01_financing_shares.svg)

The OOPE share declined while the government share increased. These figures describe the source of health financing, not the distribution of financial hardship across households.

### 2. State public health expenditure share, 2024–25 RE

![State public health expenditure share](Visualisations/05_state_health_expenditure_share_2024_25_RE.svg)

The variable is Medical and Public Health and Family Welfare expenditure as a percentage of aggregate state expenditure. Revised Estimates are not audited actuals. The percentage does not show absolute rupees, per-capita expenditure, expenditure as a share of GSDP or service quality.

### 3. Rural PHC doctor staffing and infant mortality, 2023

![Rural PHC staffing ratio and infant mortality](Visualisations/09_rural_phc_staffing_vs_imr.svg)

Notebook 06 constructs the ratio: `in-position rural PHC doctors / required rural PHC doctors`. The denominator is the source-reported administrative requirement (approximately one doctor per PHC), not population need. A ratio of 2 means about twice the benchmark post count—not twice the doctors the population needs. Small denominators can inflate ratios; the notebook reports a sensitivity sample excluding requirements below 50.

### 4. Adjusted workforce–IMR regression

![Adjusted and unadjusted staffing coefficient](Visualisations/11_adjusted_regression_staffing_coefficient.svg)

Notebook 07's main adjusted specification uses the natural log of the staffing ratio because the raw in-position-to-required ratio is heavily right-skewed; logging compresses unusually high values in the upper tail. It controls for log per-capita NSDP (2021–22) and NFHS-5 female literacy among women aged 15–49 (2019–21), with HC3 heteroskedasticity-robust standard errors. On the 32-state/UT complete-case sample, the log-ratio staffing coefficient is **−7.62** (HC3 p = **0.0345**, 95% CI **−14.68 to −0.56**). The original linear-ratio adjusted model on the same sample gives **−3.40** (HC3 p = **0.2114**, 95% CI **−8.72 to 1.93**).

The specification and sample checks are reported separately:

| Specification | n | Staffing coefficient | HC3 p-value |
|---|---:|---:|---:|
| Linear ratio, full adjusted sample | 32 | −3.40 | 0.2114 |
| Log ratio, full adjusted sample (main) | 32 | −7.62 | 0.0345 |
| Linear ratio, required PHC doctors ≥ 50 | 27 | −7.79 | 0.0042 |
| Log ratio, required PHC doctors ≥ 50 | 27 | −10.87 | 0.0076 |
| Log ratio, exclude Goa and Delhi jointly | 30 | −11.25 | 0.0021 |

The leave-one-state/UT-out log-ratio coefficients range from **−9.07** (excluding Goa) to **−5.77** (excluding Manipur). Some leave-one-out p-values exceed 0.05, so the result is not uniformly statistically significant under every one-state deletion. These are diagnostics of influence, not grounds for discarding observations. The negative association is present in the main log specification and the two restricted log specifications, but the original linear full-sample model is not statistically distinguishable from zero. The correct conclusion is specification-sensitive evidence of an inverse association, not a causal effect. Omitted confounders, non-contemporaneous controls and the small state/UT sample remain important limitations.

### 5. Government hospital beds per 1,000 population

![Government hospital beds per 1,000 population](Visualisations/10_government_hospital_beds_per_1000.svg)

The numerator is government hospital beds in NHP-2023 Table 6.2.2, dated 31 December 2022. The denominator is projected population from NHP-2023 Table 1.1.2(d), as of 1 March 2021. The approximately 21-month gap is disclosed. The indicator covers government beds only, not private beds, occupancy, staffing, geographic access or quality.

**Maharashtra source check:** NHP-2023 Table 6.2.2 reports 10,920 rural beds and 16,417 urban beds (27,337 total). With the NHP projected population of 124,437 thousand, this is **0.2197 government beds per 1,000 residents**, second-lowest among the 36 state/UT rows (only Bihar is lower), and below Uttar Pradesh (0.3445). The table's notes contain no Maharashtra-specific footnote or adjustment; they define government hospitals as central, state and local government bodies and note that Delhi and Chandigarh have no rural area. The published figure is retained and flagged as an unusual source-reported result, not silently corrected.

**Source-table consistency caveat:** the 36 state/UT bed rows sum to 880,307, while the NHP India aggregate row reports 840,455. The 39,852 difference equals the Andhra Pradesh row. State-level rates use the published state rows; no national rate is calculated from these inconsistent totals.

## Repository structure

```text
.
├── Dataset/
│   ├── *.csv
│   ├── *_DATA_DICTIONARY.md
│   └── README.md
├── Notebooks/
│   ├── 01_National_Health_Accounts_Analysis.ipynb
│   ├── 02_State_Health_Expenditure_Analysis.ipynb
│   ├── 03_Health_Outcomes_and_Expenditure.ipynb
│   ├── 04_State_Hospital_Infrastructure_Analysis.ipynb
│   ├── 05_Correlation_and_Regression_Analysis.ipynb
│   ├── 06_Rural_Workforce_and_Health_Outcomes.ipynb
│   ├── 07_Adjusted_Workforce_IMR_Regression.ipynb
│   └── 08_Government_Hospital_Beds_Per_Capita.ipynb
├── Research_Report/
├── Visualisations/
├── scripts/
└── .github/workflows/
```

There is one canonical notebook directory. The duplicate notebook tree formerly stored under `Dataset/Notebooks/` and a malformed nested README file have been removed.



## How the analysis is built

The repository follows a source-to-result workflow. Source tables are retained as documented CSV files; each notebook imports the relevant files, applies transparent transformations, and produces tables or figures. Derived datasets are not treated as independent primary sources.

| Stage | What happens | Main files |
|---|---|---|
| 1. Source documentation | Record publisher, table number, unit, geography, reference period and known caveats | `Dataset/README.md`, `Dataset/*_DATA_DICTIONARY.md` |
| 2. Data preparation | Read CSVs, standardise state/UT labels, preserve missing values and construct matched samples | Notebooks 01–08 |
| 3. Descriptive analysis | Summarise national trends and compare state/UT distributions | Notebooks 01–04, 08 |
| 4. Association analysis | Calculate correlations and exploratory regression estimates | Notebooks 05–07 |
| 5. Outputs | Save reproducible notebook outputs and publication-style SVG charts | `Visualisations/`, `Notebooks/` |
| 6. Validation | Check source files, joins, notebook syntax and execute the full sequence | `scripts/validate_project.py`, `.github/workflows/validate.yml` |

### Notebook guide

| Notebook | Question / task | Main output |
|---|---|---|
| [01 — National Health Accounts](Notebooks/01_National_Health_Accounts_Analysis.ipynb) | How did the national financing mix change between FY2013–14 and FY2023–24? | Government and OOPE financing trends |
| [02 — State health expenditure](Notebooks/02_State_Health_Expenditure_Analysis.ipynb) | How much of state aggregate expenditure is allocated to Medical and Public Health and Family Welfare? | State/UT comparison of 2024–25 Revised Estimates |
| [03 — Health outcomes and expenditure](Notebooks/03_Health_Outcomes_and_Expenditure.ipynb) | How do infant mortality and state budget shares compare? | State-level descriptive comparison |
| [04 — Hospital infrastructure](Notebooks/04_State_Hospital_Infrastructure_Analysis.ipynb) | How is government hospital infrastructure distributed across states/UTs? | Infrastructure summaries and comparisons |
| [05 — Correlation and regression](Notebooks/05_Correlation_and_Regression_Analysis.ipynb) | Is the state budget-share measure associated with infant mortality? | Pearson/Spearman correlations and simple regression |
| [06 — Rural workforce and outcomes](Notebooks/06_Rural_Workforce_and_Health_Outcomes.ipynb) | How does rural PHC doctor staffing compare with reported requirements, and how does it relate to IMR? | Staffing coverage ratios, bivariate analysis and denominator sensitivity |
| [07 — Adjusted workforce–IMR model](Notebooks/07_Adjusted_Workforce_IMR_Regression.ipynb) | Does the staffing–IMR association remain after income and female-literacy controls? | HC3-adjusted OLS, linear/log specifications, restricted-sample and influence checks |
| [08 — Government beds per capita](Notebooks/08_Government_Hospital_Beds_Per_Capita.ipynb) | How do government hospital beds compare after population adjustment? | Beds per 1,000 projected population |

The notebooks are intended to be read in numerical order. Notebook 07 is the main multivariable analysis; Notebook 08 is a separate infrastructure indicator and should not be interpreted as a measure of actual service access or quality.

## Empirical strategy

The project deliberately separates descriptive indicators from exploratory statistical associations.

### 1. National financing

The National Health Accounts series is used to calculate percentage-point changes in government health expenditure and out-of-pocket expenditure shares. A change in financing composition is not the same as a change in household-level financial hardship.

### 2. State budget composition

The state budget indicator is:

`Medical and Public Health + Family Welfare expenditure / Aggregate expenditure × 100`

The 2024–25 values are Revised Estimates. The measure captures the composition of a state budget; it is not per-capita expenditure, expenditure as a share of GSDP, or a direct measure of quality.

### 3. Rural PHC staffing

For each state/UT with a positive reported requirement:

`Staffing coverage ratio = Rural PHC doctors in position / Rural PHC doctors required`

A ratio below 1 indicates fewer doctors in position than the source-reported requirement. A ratio above 1 indicates more doctors in position than the administrative benchmark. It does not establish that the workforce is sufficient relative to population need, workload or geographic distribution.

### 4. Adjusted workforce–IMR association

The principal outcome is 2023 infant mortality per 1,000 live births. The main staffing predictor is the natural log of the in-position-to-required rural PHC doctor ratio. Controls are log nominal per-capita NSDP at current prices (FY2021–22) and NFHS-5 female literacy among women aged 15–49 (2019–21).

The model is:

`IMRᵢ = β₀ + β₁ log(PHC staffing ratioᵢ) + β₂ log(NSDP per capitaᵢ) + β₃ Female literacyᵢ + εᵢ`

OLS estimates are reported with HC3 heteroskedasticity-robust standard errors. The main adjusted sample contains 32 states/UTs. The two matched observations without a separate 2021–22 NSDP value—Lakshadweep and the combined Dadra & Nagar Haveli and Daman & Diu UT—are excluded rather than imputed.

The log transformation is used because the raw staffing ratio is right-skewed and a few high ratios can exert disproportionate leverage. The unlogged model is retained as a functional-form sensitivity check. Notebook 07 also includes a leave-one-state/UT-out diagnostic and a joint Goa–Delhi exclusion. These checks describe sensitivity; they do not create a causal design.

## Interpreting the regression carefully

The main log-ratio estimate is negative: states/UTs with higher rural PHC staffing relative to the source-reported requirement tend to have lower infant mortality, conditional on the two included controls. The coefficient is measured in IMR deaths per 1,000 live births for a one-unit increase in the natural log of the staffing ratio. It is not an effect per additional doctor.

The linear and log coefficients are not directly comparable because the staffing variables use different scales. A statistically significant coefficient in one specification and a non-significant coefficient in another is evidence that the result is specification-sensitive—not permission to select whichever model produces the preferred p-value.

The leave-one-out analysis is especially important in a sample of 32 observations. The estimates remain negative across the one-at-a-time exclusions, but the uncertainty changes and some exclusions make the p-value cross conventional significance thresholds. The joint exclusion of Goa and Delhi is a targeted sensitivity exercise, not a claim that those observations are invalid.

All results are exploratory and correlational. HC3 standard errors address heteroskedasticity in inference; they do not address omitted variables, measurement error, reverse causality, temporal mismatch or unobserved state differences.

## Data quality and validation

The project includes explicit checks rather than relying only on notebook execution:

- State/UT keys are matched with one-to-one merge validation where applicable.
- Missing source values are not silently converted to zero.
- The PHC staffing denominator must be positive before a staffing ratio is calculated.
- The two adjusted-model exclusions are documented; no missing NSDP values are imputed.
- The hospital-bed calculation checks the units of the population denominator (population in thousands).
- The NHP bed-count reference dates are retained: beds at 31 December 2022 and projected population at 1 March 2021.
- Notebook syntax and key dataset assumptions are checked by `scripts/validate_project.py`.
- GitHub Actions executes all eight notebooks in sequence. Successful runs save executed notebook outputs and generated SVGs to the main branch.

To validate locally from the repository root:

```bash
pip install -r requirements.txt
python scripts/validate_project.py
cd Notebooks
for notebook in *.ipynb; do
  jupyter nbconvert --to notebook --execute "$notebook" --inplace
done
```

If a notebook fails, inspect the first failing cell and its traceback before relying on any downstream output. A successful syntax check alone does not prove that every analysis executed successfully.

## What this project can—and cannot—conclude

**It can describe:**
- the national trend in the composition of health financing;
- differences in state public-health budget shares;
- variation in rural PHC staffing relative to reported administrative requirements;
- state-level associations between staffing coverage and infant mortality;
- differences in government hospital beds per 1,000 projected population.

**It cannot establish from the current data:**
- the share of households pushed into poverty by medical expenses;
- catastrophic health expenditure by income or consumption group;
- whether rural households use fewer services than urban households;
- whether an additional PHC doctor causes infant mortality to fall;
- whether a state with more government beds has better access, occupancy, staffing or quality.

These distinctions are central to the interpretation of the project. The repository does not treat a national OOPE share as a household-level catastrophic expenditure rate, or an administrative staffing ratio as a population-need measure.

## Research roadmap

The next extensions should address the largest evidence gaps in a staged way:

1. **Household financial protection:** add suitable NSS household consumption and health-expenditure microdata; calculate catastrophic expenditure under clearly stated denominators and thresholds, and report sensitivity to alternative definitions.
2. **Distributional analysis:** disaggregate financial burden by consumption group, rural/urban residence and state where survey design permits.
3. **Service utilisation:** add comparable household utilisation measures and distinguish availability, utilisation and affordability.
4. **Panel analysis:** build a consistent multi-year state panel for workforce, health outcomes and socioeconomic conditions before considering fixed-effects or other panel estimators.
5. **Stronger identification:** only make causal claims if a defensible policy change, instrument, discontinuity or other identification strategy is available and its assumptions can be assessed.
6. **Infrastructure quality:** supplement bed counts with occupancy, staffing, facility functionality and travel-time accessibility, rather than treating capacity counts as a complete access measure.

## Research report and supporting documentation

- [Full research report](Research_Report/Healthcare_Access_and_Affordability_India_Research_Report.md)
- [Dataset catalogue and data dictionaries](Dataset/README.md)
- [Notebook guide](Notebooks/README.md)
- [Project status and validation notes](PROJECT_STATUS.md)
- [All generated visualisations](Visualisations/)
- [GitHub Actions validation history](https://github.com/gourisaini1/Healthcare-Access-And-Affordability-India/actions)

## Reproduce the analysis

Python 3.11 is recommended.

```bash
git clone https://github.com/gourisaini1/Healthcare-Access-And-Affordability-India.git
cd Healthcare-Access-And-Affordability-India
python -m venv .venv
# Activate the environment, then:
pip install -r requirements.txt
cd Notebooks
jupyter lab
```

Run notebooks 01–08 in order. Notebooks read source datasets from `../Dataset/`.

GitHub Actions validates datasets, checks notebook syntax and executes all notebooks. Executed notebook outputs are committed only for pushes to `main`; pull-request runs do not attempt to push.

## Limitations and next research steps

1. **Household affordability:** NHA OOPE shares are national aggregates. Catastrophic expenditure, impoverishment due to medical spending and distribution by consumption quintile require household-level NSS/NFHS-compatible data.
2. **Rural–urban access:** the PHC staffing table is rural-specific; the current project does not contain a comparable urban provider dataset or household utilisation data.
3. **Socioeconomic controls and specification sensitivity:** the adjusted workforce–IMR regression includes two controls only. Maternal health, nutrition, sanitation, fertility, urbanisation, transport and health-system quality remain omitted. NFHS-5 literacy and 2021–22 NSDP predate the 2023 outcome and are not exactly contemporaneous. The staffing estimate is sensitive to logging the skewed ratio and to sample exclusions; the leave-one-out analysis is diagnostic, not a substitute for a larger sample or stronger design.
4. **Population adjustment:** the hospital-bed ratio uses a 2021 projected population denominator with 2022 bed counts. The NHP source also has an internal state-row versus national aggregate discrepancy, documented in Notebook 08.
5. **Causal inference:** the analyses are cross-sectional and observational. A causal evaluation would require a defensible identification strategy, not simply a larger regression.

## Project status

**Version 3 exploratory extension.** Eight notebooks now cover national financing, state budgets, rural PHC staffing, an exploratory adjusted regression and population-adjusted government hospital beds. Notebook execution and output saving are validated through GitHub Actions; the latest run status is linked below.

[Latest successful validation and notebook execution](https://github.com/gourisaini1/Healthcare-Access-And-Affordability-India/actions/runs/43895861327) · [All GitHub Actions runs](https://github.com/gourisaini1/Healthcare-Access-And-Affordability-India/actions)

---
**Author:** Gouri Saini | **Field:** Economics / Health Economics
