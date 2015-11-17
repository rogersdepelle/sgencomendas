$('input').removeClass('validate')

$(document).ready(function() {
    $('select').material_select();
    $('input[value="undefined"]').val("Selecione");
    $('.modal-trigger').leanModal();    
});

$('#id_delivery').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 10, // Creates a dropdown of 15 years to control year
    format: 'yyyy-mm-dd'
});

jQuery(function($){
    $("#id_phone").mask("(99) 9999-9999");
});

jQuery(function($){
    $("#id_cpf").mask("999.999.999-99");
});

$(".button-collapse").sideNav();
