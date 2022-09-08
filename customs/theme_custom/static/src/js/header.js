$('#wrapwrap').scroll(function() {
    var scroll = $('#wrapwrap').scrollTop();
    if(scroll > 50)
    {
     $(".nav-logo").removeClass("brand-logo1").addClass("brand-logo2");
     $(".nav-logo2").removeClass("nav-brand1").addClass("nav-brand2");
    }
    else
    {
    $(".nav-logo").addClass("brand-logo1").removeClass("brand-logo2");
    $(".nav-logo2").removeClass("nav-brand2").addClass("nav-brand1");
    }
    $('#top').removeAttr("style")
});

$('document').ready(function(){
$(".navbar-toggler").addClass("collapsed");

$('.navbar-toggler-icon').click(function(){
if($('.collapsed').is(':visible'))
{
$(".nav-logo2").removeClass("nav-brand1").addClass("nav-brand2");
}
else
{
$(".nav-logo2").removeClass("nav-brand2").addClass("nav-brand1");
}
});
});
