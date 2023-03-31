# PDF Merger

This is a Python program that merges multiple PDF files into a single PDF file using the PyPDF2 library. The program prompts the user to specify the names of the PDF files to be merged, creates a PdfMerger object using the PyPDF2 library, appends each PDF file to the PdfMerger object, and then saves the merged PDF file to the specified destination path.

## How to Use
1. Clone or download the repository to your local machine.

2. Install the required dependencies using pip package manager. You can install PyPDF2 by running the following command:

```
pip install pypdf2


```

3. Navigate to the pdf_merger folder in your terminal.

4. Edit the pdfiles variable in the pdf_merger.py file to specify the names of the PDF files to be merged.

5. Edit the output path and filename.

6. Run the pdf_merger.py file by entering the following command in your terminal:

``` 
python pdf_merger.py


```

7. The program will merge the specified PDF files into a single PDF file and save the resulting PDF to the specified destination path.

