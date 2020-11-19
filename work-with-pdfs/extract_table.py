from tabula import read_pdf 
table = read_pdf('sample-document.pdf', pages='all')
print(table)
