$(document).ready(function () {
    var form= $('#form_basket_created');

    // Created Basket
    form.on('submit', function (e) {
        e.preventDefault();
        var nmb = $('#qtybutton').val();
        var product_id = $('#product_id').val();
        var product_price = $('#product_price').val();

        var data = {};
        var csrf_token = $('#form_basket_created [name="csrfmiddlewaretoken"]').val();
        var url = form.attr('action');

        data.product_id = product_id;
        data.nmb = nmb;
        data.product_price = product_price;
        data.csrfmiddlewaretoken = csrf_token;

        $.ajax({
           url: url,
           type: 'POST',
           data: data,
           cache: true,
           success: function (data) {
               console.log('OK')
               console.log(data.products_basket_count)
               if (data.products_basket_count) {
                   $('.shp__cart__wrap').html('')
                   $('#total_price_basket').html(data.basket_total_price)
                   console.log(data.products)
                   $.each(data.products, function (k, v) {
                       $('.shp__cart__wrap').append(
                        '<div class="shp__single__product">\n' +
                            '<div class="shp__pro__thumb">\n' +
                                '<a href="'+ v.url +'"><img src="'+ v.img + '" alt="product images"></a>\n' +
                            '</div>\n' +
                            '<div class="shp__pro__details">\n' +
                                '<h2><a href="'+ v.url +'">'+ v.name + '</a></h2>\n' +
                                '<span class="quantity">Количество: '+ v.nmb +'</span>\n' +
                                '<span class="shp__price">'+ v.total_price +' Сом </span>\n' +
                            '</div>\n' +
                        '</div>');
                   });
               }
           },
        });
    });


    // Update Basket Page
    var form_update = $('#form_basket_updated');
    form_update.on('submit', function (e) {
        e.preventDefault();

        var nmb = $('#qtybutton_basket').val();
        var product_id = $('#product_id').val();
        var product_price = $('#product_price').val();

        var data = {};
        var csrf_token = $('#form_basket_updated [name="csrfmiddlewaretoken"]').val();
        var url = form_update.attr('action');

        data.delete = true;
        data.product_id = product_id;
        data.nmb = nmb;
        data.product_price = product_price;
        data.csrfmiddlewaretoken = csrf_token;

        $.ajax({
           url: url,
           type: 'POST',
           data: data,
           cache: true,
           success: function (data) {
               console.log('OK')
               console.log(data.products_basket_count)
               if (data.products_basket_count) {
                   $('#form_product_basket_page').html('')
                   $('#total_basket').html(data.basket_total_price)
                   $.each(data.products, function (k, v) {
                       $('#form_product_basket_page').append(
                           '<tr>\n' +
                           '<input type="hidden" value="'+ v.id +'" id="product_id">\n' +
                           '<input type="hidden" value="'+ v.price +'" id="product_price">\n' +
                                '<td class="product-thumbnail">\n' +
                                    '<a href="{{ product_basket.product.get_absolute_url }}">\n' +
                                        '<img src="'+ v.img +'" alt="product img"/>\n' +
                                    '</a>\n' +
                                '</td>\n' +
                                '<td class="product-name">\n' +
                                    '<a href="{{ product_basket.product.get_absolute_url }}">\n' +
                                        ''+ v.name +'\n' +
                                    '</a>\n' +
                                '</td>\n' +
                                '<td class="product-price">\n' +
                                    '<span class="amount">\n' +
                                        ''+ v.price +' сом\n' +
                                    '</span>\n' +
                                '</td>\n' +
                                '<td class="product-quantity">\n' +
                                    '<input type="number" id="qtybutton_basket" value="'+ v.nmb +'"/>\n' +
                                '</td>\n' +
                               '<td class="product-subtotal">'+ v.total_price +' сом</td>\n' +
                                '<td class="product-remove"><a href="" id="delete" data-product_id="'+ v.id +'">X</a></td>\n' +
                           '</tr>'
                       )
                   })
               }
           },
        });
    });

    $(document).on('click', '#offset', function (e) {
        e.preventDefault();
    });
});
