wishListBtn = document.querySelectorAll(".wishListBtn");

wishListBtn.forEach((btn) => {
    btn.addEventListener("click", (e) => {
        let productid = btn.dataset.productid;
        let action = btn.dataset.action;
        if (user == "AnonymousUser") {
            console.error("not logedin");
        }
        else {
            wishListUpdateItem(e, productid, action)
        }
    })
})


function wishListUpdateItem(e, productid, action) {
    fetch("/order/wishListUpdateItem/", {
        "method": "POST",
        "headers": {
            "Content-Type": "application/json; charset=utf-8",
            "X-CSRFToken": csrftoken,
        },
        "body": JSON.stringify({
            productid: productid,
            action: action
        })
    }).then((response) => {
        return response.json()
    }
    ).then((data) => {
        console.log(data);
        location.reload()
    })
}