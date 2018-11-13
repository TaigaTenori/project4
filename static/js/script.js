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
        var txt = list.val();
        
        list.val(txt + '\n' + ing + ': ' + quantity);
        
        x.val('');
        y.val('');
        M.textareaAutoResize($('#ingredients'));
        
    });

    
    
    
});