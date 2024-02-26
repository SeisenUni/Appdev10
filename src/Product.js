import { useState, useEffect } from "react";
import axios from "axios";
// const Item = props =>
// { 
//     return (<div onClic k={e => props.callback(props.id)}>
//         <img src={props.img} width={200} height={200} /><br/>
//         id : {props.id}<br/>
//         Name : {props.name}<br />
//         Price : {props.price}<br/>    
//     </div>);
// }
export default function Product()
{
    const [product,setProduct]=useState([])
    useEffect(()=>{
        console.log("request to api")
        axios.get("http://127.0.0.1:5000/products")
        .then(response=>setProduct(response.data))
        .catch(error => {
            console.error('Error fetching datas:', error);
          })
    },[])
    const productList=product.map(p=><li key={p.id}>{p.id} 
    {p.name} <img src={p.img}/> {p.price}</li>)
    return (<>
        <ul>
            {productList}
        </ul>
    </>)
}