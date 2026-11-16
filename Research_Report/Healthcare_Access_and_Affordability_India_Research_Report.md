# Healthcare Access and Affordability in India
## Research report

**Author:** Gouri Saini  
**Discipline:** Economics / Health Economics  
**Evidence cut-off:** 16 November 2026

---

## Executive summary

This project examines healthcare financing, state-level public health budget priorities, selected health outcomes and public healthcare infrastructure in India. It combines national National Health Accounts (NHA) time-series indicators with state/UT data from the Reserve Bank of India (RBI) and the Sample Registration System (SRS).

The central finding from the national NHA series is that the out-of-pocket expenditure (OOPE) share of total health expenditure declined from 64.2% in 2013–14 to 42.7% in 2023–24, while the government health expenditure share rose from 28.6% to 43.5%. These figures describe the composition of health financing; they do not on their own establish how much financial hardship households experience or whether access improved equally across states.

For state comparisons, RBI Statement 27 reports 2024–25 Revised Estimates (RE) of expenditure on Medical and Public Health and Family Welfare as a share of aggregate state expenditure. Among the 31 states/UTs in the dataset, the unweighted mean is 6.1% and the median is 5.9%. Delhi has the highest reported share (12.3%) and Punjab the lowest (3.0%). This is a budget-composition indicator, not per-capita expenditure or health-system performance.

The project also examines state-wise infant mortality in 2023 and government hospital/bed counts reproduced in RBI's 2024–25 Handbook. The RBI hospital table does not state a distinct observation year, so it is not labelled as 2024–25 data.

An exploratory correlation between the 2024–25 RE health budget share and 2023 infant mortality across 31 matched states/UTs is 0.044 (Pearson). This is close to zero for this particular pair of measures. It is not a causal estimate and should not be interpreted as evidence that public spending is ineffective: the years differ, the budget share is not per-capita spending, and the analysis does not control for socioeconomic or demographic factors.

## 1. Research question and motivation

Healthcare access and affordability are important dimensions of economic welfare. High direct payments at the point of service can expose households to financial risk, while geographic and institutional inequalities can constrain access even when aggregate health expenditure increases.

The project asks:

1. How has India's healthcare financing mix changed over time?
2. How do states/UTs differ in the share of aggregate expenditure allocated to Medical and Public Health and Family Welfare?
3. How do selected health outcomes, particularly infant mortality, vary across states?
4. What can available public hospital and bed counts tell us about the distribution of public infrastructure?
5. Is the state health-budget share associated with infant mortality in a simple cross-sectional comparison?

## 2. Data and sources

| Dataset | Reference period | Source | Use |
|---|---|---|---|
| National health financing indicators | 2013–14 to 2023–24 | NHSRC / Ministry of Health and Family Welfare, National Health Accounts | National financing trends |
| State health expenditure share | 2023–24 and 2024–25 RE | RBI, State Finances: A Study of Budgets 2025–26, Statement 27 | State budget composition |
| Infant mortality rate | Calendar year 2023 | SRS, reproduced in RBI Handbook of Statistics on Indian States 2024–25, Table 4 | Health outcome comparison |
| Government hospitals and beds | Reference year not specified in RBI table | National Health Profile, reproduced in RBI Handbook 2024–25, Table 17 | Public infrastructure description |

The data files and definitions are stored in the `Dataset/` directory. Source links and detailed field notes are included in the data dictionaries.

## 3. Methodology

The analysis uses:
- Descriptive time-series comparisons for national NHA indicators.
- State/UT ranking and summary statistics for 2024–25 RE health expenditure shares.
- State/UT comparisons of infant mortality and public hospital/bed counts.
- A simple Pearson correlation between the 2024–25 RE expenditure share and 2023 infant mortality.

The correlation is calculated only after matching state/UT labels. The matched sample contains 31 observations. The all-India IMR aggregate is excluded. The combined Dadra & Nagar Haveli and Daman & Diu observation is not treated as two independent observations.

## 4. Findings

### 4.1 National healthcare financing

| Indicator | 2013–14 | 2023–24 | Change |
|---|---:|---:|---:|
| Government health expenditure share | 28.6% | 43.5% | +14.9 percentage points |
| Out-of-pocket expenditure share | 64.2% | 42.7% | −21.5 percentage points |

The financing mix shifted toward a larger government share and a smaller direct household payment share over the period. OOPE nevertheless remained a substantial component of total health expenditure in 2023–24.

The per-capita NHA series is reported at current prices. It is not adjusted for inflation and should not be described as real growth without an appropriate deflator.

### 4.2 State health expenditure shares, 2024–25 RE

Across the 31 observations in the state dataset:
- Mean: 6.1%.
- Median: 5.9%.
- Highest: NCT Delhi, 12.3%.
- Lowest: Punjab, 3.0%.

The indicator is Medical and Public Health and Family Welfare expenditure as a percentage of aggregate expenditure. State fiscal structures and the size of the expenditure denominator differ. It is not an absolute spending measure, a per-capita measure, or a measure of service quality.

### 4.3 Infant mortality

