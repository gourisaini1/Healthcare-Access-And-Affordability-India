# Government hospital beds data dictionary

- Beds: total government hospital beds (rural + urban), sourced from National Health Profile 2023, Table 6.2.2.
- Beds reference date: 31 December 2022 as stated in the NHP table title.
- Population: projected total population as on 1 March 2021 from NHP 2023, Table 1.1.2(d), units in thousands.
- Combined UT: projected 2021 population for Dadra & Nagar Haveli and Daman & Diu is the sum of the two separate NHP population projections (608 + 469 = 1,077 thousand); hospital beds are reported for the merged UT.
- Rate: total government hospital beds / projected population × 1,000. Since population is stored in thousands, the rate is equivalently beds / population_thousands / 1,000? **No**: beds per 1,000 residents = beds / population_thousands / 1,000? The denominator population_thousands represents thousands of residents; beds / population_thousands gives beds per 1,000 residents directly.
- Population reference date is 1 March 2021, about 21 months before the bed-count reference date. The rate is therefore an approximate denominator-aligned availability indicator, not an exact same-date ratio.
- Government hospitals include central, state and local government bodies. This excludes private-sector beds.
- Source: Central Bureau of Health Intelligence, National Health Profile 2023, Table 6.2.2 (p.263) and Table 1.1.2(d) (pp.15–16).
  https://cbhidghs.mohfw.gov.in/sites/default/files/NHP/NHP-2023-Last-Final.pdf
