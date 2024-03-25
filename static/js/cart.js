function addToCart(id,type_=null){
    const url = "http://127.0.0.1:8000/shop/add-to-cart/"+id;
    fetch(url)
    .then(response => response.json()) // Parse the JSON response
    .then(data => {
        // Extract the values from the JSON data
        const total_price = data.total_price;
        const item_qnty = data.item_qnty;
        const item_total = data.item_total;

        var qnty_id = "itm_qnty_"+id;
        var qnty_tot = "itm_tot_"+id;
        
        // Use the extracted values as needed
        document.getElementById('tot').textContent  = total_price;
        document.getElementById(qnty_id).textContent  = item_qnty;
        document.getElementById(qnty_tot).textContent  = item_total;
        
        
    })
    .catch(error => {
        console.error('Error:', error);
        // Handle any errors that occurred during the fetch
    });
    alert("Item Added Successfully");
}


function removeFromCart(id, type_=null) {
    const url = "http://127.0.0.1:8000/shop/remove-from-cart/" + id;
    
    fetch(url)
    .then(response => response.json()) // Parse the JSON response
    .then(data => {
        // Extract the values from the JSON data
        const total_price = data.total_price;
        const item_qnty = data.item_qnty;
        const item_total = data.item_total;

        var qnty_id = "itm_qnty_"+id;
        var qnty_tot = "itm_tot_"+id;
        
        // Use the extracted values as needed
        document.getElementById('tot').textContent  = total_price;
        document.getElementById(qnty_id).textContent  = item_qnty;
        document.getElementById(qnty_tot).textContent  = item_total;

        if(total_price === 0){
            window.location.href='/shop/cart';
        }
        
       
    })
    .catch(error => {
        console.error('Error:', error);
        // Handle any errors that occurred during the fetch
    });
    alert("Item Removed Successfully");
}