The 2023 SRS-based table records substantial state variation. In the dataset, Kerala's IMR is 5 deaths per 1,000 live births, while Chhattisgarh, Madhya Pradesh and Uttar Pradesh each record 37. IMR is shaped by multiple determinants, including maternal health, nutrition, sanitation, education, income and access to timely care.

### 4.4 Public hospital infrastructure

The RBI table reports state/UT counts of government hospitals and beds, including rural/urban splits where available. These are absolute counts. A larger absolute bed count does not necessarily mean better availability relative to population, and the source table does not identify a distinct observation year. The current project therefore does not claim to have produced a definitive beds-per-capita comparison.

### 4.5 Exploratory expenditure–IMR association

The Pearson correlation between 2024–25 RE health expenditure share and 2023 IMR is 0.044 across 31 matched observations.

This near-zero linear correlation applies only to these two variables, this sample and these mismatched reference periods. It does not estimate the causal impact of government expenditure on health outcomes. A more credible econometric design would require multiple years of comparable state-level data and controls such as per-capita income, maternal education, sanitation, nutrition, urbanisation, fertility, workforce availability and health infrastructure.

## 5. Interpretation for health economics and public policy

The national NHA trend is consistent with a shift in the financing composition toward government expenditure and away from direct household payments. However, the persistence of a substantial OOPE share indicates that financial protection remains an important subject for further analysis.

State budget shares can reveal differences in fiscal priorities, but they must be interpreted alongside state income, population, fiscal capacity, actual expenditure and delivery outcomes. Budget allocations do not automatically translate into accessible or high-quality services.

The state variation in IMR highlights the importance of considering broader social determinants alongside healthcare resources. The exploratory correlation does not provide evidence for a simple one-variable relationship between budget shares and infant mortality.

## 6. Limitations

1. The datasets do not all refer to the same year. In particular, 2024–25 RE expenditure is compared with 2023 IMR.
2. Revised Estimates are not final audited accounts.
3. Health expenditure as a percentage of aggregate expenditure is not expenditure per person or as a percentage of GSDP.
4. The hospital/bed table does not specify a distinct observation year.
5. Hospital/bed counts are absolute and not adjusted for population.
6. The current analysis does not include state-level private infrastructure, facility utilisation, quality, waiting time or travel distance.
7. The analysis is based on secondary administrative and survey data, each with its own coverage and reporting limitations.
8. The correlation is descriptive and does not control for confounding variables or establish causality.
9. The national NHA per-capita expenditure series is at current prices and is not inflation-adjusted.

## 7. Further research

The next empirical extension should:
- Add population projections matched to the hospital/bed observation period and label them as projections.
- Calculate indicative beds per 1,000 projected population only when the reference-year mismatch is clearly disclosed.
- Extract and analyse the RBI Table 16 doctors and specialists data, preserving each year and facility type.
- Add state-level socioeconomic controls and use a multi-year panel if comparable observations can be assembled.
- Expand affordability analysis with household survey data on medical expenditure, consumption and catastrophic health spending.

## 8. Conclusion

The project documents changes in India's healthcare financing composition and differences across states in budgetary health expenditure, infant mortality and public hospital infrastructure. It demonstrates how public economic and health datasets can be combined for exploratory health economics research, while also showing why differences in definitions, coverage and reference periods matter.

The evidence supports further investigation of state-level financial protection and service availability. It does not support causal claims about the effect of expenditure on health outcomes. A more rigorous panel analysis with population-adjusted resources and socioeconomic controls is the appropriate next step.

## References

1. National Health Systems Resource Centre, Ministry of Health and Family Welfare. *National Health Accounts Estimates for India 2023–24*. https://nhsrcindia.org/national-health-accounts-records
2. Reserve Bank of India. *State Finances: A Study of Budgets of 2025–26*, Statement 27. https://www.rbi.org.in/scripts/PublicationsView.aspx?id=23736
3. Reserve Bank of India. *Handbook of Statistics on Indian States 2024–25*, Table 4: State-wise Infant Mortality Rate. https://www.rbi.org.in/scripts/PublicationsView.aspx?id=23453
4. Reserve Bank of India. *Handbook of Statistics on Indian States 2024–25*, Table 16: State-wise Health Infrastructure – Doctors and Specialists. https://www.rbi.org.in/scripts/PublicationsView.aspx?id=23465
5. Reserve Bank of India. *Handbook of Statistics on Indian States 2024–25*, Table 17: State-wise Number of Government Hospitals and Beds. https://www.rbi.org.in/scripts/PublicationsView.aspx?id=23466
6. Reserve Bank of India. *Handbook of Statistics on Indian States 2024–25*, Table 18: State-wise Public Expenditure on Health. https://www.rbi.org.in/scripts/PublicationsView.aspx?id=23467
7. Ministry of Health and Family Welfare / Central Bureau of Health Intelligence. *National Health Profile 2023*. https://cbhidghs.mohfw.gov.in/WriteReadData/l892s/Final_Central%20Bureau%20of%20Health%20Intelligene%20July%202024.pdf
