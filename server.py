from itertools import product
from flask import Flask
from about import me
import json
from data import mock_data

app = Flask ("server")

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


@app.get("/api/products")
def get_products(): 
    return json.dumps(mock_data) 


@app.get("/api/products/<id>")
def get_product_by_id(id):
    for prod in mock_data:
        if str(prod["id"]) == id:
            return json.dumps(prod)

    return "not found in prod list"        


@app.get("/api/products_category/<category>")
def get_product_by_category(category):
    print("your category: ", category)
    result = []
    category = category.lower()
    for prod in mock_data:
        if prod["category"].lower() == category:
            result.append(prod)
    return json.dumps(result)


@app.get("/api/products_cheapest")
def get_products_cheapest():
    solution = mock_data[0]
    for prod in mock_data:
        if prod["price"] < solution["price"]:
            solution = prod
    return json.dumps(solution)



@app.get("/api/categories")
def get_categories():
    categories = []
    for prod in mock_data:
        cat = prod["category"]
        if not cat in categories:
            categories.append(cat)
        
    return json.dumps(categories)



app.run(debug=True)

