import tabula

__filePath = "G274756.pdf"
__outputCsvPath = "OutputCsv.csv"
__outputJsonPath = "tabulaAppTemplate.json"
__tabulaAppTemplatePath = "tabulaAppTemplate.json"
# Read pdf into a list of DataFrame in form of pandas
__area = [169.8, 11.21, 649.16, 573.46]
__columns = [45, 159, 312, 363, 393.09, 446.2, 506]
dfs = tabula.read_pdf(__filePath, stream=True, lattice=False, area=__area, columns=__columns, pages=1, multiple_tables=False, guess=False)
#__buildOptions = tabula.io.build_options(stream=True, pages='all')
#dfs = tabula.read_pdf_with_template(__filePath, __tabulaAppTemplatePath, __buildOptions)
#dfsJson = tabula.convert_into(__filePath, __outputJsonPath, output_format='json', pages='all')
#dfsCsv = tabula.convert_into(__filePath, __outputCsvPath, output_format='csv', pages='all')
#print(type(dfs))
#print(len(dfs))
#print(type(dfs[0]))
print(dfs)
print(dfs[0].shape)
print(dfs[0].columns)
print(dfs[0].index)
print(dfs[0].iloc[4, [1, 2, 3]])