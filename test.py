from data_base import session_factory, Products


session = session_factory()

products = session.query(Products).all()
print(products)
product_new = Products(product_name='Пюре', proteins=2.5, fats=4.2, carbs=14.7, calories=106)
print(product_new.product_name)

if product_new.product_name not in products:
    session.add(product_new)
    session.commit()
session.close()




