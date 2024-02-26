import React, { useState, useEffect } from "react";
import axios from "axios";

export default function Product() {
    const [products, setProducts] = useState([]);
    const [formData, setFormData] = useState({
        _id: "",
        name: "",
        price: "",
        img: ""
    });

    useEffect(() => {
        axios.get('http://localhost:5000/products')
            .then(response => setProducts(response.data.products))
            .catch(error => console.error('Error fetching products:', error));
    }, []);

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post('http://localhost:5000/products', formData)
            .then(response => {
                setProducts([...products, response.data.product]);
                setFormData({
                    _id: "",
                    name: "",
                    price: "",
                    img: ""
                });
            })
            .catch(error => console.error('Error adding product:', error));
    };

    return (
        <div>
            <h2>Add Product</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>ID:</label>
                    <input type="text" name="id" value={formData.id} onChange={handleChange} />
                </div>
                <div>
                    <label>Name:</label>
                    <input type="text" name="name" value={formData.name} onChange={handleChange} />
                </div>
                <div>
                    <label>Price:</label>
                    <input type="text" name="price" value={formData.price} onChange={handleChange} />
                </div>
                <div>
                    <label>Image URL:</label>
                    <input type="text" name="img" value={formData.img} onChange={handleChange} />
                </div>
                <button type="submit">Add Product</button>
            </form>
            <ul>
            <h1>All Product</h1>
                {products.map(product => (
                    <li key={product._id}>
                        <img src={product.img} alt={product.name} />
                        <div>{product.name}</div>
                        <div>Price: {product.price}</div>
                    </li>
                ))}
            </ul>
            
        </div>
    );
}
