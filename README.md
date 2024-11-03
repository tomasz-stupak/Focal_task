# Focal Report Regression Testing

## Overview
This project automates regression testing for Focal reports in CSV and PDF formats to ensure consistency between production and staging data.

The project focuses on comparing files from the Staging environment with files from the Production environment, which serve as the reference standard. The test could be enhanced by adding more detailed validation checks for each column (e.g. data formatting, value ranges, field dependencies) which could be beneficial for cases with no reference files available.

## Requirements
- python 3.x
- pip

Included in requirements.txt:
- pandas 
- pdfplumber
- pytest

## Install dependencies:
    pip install -r requirements.txt

## Run tests with pytest:
    pytest tests

## Document data validation rules:
- Column Structure Consistency: Ensure both CSVs have identical columns.
- Row Count Consistency: Validate both reports have the same row count.
- Row-by-Row Consistency: Check if each row in staging matches production.
- PDF Text Consistency: Ensure the content of PDFs is identical.

## Future improvements:
- Enhance validation rules so it covers a broader range of checks (e.g. data formatting, value ranges, field dependencies).
- Parametrization which allows the tests to run on different datasets by using env variables or config files.
- Integrate tests into CI/CD for automated regression checks.
- Add logging and more detailed reporting for better visibility.
- Add deeper content verification within PDFs and extend the comparison to include visual differences to ensure minor formatting changes or layout issues are also detected.
- Implement historical analysis to track regression trends.
- Create a dashboard for real-time monitoring.
