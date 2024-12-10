# PDF to CSV Extractor

This script allows you to extract text from all PDF files in a selected folder and save the extracted text into a CSV file. The CSV will contain information about each PDF file, including the file name, page number, and the text extracted from each page.

## Features:
- **Extract text**: Extracts the text from all pages of PDF files.
- **Batch processing**: Processes all PDF files in a selected folder.
- **CSV output**: Saves the extracted text into a CSV file with columns for the PDF file name, page number, and the text content.
- **Graphical Interface**: Provides an easy-to-use graphical interface for selecting the input folder and output CSV file.

## Requirements:
- Python 3.x
- `PyPDF2`: A library to read and extract text from PDF files.
- `pandas`: A library to handle data and export it to CSV.
- `tkinter`: A GUI library for creating a simple interface.

You can install the required libraries using the following command:
```bash
pip install PyPDF2 pandas
```

## How to Use:
1. **Run the script**: When you run the script, a window will appear prompting you to select a folder containing the PDF files you want to process.
2. **Select the folder**: After selecting the folder, you will be asked to choose where to save the resulting CSV file.
3. **Processing**: The script will extract text from each PDF in the selected folder and save it into the chosen CSV file.
4. **Completion**: Once the process is complete, a message will appear notifying you that the data has been saved successfully.

### CSV Output:
The CSV file will contain the following columns:
- **Archivo**: The name of the PDF file.
- **Página**: The page number in the PDF.
- **Contenido**: The text content extracted from that page.

## Example:
If the folder contains two PDF files:
- `file1.pdf` with 3 pages
- `file2.pdf` with 2 pages

The resulting CSV will look like this:

| Archivo     | Página | Contenido            |
|-------------|--------|----------------------|
| file1.pdf   | 1      | Text from page 1     |
| file1.pdf   | 2      | Text from page 2     |
| file1.pdf   | 3      | Text from page 3     |
| file2.pdf   | 1      | Text from page 1     |
| file2.pdf   | 2      | Text from page 2     |

## Troubleshooting:
- **Missing Libraries**: Ensure that `PyPDF2`, `pandas`, and `tkinter` are installed in your environment.
- **PDF Extraction Limitations**: Some PDFs may have non-text content (e.g., images or scanned pages) that cannot be extracted as text.

## License:
This script is provided under the MIT License.

---

This README should give a clear overview of how to use your script, what it does, and what users can expect.
