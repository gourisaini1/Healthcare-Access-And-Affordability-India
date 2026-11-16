# State-wise infant mortality rate (IMR), 2023

## Indicator
Infant deaths per 1,000 live births.

## Coverage
State/UT observations for calendar year 2023, plus the all-India aggregate. Daman & Diu is not separately available in the source for 2023; the Dadra & Nagar Haveli value is reported jointly for Dadra & Nagar Haveli and Daman & Diu.

## Source
Reserve Bank of India, *Handbook of Statistics on Indian States 2024–25*, Table 4: State-wise Infant Mortality Rate, data sourced from Sample Registration System (SRS) Bulletin, Office of the Registrar General and Census Commissioner, Ministry of Home Affairs.

Official table: https://www.rbi.org.in/scripts/PublicationsView.aspx?id=23453

## Fields
- `state_ut`: State, Union Territory, or national aggregate as named in the source.
- `infant_mortality_rate_2023_per_1000_live_births`: IMR for 2023. Blank means not separately available.
- `reference_year`: Calendar year of observation.
- `notes`: Source-specific qualification.

## Important limitations
1. This is a 2023 health outcome dataset, not 2024–25 data.
2. IMR is a population-level outcome and does not measure access to care directly.
3. The 2023 DNH figure includes Daman & Diu; do not treat these as two independent observations.
4. The all-India row must be excluded from state-level averages and correlations.
5. Association between health expenditure and IMR does not establish causality. Time alignment, demographic factors, income, sanitation, nutrition and other confounders matter.

## Citation
Reserve Bank of India. (2025). *Handbook of Statistics on Indian States 2024–25*, Table 4. SRS Bulletin, Office of the Registrar General and Census Commissioner, Ministry of Home Affairs.
