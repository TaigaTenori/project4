/* global $ */

$(document).ready(function(){
    $('#add_recipe').click(function (){
        var ing = $('#ingredient').val();
        var quantity = $('#quantity').val();
        
        var list = $('#ingredients');
        var txt = list.val();
        
        list.val(txt + '\n' + ing + ':' + quantity);
        
        M.textareaAutoResize($('#ingredients'));
        
    });

    
    
    
});