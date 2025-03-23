from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws['A1'] = 'Hello, world!'

wb.save('output.xlsx')