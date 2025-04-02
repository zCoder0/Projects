import pdfplumber

def extract_text_from_pdf(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            extracted_text = ""
            for page in pdf.pages:
                extracted_text += page.extract_text() + "\n"
        return extracted_text
    except Exception as e:
        print(f"Error reading the PDF: {e}")
        return None


# Specify the path to the PDF file
pdf_file_path = "your_pdf_path"  # Replace with your PDF file path


# Extract text and display it
extracted_data = extract_text_from_pdf(pdf_file_path)
if extracted_data:
    print("Extracted Text from PDF:")
    print(extracted_data)

