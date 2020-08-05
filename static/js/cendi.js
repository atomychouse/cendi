function activate_paso_dos(folio,id){
    $('[href="#form-paso2"]').removeClass('disabled').click();
    $('#parent_folio,#folio_pago').html(folio);
    $('#id_parent,#parenttutor').val(id);
}

function activate_paso_tres(folio,id){
    $('[href="#form-paso3"]').removeClass('disabled').click();
    $('#folio_alumno').html(folio);
    $('#id_alumno').val(id);

}


(function($) {
$('.nav-item').click(function(e){
    e.preventDefault();
    if(!$(this).find('.nav-link').hasClass('disabled'))
    {
        var target_to_display = $(this).find('.nav-link').attr('href');
        var section_glob = $(this).parent('ul:first').attr('id');
        $(this).siblings().find('.nav-link').removeClass('active');
        $(this).find('.nav-link').addClass('active');
        var targ = '#collapse-'+section_glob + ' .collapse';
        var to_show = '#collapse-'+section_glob + ' '+target_to_display;
        $(targ).removeClass('show');
        $(to_show).addClass('show');
    }
});

$('input').blur(function(e){
    if($(this).hasClass('error_field'))
        $(this).removeClass('error_field');
});

$('.form-btn').click(function(e){
    e.preventDefault();
    $(this).parents('form:first').submit();
});

$('.sendajax').submit(function(e){
    e.preventDefault();
    var forma = $(this);
    $(this).find('.error').remove();
    $('.error_field').removeClass('error_field');
    var data = $(this).serializeArray();
    var data = new FormData(this);
    $.ajax({
        url:$(this).attr('action'),
        type:$(this).attr('method'),
        enctype: 'multipart/form-data',
        dataType:'json',
        contentType: false,
        cache: false,
        processData:false,        
        data:data,
        success:function(response){
            if(response.errors){
                $.each(response.errors,function(name_input,arry){
                    var name = name_input;
                    forma.find("[name='"+name+"']").after('<div class="error">'+arry[0].message+'</div>');
                    forma.find("[name='"+name+"']").addClass('error_field');
                });
                forma.find('.error_field:first').focus();
            }
            else
            {
                folio = response.folio;
                $.each(response.callbacks, function( index, value ) {
                    window[value](folio,response.id);
                  });
            }
        }
    });
    
});


}(jQuery));