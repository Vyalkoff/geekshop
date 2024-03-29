window.onload = function (){
    let _quantity, _price, orderitem_num, delta_quantity, orderitem_quantity,delta_cost;

    let quantity_arr = []
    let price_arr = []
    let order_form = '.order_form'

    let total_forms = parseInt($('input[name = orderitems-TOTAL_FORMS]').val())
    console.log(total_forms)

    let order_total_quantity = parseInt($('.order_total_quantity').text()) || 0;
    let order_total_price = parseInt($('.order_total_cost').text().replace(',','.')) || 0;


    for (let i = 0; i < total_forms; i++){
        _quantity = parseInt($('input[name=orderitems-' + i +'-quantity]').val());
        _price = parseInt($('.orderitems-' + i +'-price').text().replace(',','.'));

        quantity_arr[i] = _quantity
        if(_price){
            price_arr[i] = _price;

        }else{
            price_arr[i] = 0;
        }
    }
    // console.info('PRICE',price_arr)
    // console.info('QUANTITY',quantity_arr)

    $(order_form).on('click','input[type=number]',function(event){
        let target = event.target;
        orderitem_num = parseInt(target.name.replace('orderitems-','').replace('-quantity',''));

        if (price_arr[orderitem_num]){
            orderitem_quantity = parseInt(target.value);
            delta_quantity= orderitem_quantity - quantity_arr[orderitem_num];
            quantity_arr[orderitem_num] = orderitem_quantity;
            orderSummerUpdate(price_arr[orderitem_num],delta_quantity);


        }
    });

     $(order_form).on('click','input[type=checkbox]',function(event){
        let target = event.target;
        orderitem_num = parseInt(target.name.replace('orderitems-','').replace('-DELETE',''));
        if (target.checked){
            delta_quantity = -quantity_arr[orderitem_num]
        }else{
             delta_quantity = quantity_arr[orderitem_num]
        }
        orderSummerUpdate(price_arr[orderitem_num],delta_quantity);
    });

     function  orderSummerUpdate(orderitem_price,delta_quantity){
        delta_cost = orderitem_price * delta_quantity
        order_total_price = Number((order_total_price+delta_cost).toFixed(2));
        order_total_quantity = order_total_quantity + delta_quantity;
        $('.order_total_quantity').html(order_total_quantity.toString());
        $('.order_total_cost').html(order_total_price.toString() + ',00');
    }





    $('.formset_row').formset({
        addText: 'добавить продукт',
        prefix: 'orderitems',
        deleteText: 'удалить',
        removed: deleteOrderItem,


    });
    function deleteOrderItem(row){
        let target_name = row[0].querySelector('input[type="number"]').name;
        orderitem_num = parseInt(target_name.replace('orderitems-','').replace('-quantity',''));
        delta_quantity= -quantity_arr[orderitem_num];
        orderSummerUpdate(price_arr[orderitem_num],delta_quantity);
    }



}