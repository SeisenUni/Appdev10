from flask import Flask,jsonify,request
from flask_cors import CORS
from pymongo.mongo_client import MongoClient
app = Flask(__name__)
uri = "mongodb+srv://chayathon14639:GVlE571RSj3LCD1p@cluster0.76js1dj.mongodb.net/"
client = MongoClient(uri)

db = client["Week+10Db"]
collection = db["product"]
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"



@app.route("/products",methods=["GET"])
def get_all_products():
    products = list(collection.find({}))
    product_list = []

    for product in products:
        product_data = {
            "id": str(product["id"]),
            "name": product.get("name", ""),
            "price": product.get("price", ""),
            "img": product.get("img", "")
        }
        product_list.append(product_data)
    
    return product_list




if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)