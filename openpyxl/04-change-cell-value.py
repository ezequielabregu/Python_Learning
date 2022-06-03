from openpyxl import Workbook, load_workbook

wb = load_workbook('Grades.xlsx')   # genero el workbook
ws = wb.active                      # activo el worksheet
ws['A2'].value = "Ezequiel"         # --> cambio el valor de la cell

wb.save('Grades.fix.xlsx')          # guardo file con otro nombre