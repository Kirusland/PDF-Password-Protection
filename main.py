from getpass4 import getpass
from PyPDF2 import PdfWriter, PdfReader
pdfwriter = PdfWriter()
pdf = PdfReader("name.pdf")
for page_num in range(pdf.numPages):
    pdfwriter.addPage(pdf.getPage(page_num))
passw = getpass.getpass(prompt = 'Введите пароль: ')
pdfwriter.encrypt(passw)
with open('ho.pdf', 'wb') as f:
    pdfwriter.write(f)