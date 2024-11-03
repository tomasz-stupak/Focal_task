# Focal Report Regression Testing

## Overview
This project automates regression testing for Focal reports in CSV and PDF formats to ensure consistency between production and staging data.

## Requirements
- python 3.x
- pandas
- pdfplumber
- pytest

## Install dependencies:
    pip install -r requirements.txt

## Run tests with pytest:
    pytest tests/

## Document data validation rules:
- Column Structure Consistency: Ensure both CSVs have identical columns.
- Row Count Consistency: Validate both reports have the same row count.
- Row-by-Row Consistency: Check if each row in staging matches production.
- PDF Text Consistency: Ensure the content of PDFs is identical.

## Future improvements:
- Expand tests for specific column types (e.g., dates, numerical ranges).
- Integrate tests into CI/CD for automated regression checks.
- Add deeper content verification within PDFs.
