from openpyxl import Workbook, load_workbook

wb = load_workbook('Grades.xlsx')   # genero el workbook
ws = wb.active                      # activo el worksheet

print(ws)