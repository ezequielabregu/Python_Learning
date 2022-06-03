from openpyxl import Workbook, load_workbook

wb = Workbook()             # crea el WB
ws = wb.active              # activa el WB
ws.title = "Data"           # titulo del WB


ws.append(['Eze', 'es', 'Great', '!']) # escribo en toda la 1ra fila
ws.append(['Gise', 'es', 'Great', '!']) # escribo en toda la 2da fila
ws.append(['Lucy', 'es', 'Great', '!']) # escribo en toda la 1ra fila
ws.append(['Callao', 'es', 'Great', '!']) # escribo en toda la 2da fila


wb.save('ezequiel.xlsx')                # guardo el WB