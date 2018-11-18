/* global $ */

$(document).ready(function(){
    $('#add_recipe').click(function (){
        var x =  $('#ingredient');
        var y =  $('#quantity');
        
        var ing = x.val();
        var quantity = y.val();
        
        if (ing == '' || quantity == '') {
            window.alert('Both Ingredient and Quantity fields must not be empty');
            return;
        }
        var list = $('#ingredients');
        var list2 = $('#quantities');
        var txt = list.val();
        var txt2 = list2.val();
        var app = ''
        if (txt != '') {
            app = '\n' ;
        }
        list.val(txt + app + ing);
        list2.val(txt2 + app + quantity)
        
        x.val('');
        y.val('');
        
        M.textareaAutoResize($('#ingredients'));
        M.textareaAutoResize($('#quantities'));
        
    });

    $('#upvote_button').click(function() {
        $.ajax({
            url: '/upvote/' + $('#span_rid').text(),
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
                var uv = $('#upvotes');
                uv.text(parseInt(uv.text()) + 1);
                $('#upvote_button').remove();
                },
            error: function(error) {
                console.log(error);
            }
        });
    });

    
    
    
});