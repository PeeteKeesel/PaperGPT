
from PyPDF2 import PdfReader


# Read the file if it's a PDF.
reader = PdfReader("tests/attention_is_all_you_need.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

