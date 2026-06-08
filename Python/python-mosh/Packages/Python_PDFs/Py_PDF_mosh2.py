import PyPDF2

merger = PyPDF2.PdfFileMerger()
file_names =["first.pdf", "second.pdf"]
for file_name in file_names:
    merger.append(file_name)

merger.write("combined.pdf")

