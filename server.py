from random import randrange
from flask import Flask, request
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



@app.post("/api/products")
def save_products():
    product = request.get_json()  
    
    mock_data.append(product)
    product["id"] = randrange(1, 1000000000)

    return json.dumps(product) 


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




@app.get("/api/count_products")
def get_product_count():
    count = len(mock_data)

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