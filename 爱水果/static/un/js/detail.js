 addShop =  function (goods_id){
    csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url:'/order/add/',
        type:'POST',
        data:{'goods_id': goods_id},
        dataType:'json',
        headers:{'X-CSRFToken': csrf},
        success:function(msg){
             // count_price()
           console.log('aa')
            // $('#num_' + goods_id).html(msg.c_num)
        },
        error:function(msg){
            alert('aaaaaa')
        }
    });
}



function subShop(goods_id){
    csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url:'/app/subgoods/',
        type:'POST',
        data:{'goods_id': goods_id},
        dataType:'json',
        headers:{'X-CSRFToken': csrf},
        success:function(msg){




        },
        error:function(msg){
            alert('aaaa')
        }
    });
}