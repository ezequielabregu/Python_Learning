from openpyxl import Workbook, load_workbook

wb = load_workbook('Grades.xlsx')   # genero el workbook

wb.create_sheet("test")

print(wb.sheetnames)                # da el nombre de las sheets del documento