//toggle for profile//
$("[data-toggle='toggle']").click(function() {
    var selector = $(this).data("target");
    $(selector).toggleClass('in');
});

//popover for profile)//
$(function(){
    $('#post').popover({
        placement: 'bottom',
        title: 'Popover Form',
        html:true,
        content:  $('#myForm').html()
    }).on('click', function(){
    $('.btn-primary').click(function(){
    $('#result').after("form submitted by " + $('#title').val())
        $.post('/echo/html/',  {
            title: $('#title').val(),
        }, function(r){
        $('#pops').popover('hide')
        $('#result').html('resonse from server could be here' )
        })
    })
})
})
