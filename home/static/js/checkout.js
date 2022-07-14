newaddressradio = document.getElementsByName("selectAddress")
isMyAddress = true;
newaddressradio[0].addEventListener('change', (e) => {

    document.getElementById("newAddress").classList.remove("in")
    isMyAddress = true;
})
newaddressradio[1].addEventListener('change', (e) => {
    isMyAddress = false;
})



checkoutForm = document.getElementById("checkoutForm")
checkoutForm.addEventListener('submit', (e) => {
    e.preventDefault();

    fetch('/order/checkout/', {
        method: "POST",
        headers: {
            'Content-Type': 'application/json; charset=utf-8',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'isMyAddress' : isMyAddress,
        })
    }).then(() => {
        console.log("Sipariş Alındı")
        setTimeout(()=>{
            window.location.reload()
        },1500)
    })
})