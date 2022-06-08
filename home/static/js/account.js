Form = document.getElementsByClassName("form-inline");
for (var i = 0; i < Form.length; i++) {
    Form[i].addEventListener('submit', function(e) {
        e.preventDefault();
        var action = this.dataset.action;
        var id = this.dataset.customer;
        var updateData = {};
        if (action === 'info') {
            updateData = {
                'name': document.getElementById("name").value,
                'lastname': document.getElementById("lastname").value,
            };
        } else if (action === 'contact') {
            updateData = {
                'email': document.getElementById("email").value,
                'phone': document.getElementById("phone").value,
            };
        } else if (action === 'address') {
            updateData = {
                'address': document.getElementById("address").value,
                'country': document.getElementById("country").value,
                'city': document.getElementById("city").value,
            };
        }

        fetch("UserUpdate/", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json; charset=utf-8',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({
                'customer': id,
                'action': action,
                'infoUpdate': updateData
            }).then((response) => {
                window.location.reload();
            })

        })
    })
}