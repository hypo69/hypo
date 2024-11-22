$(document).ready(function() {
	var $newSlideConf = $('.pos_new_product');
	var items       = parseInt($newSlideConf.attr('data-items'));
	var speed     	= parseInt($newSlideConf.attr('data-speed'));
	var autoPlay    = parseInt($newSlideConf.attr('data-autoplay'));
	var time    	= parseInt($newSlideConf.attr('data-time'));
	var arrow       = parseInt($newSlideConf.attr('data-arrow'));
	var pagination  = parseInt($newSlideConf.attr('data-pagination'));
	var move        = parseInt($newSlideConf.attr('data-move'));
	var pausehover  = parseInt($newSlideConf.attr('data-pausehover'));
	var lg          = parseInt($newSlideConf.attr('data-lg'));
	var md          = parseInt($newSlideConf.attr('data-md'));
	var sm          = parseInt($newSlideConf.attr('data-sm'));
	var xs          = parseInt($newSlideConf.attr('data-xs'));
	var xxs         = parseInt($newSlideConf.attr('data-xxs'));	
	
	if(autoPlay==1) {
		if(time){
			autoPlay = time; 
		}else{
			autoPlay = '3000';
		}
	}else{
		autoPlay = false;
	}
	if(pausehover){pausehover = true}else{pausehover=false}
	if(move){move = false}else{move=true}
	if(arrow){arrow =true}else{arrow=false}
	if(pagination==1){pagination = true}else{pagination=false}

	var newSlide = $(".pos_new_product .newSlide");
	newSlide.owlCarousel({
		autoPlay : autoPlay ,
		smartSpeed: speed,
		autoplayHoverPause: pausehover,
		scrollPerPage: move,
		nav: arrow,
		dots : pagination,	
		responsive:{
			0:{
				items:xxs,
			},
			360:{
				items:xs,
			},	
			576:{
				items:sm,
			},
			768:{
				items:md,
			},
			992:{
				items:lg,
			},
			1200:{
				items:items,
			}
		}
	});
	checkClasses();
    newSlide.on('translated.owl.carousel', function(event) {
        checkClasses();
    });

    function checkClasses(){
		var total = $('.pos_new_product .newSlide .owl-stage .owl-item.active').length;
        $('.pos_new_product ').each(function(){
			$(this).find('.owl-item').removeClass('firstActiveItem');
			$(this).find('.owl-item').removeClass('lastActiveItem');
			$(this).find('.owl-item.active').each(function(index){
				if (index === 0) { $(this).addClass('firstActiveItem'); }
				if (index === total - 1 && total>1) {
					$(this).addClass('lastActiveItem');
				}
			})  
        });
    }
});

