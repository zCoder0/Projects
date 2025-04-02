# PDF Summarization using FLAN-T5

## 📌 Project Overview
This project implements a PDF summarization system using Google's `flan-t5-large` model. It extracts text from PDF documents and generates concise summaries using Natural Language Processing (NLP).

## 🚀 Features
- Extracts text from PDF files using `pdfplumber`.
- Summarizes extracted text using `flan-t5-large`.
- Handles large documents efficiently.

## 🛠 Tech Stack
- **Programming Language:** Python
- **Libraries:**
  - `pdfplumber` (for text extraction from PDFs)
  - `transformers` (for NLP processing)
  - `torch` (for deep learning model execution)

## 📂 Project Structure
```
📦 PDF-Summarization
│-- main.py                     # Main script for execution
│-- requirements.txt             # Dependencies
│-- README.md                    # Project documentation
│-- data/                        # Folder containing PDFs
│   │-- sample.pdf                # Sample input file
│-- models/                      # Model storage
│   │-- flan-t5-large             # Pretrained model
```

## 🔧 Installation & Setup
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/your-username/pdf-summarization.git
   cd pdf-summarization
   ```
2. **Create a Virtual Environment (Optional but Recommended):**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## 📜 Usage
1. **Run the Summarization Script:**
   ```sh
   python main.py 
   # Specify the path to the PDF file
   pdf_file_path = "your_pdf_path"  # Replace with your PDF file path

   ```
2. **Example Output:**
   ```
   Extracted Text: "This is a sample document..."
   Generated Summary: "Summary of the document..."
   ```

## 📝 Future Enhancements
- Implement a web-based UI with `Streamlit`.
- Support multiple summarization models.
- Improve summarization accuracy with fine-tuning.

## 👨‍💻 Author
**Prem Raj** – [GitHub](https://github.com/zCoder0) | [LinkedIn](https://www.linkedin.com/in/prem-raj-sivakumar-998aa628a/)

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

