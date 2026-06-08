import PyPDF2

with open("/Users/jack/Desktop/Learning_Python.pdf", "rb") as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    page = reader.getPage(0)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open("Output.pdf", "wb") as output:
        writer.write(output)
    # writer.insertPage(page)
    # writer.insertBlankPage()




