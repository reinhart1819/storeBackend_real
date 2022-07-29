# from random import randrange

from flask import Flask, request
from about import me
import json
from data import mock_data
from config import db
from bson import ObjectId
from flask_cors import CORS

app = Flask ("server")
CORS(app)

@app.get("/")
def home():
    return "Hello World!"

@app.get("/test")
def test():
    return "This is a test"

@app.get("/about")
def about_me():
    return "I'm Chris"


###########################################################
################ API ENDPOINTS = PRODUCTS #################
###########################################################  

@app.get("/api/versions")
def version():
    return "1.0"

@app.get("/api/users")
def users():
    return "A list of users"

@app.get("/api/about")
def about_json():
    # return me["first"] + " " + me["last"]
    return json.dumps(me)  

def fix_mongo_id(obj):
    obj["id"] = str(obj["_id"])
    del obj["_id"]
    return obj    


@app.get("/api/products")
def get_products(): 
    cursor = db.products.find({})
    result = []
    for prod in cursor:
        fix_mongo_id(prod)
        result.append(prod)

    return json.dumps(result) 



@app.post("/api/products")
def save_products():
    product = request.get_json() 
 
    db.products.insert_one(product) 
    fix_mongo_id(product)

    return json.dumps(product) 


@app.get("/api/products/<id>")
def get_product_by_id(id):
    prod = db.products.find_one({"_id": ObjectId(id)})
    if not prod:
        return "not found"

    fix_mongo_id(prod)
    return json.dumps(prod)    
           


@app.get("/api/products_category/<category>")
def get_product_by_category(category):
    cursor = db.products.find({"category": category})
    results = []
    for prod in cursor:
        fix_mongo_id(prod)
        results.append(prod)
    return json.dumps(results)


@app.get("/api/products_cheapest")
def get_products_cheapest():
    cursor = db.products.find({})
    solution = cursor[0]
    for prod in cursor:
        if prod["price"] < solution["price"]:
            solution = prod
    fix_mongo_id(solution)        
    return json.dumps(solution)



@app.get("/api/categories")
def get_categories():
    categories = []
    cursor = db.categories.find({}) 
    for prod in cursor:
        cat = prod["category"]
        if not cat in categories:
            categories.append(cat)
        
    return json.dumps(categories)




@app.get("/api/count_products")
def get_product_count():
    cursor = db.categories.find({})
    count = 0
    for prod in cursor:
        count += 1


    return json.dumps({"count": count})






@app.get("/api/search/<text>")
def get_title_text(text):
    result = []
    text = text.lower()
    for product in mock_data:
        if text in product["title"].lower():
            result.append(product)


    return json.dumps(result)



app.run(debug=True)    