/* global $ */
$(document).delegate('[id^=remove_ingredient]', 'click', function()
{
   console.log('click');
   $(this).closest('.added_div').remove(); 
});

$(document).ready(function(){
    var click = 0;

    $('#add_ingredient').click(function (){
        
        var a = $(`<div class="added_div" id="row">
               <div class="ing1 input-field col s6">
                  <i class="material-icons prefix">flag</i>
                  <input name="ingredient${click}" id="ing${click}" type="text">
                  <label for="ingredient${click}">Ingredient</label>
                </div>
               <div class="quant input-field col s3">
                  <i class="material-icons prefix">flag</i>
                  <input name="quantity${click}" id="quant${click}" type="text">
                  <label for="quantity${click}">Quantity</label>
                </div>
               <div class="input-field col s3">
                    <a id="remove_ingredient${click}" class="btn-floating btn-small waves-effect waves-light red"><i class="material-icons">indeterminate_check_box</i></a>
                </div>
            </div>`);

        click++;
        a.insertAfter('#ingredients');
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
                $('#upvote_button').addClass('blackandwhite').off('click');
                
                },
            error: function(error) {
                console.log(error);
            }
        });
    });

    
    
    
});