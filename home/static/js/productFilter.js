// noUiSlider
var skipSlider = document.getElementById('skipstep');
var skipValues = [
    document.getElementById('skip-value-lower'),
    document.getElementById('skip-value-upper')
];
// number olarak alıyoruz
minPrice = parseFloat(skipValues[0].innerHTML);
maxPrice = parseFloat(skipValues[1].innerHTML);

noUiSlider.create(skipSlider, {
    start: [minPrice, maxPrice],
    connect: false,
    step: 1,
    range: {
        'min': minPrice,
        'max': maxPrice

    },

});

var skipValues = [
    document.getElementById('skip-value-lower'),
    document.getElementById('skip-value-upper')
];

skipSlider.noUiSlider.on('update', function (values, handle) {
    skipValues[handle].innerHTML = values[handle];
});

displayedProductsIds = [];
$(".product").each(function () {
    displayedProductsIds.push($(this).attr("id"));
});

$(".aa-filter-btn").click(function(e){
    e.preventDefault();
    var min = $("#skip-value-lower").text();
    var max = $("#skip-value-upper").text();

    console.log(displayedProductsIds + " " + min + " " + max)
    // def filter_product(request,minPrice,maxPrice): için fetch requesti atar
    url = "/filter_product/" + "displayedProductsIds=" + displayedProductsIds + "&minPrice=" + min + "&maxPrice=" + max + "/";
    console.log(url)
    $.ajax({
        type: "GET",
        // filter_product/minPrice=<str:minPrice>&maxPrice=<str:maxPrice>/
        url: url,
        success: function (response) {
            $(".aa-product-catg-body").empty();
            $(".aa-product-catg-body").append(response);
        }
    });

});
