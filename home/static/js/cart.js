updateBtns = document.getElementsByClassName('update_item')
for (let i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function (e) {
        var productid = this.dataset.productid
        var action = this.dataset.action
        if (user == "AnonymousUser") {
            console.log("not logedin");
            addItemToCookie(e,productid, action)
        }
        else {
            updateItem(e, productid, action)
        }
    })

};


function addItemToCookie(e,productid, action) {
    console.log('not login');
    if (action == 'add') {
        if (cart[productid] == undefined) {
            cart[productid] = { 'quantity': 1 }
        } else {
            cart[productid]['quantity'] += 1;
        }

    }
    else if (action == 'remove') {

        cart[productid]['quantity'] -= 1;
        if (cart[productid]['quantity'] <= 0) {
            delete cart[productid]
        }
    }
    else if (action == 'AllRemove') {
        delete cart[productid]
    }

    console.log('cart : ', cart);
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    if (e.target.classList.contains("fa")) {
        location.reload()
    }

}


function updateItem(e, productid, action) {
    fetch("/order/UpdateItem/", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json; charset=utf-8',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            productid: productid,
            action: action
        })
    }).then((response) => {
        return response.json()

    }).then(() => {
        if (e.target.classList.contains("fa")) {
            location.reload()
        }
    })

}
//sepete ekle tuşları
addtocartBtns = document.getElementsByClassName('add_to_cart')
for (let cartBtn = 0; cartBtn < addtocartBtns.length; cartBtn++) {
    addtocartBtns[cartBtn].addEventListener('click', function (e) {
        var imgurl = this.dataset.imageurl
        var title = this.dataset.title
        var price = this.dataset.price
        viewerCreator(imgurl, title, price)
    })

}

function viewerCreator(imgurl, title, price) {
    var body = document.getElementsByTagName('body')[0]
    var viewer = document.createElement("div")
    viewer.style = ` z-index: 100;
        position: fixed;
        display: flex;
        top: 85%;
        left: 75%;
        width: 400px;
        height: 130px;
        background-color: mediumaquamarine;
        flex-direction: row;
        align-items: center;
        justify-content: space-evenly;`
    viewer.innerHTML = ` 
    <div>
        <img src= "` + imgurl + ` " style=" width: 75px;height:auto ;object-fit:cover;">
    </div>
    <div style="width: 66%; display:flex; flex-direction: column;">

        <h4 style="color: white; font-size: large; margin-top: 0px;">` + title + `</h4>
        <h5 style="color: white; font-size: large; margin-top: 0px;">` + price + `</h5>
        <div class="btns" style="display: flex;flex-direction: row;justify-content: space-evenly;">
            <button class="btn btn-danger">iptal et</button>
            <a href="/order/" class="btn btn-success">Sepeti Görüntüle</a>
        </div>
    </div>
    `
    body.appendChild(viewer)
    viewer.addEventListener('mouseleave', () => {
        setTimeout(() => {
            body.removeChild(viewer)
        }, 3000)
    })

}