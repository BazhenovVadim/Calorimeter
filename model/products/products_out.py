from model.products import ProductIn


class ProductOut(ProductIn):
    product_id: int

    class Config:
        orm_mode: True
