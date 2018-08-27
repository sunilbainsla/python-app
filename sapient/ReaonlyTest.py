from openpyxl import load_workbook
wb = load_workbook(filename='D:/MIP/Manpower_plan_2017_2019.xlsm', read_only=True)
ws = wb['Q3F Demand']

for row in ws.rows:
    print(row)