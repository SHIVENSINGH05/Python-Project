from PyPDF2 import PdfMerger  # Fix: Use PdfMerger for merging PDFs

merger = PdfMerger()

pdfs = []
n = int(input("How many pdfs do u want to merge?\n"))

for i in range(0, n):
    name = input(f"Enter the name of first pdf {i + 1}: ")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merger-pdf.pdf")
merger.close()