from data_base import session_factory, Products


session = session_factory()


product = session.query(Products).where(Products.product_name == 'Пюре').first()
print(product.calories)




