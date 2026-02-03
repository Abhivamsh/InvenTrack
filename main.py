
from fastapi import Depends,FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Product
from database import Session, engine
import database_models


app= FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allows all origins
    # allow_credentials=True,
     allow_methods=["*"],  # Allows all methods
    # allow_headers=["*"],  # Allows all headers
)

database_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "Hello, World!,fastapi"
 
products = [
    #  Product(1,"Phone",789,"Smartphone with 6GB RAM",5),
    #     Product(2,"Laptop",1299,"Powerful laptop with 16GB RAM",3),     
    #     Product(3,"Headphones",199,"Wireless headphones with noise cancellation",10)
    Product(id=1,name="Phone",price=789,description="Smartphone with 6GB RAM",quantity=5),
    Product(id=2,name="Laptop",price=1299,description="Powerful laptop with 16GB RAM",quantity=3),     
    Product(id=3,name="Headphones",price=199,description="Wireless headphones with noise cancellation",quantity=10)
 ]
 
 
def get_db():
    db = Session()
    try:
        yield db #waiting for the db operation to complete
    finally:
        db.close()
            
        
        
def init_db():
     db = Session()
     
     count = db.query(database_models.Product).count()
     if count ==0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))            
        db.commit()
        
init_db()




@app.get("/products")
def get_all_products (db:Session = Depends(get_db)):
    # db=session()
    # db.query()
    db_products = db.query(database_models.Product).all()
    return db_products

@app.get("/products/{id}")
def  get_product_by_id(id:int, db: Session= Depends(get_db)):
      db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
      if db_product:
          return db_product
      return   "not found the product"

@app.post("/products")
def add_product(product:Product,db: Session= Depends(get_db)):
    db_product = database_models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    # products.append(product)
    return product


@app.put("/products/{id}")
def update_product(id:int,product:Product,db:Session=Depends(get_db)):
    # for index in range(len(products)):
    #     if products[index].id ==id:
    #         products[index]=product
    #         return product
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:      
        db_product.name = product.name
        db_product.price = product.price
        db_product.description = product.description
        db_product.quantity = product.quantity
        db.commit()
        return product  
    else:
         return "not found the product"


@app.delete("/products/{id}")
def delete_product(id:int,db:Session=Depends(get_db)):
    # for index in range(len(products)):
    #     if products[index].id == id:
    #         products.pop(index)  #del products[index] rreplce of pop method
    #         return "product deleted successfully"
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:  
        db.delete(db_product)
        db.commit()
        return "product deleted successfully"
        
    return "not found the product"

   