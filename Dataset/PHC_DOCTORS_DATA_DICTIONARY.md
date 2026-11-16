# Rural PHC doctors data dictionary

## Source
Reserve Bank of India, *Handbook of Statistics on Indian States 2024–25*, Table 16: State-wise Health Infrastructure – Doctors and Specialists. The table reports 2023 staffing at Primary Health Centres (PHCs) in rural areas. Official source: https://www.rbi.org.in/Scripts/PublicationsView.aspx?id=23465

## Unit and coverage
One row per state/UT as represented in the RBI table (36 rows). Counts refer to doctors at rural PHCs, not all doctors in a state and not the entire health workforce.

## Fields
- `state_ut`: RBI state/UT label. Dadra & Nagar Haveli and Daman & Diu are combined.
- `required_rural_phc_doctors`: staffing requirement reported by the source.
- `sanctioned_rural_phc_doctors`: sanctioned positions.
- `in_position_rural_phc_doctors`: doctors reported in position.
- `vacant_reported`: reported vacancies where numeric.
- `shortfall_reported`: source-reported shortfall where numeric.
- `reference_year`: 2023.

## Missing-value handling
The RBI table uses an asterisk and dash in some cells. These are represented as blank/NA, not zero. A numeric zero remains zero. The source's shortfall field is not always numerically reported; do not reconstruct it from other columns. The Chandigarh row has no rural PHC doctor requirement and is excluded from coverage-ratio calculations.

## Derived indicator
The notebook calculates `in_position_rural_phc_doctors / required_rural_phc_doctors` where the requirement is positive. Values above 1 indicate in-position staffing above the reported requirement; this is not an error to cap or winsorise. It is a staffing-coverage ratio relative to the source's requirement, not doctors per capita or a measure of service quality.

## Limitation
The RBI table's PHC staffing figures are a point-in-time 2023 measure. Cross-sectional association with 2023 IMR is contemporaneous but remains observational. It cannot establish that staffing levels caused differences in infant mortality.
