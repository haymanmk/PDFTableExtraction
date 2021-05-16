import tabula

__filePath = "G274756.pdf"
__outputCsvPath = "OutputCsv.csv"
# Read pdf into a list of DataFrame in form of pandas
dfs = tabula.read_pdf(__filePath, stream=True, pages='all')
dfsCsv = tabula.convert_into(__filePath, __outputCsvPath, output_format='csv', pages='all')
print(type(dfs))
print(len(dfs))
print(type(dfs[0]))