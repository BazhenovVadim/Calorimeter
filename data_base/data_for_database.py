import pandas as pd
from openpyxl import load_workbook

from data_base import session_factory, Products

df = pd.read_excel(r"C:\Users\vadim\OneDrive\Документы\data_for_python.xlsx")

wb2 = load_workbook(r"C:\Users\vadim\OneDrive\Документы\data_for_python.xlsx")
print(wb2.sheetnames)
ws = wb2['Лист1'].values


def update_table_products(ws):
    for line in ws:

        session = session_factory()
        name, f, p, c, calories = tuple(line)
        product = Products(product_name=name, proteins=p, fats=f, carbs=c, calories=calories)

        session.add(product)
        session.commit()
        session.close()


# update_table_products(ws)

