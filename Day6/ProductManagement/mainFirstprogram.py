from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Product Class
class Product(BaseModel):
    id: int
    name: str
    category: str
    price: float
    quantity: int


# Store Products in LIST
products = []

# API 1: Home
@app.get("/")
def home():
    return {"message": "Welcome to Product Management"}

# API 2: Add Product
@app.post("/addProduct")
def addProduct(product: Product):
    products.append(product)
    return {"message": "Product Added Successfully"}





# API 3: Get All Products
@app.get("/getAllProducts")
def getAllProducts():
    return products



# 15 minuts break  























# API 4: Get Product By ID
@app.get("/productByID/{id}")
def getProductByID(id: int):
    for p in products:
        if p.id == id:
            return p
    return {"message": "Product Not Found"}





















# API 5: Get Product By Name
@app.get("/productByName/{name}")
def getProductByName(name: str):
    for p in products:
        if p.name == name:
            return p
    return {"message": "Product Not Found"}

















# API 6: Get Products By Category
@app.get("/productByCategory/{category}")
def getProductByCategory(category: str):
    result = []
    for p in products:
        if p.category == category:
            result.append(p)
    return result



















# API 7: Update Product
@app.put("/updateProduct/{id}")
def updateProduct(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return {"message": "Product Updated Successfully"}
    return {"message": "Product Not Found"}


# API 8: Update Product Price
@app.patch("/updatePrice/{id}")
def updatePrice(id: int, price: float):
    for p in products:
        if p.id == id:
            p.price = price
            return {"message": "Price Updated Successfully"}
    return {"message": "Product Not Found"}


# API 9: Delete Product
@app.delete("/deleteProduct/{id}")
def deleteProduct(id: int):
    for p in products:
        if p.id == id:
            products.remove(p)
            return {"message": "Product Deleted Successfully"}
    return {"message": "Product Not Found"}


# API 10: Delete All Products
@app.delete("/deleteAllProducts")
def deleteAllProducts():
    products.clear()
    return {"message": "All Products Deleted Successfully"}
