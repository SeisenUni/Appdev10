import { useState, useEffect } from "react";
import axios from "axios";

export default function Product() {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:5000/products')
            .then(response => setProducts(response.data.products))
            .catch(error => console.error('Error fetching products:', error));
    }, []);

    return (
        <div>
            <h1>Products </h1>
            <ul>
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
