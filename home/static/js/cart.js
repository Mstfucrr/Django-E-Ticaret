updateBtns = document.getElementsByClassName('update_item')

for (let i = 0; i < updateBtns.length; i++) {
    
    console.log(updateBtns[i])
    updateBtns[i].addEventListener('click', function () {
        var productid = this.dataset.productid
        var action = this.dataset.action
        updateItem(productid, action)
    })
};

function updateItem(productid, action) {
    fetch("/order/UpdateItem/", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json; charset=utf-8',
            'X-CSRFToken':csrftoken,
        },
        body: JSON.stringify({
            productid: productid,
            action: action
        })
    }).then((response) => {
        return response.json()
        
    })
    .then((data) => {
        console.log('Data:',data);
        location.reload()
    })

}