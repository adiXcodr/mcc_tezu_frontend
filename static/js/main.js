$(document).ready(function(){
    $('i').click(function(){
        $('.main_header').toggleClass('active');
        $('.main_header').toggleClass('tray-transition');
    })
})

var windowWidth = $(window).width();
if(windowWidth<768)
{
    document.getElementById('header_logo').classList.remove('mobil');
    document.getElementById('header_logo').classList.add('show');
}

