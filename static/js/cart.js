function addToCart(id,type_=null){
    const url = "http://127.0.0.1:8000/shop/add-to-cart/"+id;
    fetch(url);
    if(type_ == 'reload'){
        window.location.reload();
        return;
    }
    alert("Item Added Successfully");
}

function removeFromCart(id,type_=null){
    const url = "http://127.0.0.1:8000/shop/remove-from-cart/"+id;
    fetch(url);
    if(type_ == 'reload'){
        window.location.reload();
        return;
    }
    alert("Item Removed Successfully");
}