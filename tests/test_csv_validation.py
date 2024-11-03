import pandas as pd
import pytest

# Helper function that is responsible for loading CSV data
def load_csv(filepath):
    try:
        data = pd.read_csv(filepath)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}. Please check the file path and try again.")
    except pd.errors.EmptyDataError:
        raise ValueError(f"File is empty: {filepath}. Ensure the file contains data.")
    except pd.errors.ParserError:
        raise ValueError(f"Parsing error: {filepath}. The file format may be incorrect or corrupted.")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred while loading {filepath}: {e}")

# These fixtures load production and staging data for each test
@pytest.fixture
def production_data():
    # Given a production data file is available
    return load_csv("resources/prod/gap_report_grocery_focal_superstore_101_2024-10-28_2024-10-28.csv")

@pytest.fixture
def staging_data():
    # Given a staging data file is available
    return load_csv("resources/staging/gap_report_grocery_focal_superstore_101_2024-10-28_2024-10-28.csv")

# Test: Check if column structure is consistent
def test_column_consistency(production_data, staging_data):
    # Given production and staging data are loaded successfully

    # When comparing the column structure of production and staging
    production_columns = set(production_data.columns)
    staging_columns = set(staging_data.columns)

    # Then the column structure should match
    mismatches = []
    missing_in_staging = production_columns - staging_columns
    extra_in_staging = staging_columns - production_columns

    if missing_in_staging:
        mismatches.append(f"Columns missing in staging: {', '.join(missing_in_staging)}")
    if extra_in_staging:
        mismatches.append(f"Extra columns in staging: {', '.join(extra_in_staging)}")

    # Assert that there are no mismatches
    assert not mismatches, "Column mismatch between production and staging reports:\n" + "\n".join(mismatches)

# Test: Check if row counts match
def test_row_count(production_data, staging_data):
    # Given production and staging data are loaded correctly

    # When comparing the row counts between production and staging
    production_row_count = len(production_data)
    staging_row_count = len(staging_data)

    # Then the row counts should be identical
    assert production_row_count == staging_row_count, \
        f"Row count mismatch: Production has {production_row_count} rows, staging has {staging_row_count} rows."

# Test: Check row-by-row if data is consistent
def test_data_consistency(production_data, staging_data):
    # Given production and staging data are loaded, and column structures match
    assert set(production_data.columns) == set(staging_data.columns), \
        "Column mismatch detected. Please check column consistency before running data consistency tests."

    # And the row counts are consistent
    assert len(production_data) == len(staging_data), \
        "Row count mismatch detected. Please ensure row counts are consistent before running data consistency tests."

    # When performing row-by-row and column-by-column comparison
    mismatches = []
    for row_idx, (prod_row, stag_row) in enumerate(zip(production_data.iterrows(), staging_data.iterrows())):
        prod_data = prod_row[1]  # Access the production row data
        stag_data = stag_row[1]  # Access the staging row data

        # Then each cell should be identical, treating NaN values as equal
        for col in production_data.columns:
            prod_value = prod_data[col]
            stag_value = stag_data[col]

            # Handle NaN values - treat them as equal if both are NaN
            if pd.isna(prod_value) and pd.isna(stag_value):
                continue  # Skip this comparison if both values are NaN

            # Compare non-NaN values
            if prod_value != stag_value:  # Check for inequality in specific columns
                mismatches.append(f"Data mismatch at row {row_idx + 1}, column '{col}': "
                                  f"Production = {prod_value}, Staging = {stag_value}")

    # Assert no mismatches were found
    if mismatches:
        error_message = "\n".join(mismatches)
        raise AssertionError(f"Inconsistent data found:\n{error_message}")