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
            })
        }).then(() => {
            setTimeout(() => {
                window.location.reload()
            }, 1500)

        })
    })
}


// get just list_group_items in id = logged-in-myAccount <section></section>
var list_group_items = document.querySelectorAll("#logged-in-myAccount .list-group-item");

list_group_items.forEach(function(item) {
    item.addEventListener("click", function() {
        var active = document.querySelector("#logged-in-myAccount .list-group-item.active");
        active.classList.remove("active");
        item.classList.add("active");
        // for loggedin Users Account , Order infos id show in this section
        showDiv = item.dataset.show;
        // seçileni göster
        document.getElementById(showDiv).style.display = "block";     
        // diğerlerini gizle item haric diğerlerini gizle
        var others = document.querySelectorAll("#logged-in-myAccount .list-group-item:not(.active)");
        others.forEach(function(other) {
            hideDiv = other.dataset.show;
            document.getElementById(hideDiv).style.display = "none";
        })
        
    })
})
