// autofit <ul>
function sliderAutoWidth() {
	var numOf = $("#content-holder > li").length;
	$("#content-holder").width(numOf * 180);
}

$(document).ready(function() {
	$("a.anchorLink").anchorAnimate()
	if(document.location.hash.length < 1) {
		//document.location = "#home";
		$("a.home.anchorLink").click();
	}
	sliderAutoWidth();
});


/* Fancybox */

		$(document).ready(function() {
			
			$("a.fancy").fancybox({
				'padding'		: 0,
				'titleShow'		: true,
				'transitionIn'	: 'elastic',
				'transitionOut'	: 'elastic',
				'easingIn'      : 'easeOutBack',
				'easingOut'     : 'easeInBack',
				'speedIn'		:	500,
			});

		});

		
		
/* Moving Clouds */		
		$(function(){
		
		  $('#wrapper').css({backgroundPosition: '0px 0px'});
		  
		
			$('#wrapper').animate({
				backgroundPosition:"(-10000px 0px)"
			}, 580000, 'linear');
			
		});


/* Fade Hover */

    $(function () {
  // IE6 doesn't handle the fade effect very well - so we'll stick with
  // the default non JavaScript version if that is the user's browser.
  if ($.browser.msie && $.browser.version < 8) return;
  
  $('.navigation li, .badge li, .portimg li')
  
    // remove the 'highlight' class from the li therefore stripping 
    // the :hover rule
    .removeClass('highlight')
    
    // within the context of the li element, find the a elements
    .find('a')
    
    // create our new span.hover and loop through anchor:
    .append('<span class="hover" />').each(function () {
      
      // cache a copy of the span, at the same time changing the opacity
      // to zero in preparation of the page being loaded
      var $span = $('> span.hover', this).css('opacity', 0);
      
      // when the user hovers in and out of the anchor
      $(this).hover(function () {
        // on hover
        
        // stop any animations currently running, and fade to opacity: 1
        $span.stop().fadeTo(500, 1);
      }, function () {
        // off hover
        
        // again, stop any animations currently running, and fade out
        $span.stop().fadeTo(500, 0);
      });
    });
});