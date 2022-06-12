updateBtns = document.getElementsByName('quantity')
updateBtns.forEach(updateBtn => {

    updateBtn.addEventListener('change', function (e) {
        var quantit = this.dataset.quan
        var productid = this.dataset.productid
        console.log(e);
        var action = ""
        if ( quantit < updateBtn.value ) 
            action = 'add'
        else 
            action = 'remove'
        console.log(action + this.dataset.productid + " " + quantit);
        // updateItem(productid, action)
    })
});





function updateItem(productid,action) {

    fetch("/UpdateItem/", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json; charset=utf-8',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            productid : productid,
            action : action
        })
    })

}


