# Raw data and source register

## API data (automated)
Notebook 01 downloads national health-financing observations from the World Bank Indicators API. The relevant series are sourced from WHO's Global Health Expenditure Database. Retrieval date and indicator codes are retained in metadata.

## Official state-level inputs (manual download)
- **NFHS-5 (2019–21) state/UT factsheets:** download the official compendium from https://www.nfhsiips.in/nfhsuser/index.php or https://www.nfhsiips.in/nfhsuser/publication.php. The OGD catalogue entry is https://www.data.gov.in/resource/all-india-and-stateut-wise-factsheets-national-family-health-survey-nfhs-5-2019-2021. Save a reviewed state-level workbook as `nfhs5_state_factsheets.xlsx`.
- **Rural Health Statistics 2021–22:** Ministry of Health and Family Welfare publication, https://www.mohfw.gov.in/sites/default/files/RHS%202021-22.pdf. Save the original as `rhs_2021_22.pdf`. Extract the relevant state/UT table into `rhs_state_infrastructure.csv` and retain original labels, units and page references.

Do not edit original source files. Do not infer missing values or combine incompatible years, geographies or definitions. Record the download date and page/table for every manually transcribed field.
