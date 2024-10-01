import PyPDF2

pdf_files = input("Enter the names of the PDF files you want to merge (Use ',' to seperate the names): ").split(', ')

pdf_files = [file.strip() for file in pdf_files]

merger = PyPDF2.PdfMerger()

for filename in pdf_files:
    with open(filename, "rb") as pdf:
        reader = PyPDF2.PdfReader(pdf)
        merger.append(reader)

with open("merged.pdf", "wb") as merged_pdf:
    merger.write(merged_pdf)

print("PDFs merged successfully into 'merged.pdf'")

# You must have to upload the pdf files in the interpreters. Such as in this code I uploaded "1.pdf" and "2.pdf" in the interpreter.
