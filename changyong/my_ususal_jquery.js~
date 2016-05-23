/*
 ajax 用法
 */
$.ajax({
                type: "POST",
                url: "{url:/assist/cancelOrder}",
                data: "order_id="+orderId,
                success: function(msg){
                    alert( "Data Saved: " + msg );
                },
                error: function(XMLHttpRequest, textStatus, errorThrown){
                    alert(XMLHttpRequest.readyState + XMLHttpRequest.status + XMLHttpRequest.responseText);
                }
            });
