$(document).ready(function(){
    //inja script ro neveshtam vase flat btn
	$('#bombtitle').html('عنوان بمب ها');
    $('#bombdis').html('توضیح بمب ها')
    
    $('.medalslider').owlCarousel({
        center: true,
        loop:true,
        dots:false,
        autoplay:true,
        autoplayTimeout:2000,
        autoplayHoverPause:true,
        animateIn:true,
        autoplayHoverPause:true,
        responsive:{
            0:{
                items:5
            }
        }
    });
    $('.tableslider').owlCarousel({
        center: true,
        loop:true,
        dots:false,
        autoplay:true,
        autoplayTimeout:2000,
        autoplayHoverPause:true,
        autoplayHoverPause:true,
        responsive:{
            0:{
                items:1
            }
        }
    });
  });
  