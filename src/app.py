from flask import Flask, jsonify, request
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
            "id" : str(product["_id"]),
            "name" : product["name"],
            "price" : product["price"],
            "img": product["img"]
        }
        product_list.append(product_data)
    return jsonify({"products": product_list})

@app.route("/products", methods=["POST"])
def add_product():
    data = request.get_json()
    
    existing_product = collection.find_one({"_id": data.get("_id")})
    if existing_product:
        return jsonify({"error": "Cannot add product"}),500
    
    new_product = {
        "_id" : data.get("_id"),
        "name" : data.get("name"),
        "price" : data.get("price"),
        "img" : data.get("img")
    }
    result = collection.insert_one(new_product)
    return jsonify({"product": new_product}), 200


@app.route("/products/<string:product_id>", methods=["DELETE"])
def delete_product(product_id):
    deleted_product = collection.find_one_and_delete({"_id": product_id})

    if deleted_product:
        deleted_product_data = {
            "_id": str(deleted_product["_id"]),
            "name": deleted_product.get("name", ""),
            "price": deleted_product.get("price", ""),
            "img": deleted_product.get("img", "")
        }
        return jsonify({"message": "Product deleted successfully", "deleted_product": deleted_product_data}), 200
    else:
        return jsonify({"error": "Product not found"}), 404
@app.route("/products/<string:prod_id>", methods=["PUT"])
def update_product(prod_id):
    data = request.get_json()

    existing_product = collection.find_one({"_id": prod_id})

    if existing_product:
        updated_product = {
            "$set": {
                "name": data.get("name", existing_product["name"]),
                "price": data.get("price", existing_product["price"]),
                "img": data.get("img", existing_product["img"])
            }
        }

        result = collection.find_one_and_update({"_id": prod_id}, updated_product, return_document=True)

        return jsonify({"product": result}), 200
    else:
        return jsonify({"error": "Product not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)