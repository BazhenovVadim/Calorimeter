import pandas as pd
from openpyxl import load_workbook

from data_base import session_factory, Products

# df = pd.read_excel(r"C:\Calorimeter\data_for_python.xlsx")
#
# wb2 = load_workbook(r"C:\Calorimeter\data_for_python.xlsx")
# print(wb2.sheetnames)
# ws = wb2['Лист1'].values

# with open("products.txt", "w", encoding="utf-8") as file:
#     for elem in ws:
#         name, f, p, c, calories = elem
#         file.write(f"{name}, {f}, {p}, {c}, {calories}\n")

with open("products.txt", "r", encoding="utf-8") as fil:
    session = session_factory()
    products = session.query(Products).all()
    new_prod = [str(x) for x in products]
    for line in fil:
        name = line.split(', ')[0]
        f = line.split(', ')[1]
        p = line.split(', ')[2]
        c = line.split(', ')[3]
        calories = line.split(', ')[4]
        product = Products(product_name=name, fats=f, proteins=p, carbs=c, calories=calories)
        if name not in new_prod:
            session.add(product)
            session.commit()
print(products)
