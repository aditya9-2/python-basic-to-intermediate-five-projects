import PyPDF2

pdfiles = ["1.pdf", "2.pdf"]

merger = PyPDF2.PdfMerger()

for filename in pdfiles:
    pdFile = open(filename, "rb")
    pdReader = PyPDF2.PdfReader(pdFile)
    merger.append(pdReader)
    pdFile.close()

pdFile.close()
merger.write("NewPDF.pdf")

#          or
# with open("merged.pdf", "wb") as output:
#     merger.write(output)
