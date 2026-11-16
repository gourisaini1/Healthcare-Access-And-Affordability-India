# Dataset: National Health Accounts — India

## Coverage
National-level health financing indicators for financial years 2013–14 to 2023–24.

## Source
National Health Systems Resource Centre (NHSRC), Ministry of Health and Family Welfare, Government of India, *National Health Accounts Estimates for India 2023–24* (published 2026), Table 1, page 40.

Official report: https://nhsrcindia.org/sites/default/files/2026-11/NHA%20Report%202023-24.pdf  
Official NHA reports page: https://nhsrcindia.org/national-health-accounts-records

## Variables
- `financial_year`: Financial year.
- `total_health_expenditure_gdp_pct`: Total health expenditure as a percentage of GDP. The report uses the 2011–12 GDP base through 2021–22 and the 2022–23 GDP base for 2022–23 and 2023–24; interpret the series with this break in mind.
- `ghe_share_total_health_expenditure_pct`: Government health expenditure as a percentage of total health expenditure.
- `oope_share_total_health_expenditure_pct`: Out-of-pocket expenditure as a percentage of total health expenditure.
- `social_security_health_share_total_health_expenditure_pct`: Social security expenditure on health as a percentage of total health expenditure.
- `private_health_insurance_share_total_health_expenditure_pct`: Private health insurance expenditure as a percentage of total health expenditure.
- `total_health_expenditure_per_capita_current_inr`: Total health expenditure per capita at current prices, in INR.

## Important limitations
1. This is a national-level time series, not a state-level or household-level microdataset.
2. The latest National Health Accounts observation currently published in the official NHSRC archive is 2023–24. It must not be relabelled as 2024–25.
3. The GDP percentage series has a stated GDP-base change from 2022–23 onward. Avoid interpreting the entire series as perfectly continuous without noting this.
4. Values are transcribed from the report's Table 1. Please consult the source report for definitions and methodological refinements.

## Reproducibility
The accompanying notebook loads this CSV directly from the repository and creates charts from the published values.
