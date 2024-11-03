import pdfplumber
import pytest

# Helper function that is responsible for extracting text from each page of a PDF
def extract_text_from_pdf(filepath):
    try:
        with pdfplumber.open(filepath) as pdf:
            text = ""
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
            return text
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}. Please check the file path and try again.")
    except pdfplumber.pdf.PDFSyntaxError:
        raise ValueError(f"File could not be read: {filepath}. Ensure the file is a valid PDF format.")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred while processing the PDF file '{filepath}': {e}")

# These fixtures load production and staging data for each test
@pytest.fixture
def production_text():
    # Given a production PDF file is available
    return extract_text_from_pdf("resources/prod/gap_report_grocery_focal_superstore_101_2024-10-28_2024-10-28.pdf")

@pytest.fixture
def staging_text():
    # Given a staging PDF file is available
    return extract_text_from_pdf("resources/staging/gap_report_grocery_focal_superstore_101_2024-10-28_2024-10-28.pdf")

# Test: Check if Staging PDF and Production PDF match
def test_pdf_text_consistency(production_text, staging_text):
    # Given production and staging PDFs are loaded

    # When comparing the full text content of both PDFs
    # Then the text content should be identical
    assert production_text == staging_text, "PDF text content differs between production and staging."