$(document).ready(function () {
	//inja script ro neveshtam vase flat btn
	$('#bombtitle').html('عنوان بمب ها');
	$('#bombdis').html('توضیح بمب ها')

	$('.medalslider').owlCarousel({
		center: true,
		loop: true,
		margin: 10,
		autoplayHoverPause: true,
		responsive: {
			0: {
				items: 5
			}
		},
		dots: false,
		autoplay: true,
		autoplayTimeout: 3000
	});
	$('.gameslider').owlCarousel({
		center: true,
		loop: true,
		autoplayHoverPause: true,
		margin: 10,
		responsive: {
			0: {
				items: 2
			}
		},
		dots: false,
		autoplay: true,
		autoplayTimeout: 3000
	});
	$('.tableslider').owlCarousel({
		center: true,
		loop: true,
		margin: 10,
		autoplayHoverPause: true,
		responsive: {
			0: {
				items: 1
			}
		},
		dots: false,
		autoplay: true,
		autoplayTimeout: 3000
	});
	$('#owl-demo-2').owlCarousel({
		autoplay: true,
		autoplayTimeout: 1000,
		autoplayHoverPause: true,
		autoplayHoverPause: true,

		items: 3,
		loop: true,
		center: false,
		rewind: false,

		mouseDrag: true,
		touchDrag: true,
		pullDrag: true,
		freeDrag: false,

		margin: 0,
		stagePadding: 0,

		merge: false,
		mergeFit: true,
		autoWidth: false,

		startPosition: 0,
		rtl: false,

		smartSpeed: 250,
		fluidSpeed: false,
		dragEndSpeed: false,
		responsive: {
			0: {
				items: 1,
				nav: true
			},
			480: {
				items: 2,
				nav: false
			},
			768: {
				items: 3,
				nav: true,
				loop: false
			},
			992: {
				items: 4,
				nav: true,
				loop: false
			}
		},
		responsiveRefreshRate: 200,
		responsiveBaseElement: window,

		fallbackEasing: 'swing',

		info: false,

		nestedItemSelector: false,
		itemElement: 'div',
		stageElement: 'div',

		refreshClass: 'owl-refresh',
		loadedClass: 'owl-loaded',
		loadingClass: 'owl-loading',
		rtlClass: 'owl-rtl',
		responsiveClass: 'owl-responsive',
		dragClass: 'owl-drag',
		itemClass: 'owl-item',
		stageClass: 'owl-stage',
		stageOuterClass: 'owl-stage-outer',
		grabClass: 'owl-grab',
		autoHeight: false,
		lazyLoad: false
	});
});