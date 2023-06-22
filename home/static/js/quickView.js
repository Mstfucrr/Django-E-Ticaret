

function QuickView(e) {

    productid = e.dataset.productid;
    $.ajax({
        url: "/product/Get_product_detail/",
        type: "POST",
        headers: {
            "X-CSRFToken": csrftoken
        },
        data: {
            "product_id": productid
        },

        success: function (response) {
            console.log(response);
            document.querySelector("#quick-view-modal .aa-product-view-content h3").innerHTML = response.name;
            // main img
            document.querySelector("#quick-view-modal .aa-product-view-slider .simpleLens-big-image").src = response.image;
            // sub imgages list
            images = response.images;
            /*
            <a href="#" class="simpleLens-thumbnail-wrapper"
                                                            data-lens-image="{% static 'img/view-slider/large/polo-shirt-1.png' %}"
                                                            data-big-image="{% static 'img/view-slider/medium/polo-shirt-1.png' %}">
                                                            <img
                                                                src="{% static 'img/view-slider/thumbnail/polo-shirt-1.png' %}">
                                                        </a>
            */
            document.querySelector("#quick-view-modal .aa-product-view-slider .simpleLens-thumbnails-container").innerHTML = "";
            images.forEach(function (image) {
                document.querySelector("#quick-view-modal .aa-product-view-slider .simpleLens-thumbnails-container").innerHTML += `
                        <a href="#" class="simpleLens-thumbnail-wrapper"
                                                                    data-lens-image="${image}"
                                                                    data-big-image="${image}">
                                                                    <img src="${image}" style="width: 50px; height: 50px; object-fit: contain;">
                                                                </a>
                        `;
            });

            document.querySelector("#quick-view-modal .aa-product-view-content .aa-product-view-price").innerHTML = response.price + " TL";
            document.querySelector("#quick-view-modal .aa-product-view-content p.description").innerHTML = response.description;
            document.querySelector("#quick-view-modal .aa-product-view-content .aa-prod-category a").innerHTML = response.category;
            document.querySelector("#quick-view-modal .aa-product-view-content .aa-prod-category a").href = "/category/" + response.category_id + "/" + response.category;
            // view details button
            document.querySelector("#quick-view-modal .aa-product-view-content .aa-add-to-cart-btn.viewDeatils").href = "/product/" + response.id + "/" + response.slug;
            // add to cart button
            document.querySelector("#quick-view-modal .aa-product-view-content .aa-add-to-cart-btn").dataset.imageurl = response.image;
            document.querySelector("#quick-view-modal .aa-product-view-content .aa-add-to-cart-btn").dataset.title = response.name;
            document.querySelector("#quick-view-modal .aa-product-view-content .aa-add-to-cart-btn").dataset.price = response.price;
            document.querySelector("#quick-view-modal .aa-product-view-content .aa-add-to-cart-btn").dataset.productid = response.id;



        }
    });

}

