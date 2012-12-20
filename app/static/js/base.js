/**
 * @author Administrator
 */
// function pageScroll(to,step) {
// window.scrollBy(0, step);
//
// scrolldelay = setTimeout('pageScroll('+to+','+step+')', 10);
//
// if(window.scrollY==to){
// clearTimeout(scrolldelay);
// }
// }
$(document).ready(function() {

	$(".navigation a").eq(0).click(function() {
		$("html,body").animate({
			scrollTop : 0
		}, 1000);

	})

	$(".navigation a").eq(0).hover(function() {
		$(this).addClass('bhover');
		$(this).removeClass('works')
	}, function() {
		$(this).addClass('works')
		$(this).removeClass('bhover');
	})

	$(".navigation a").eq(1).click(function() {
		$("html,body").animate({
			scrollTop : $(".bottom").offset().top
		}, 1000);

	})

	$(".navigation a").eq(1).hover(function() {
		$(this).removeClass('aboutus');
		$(this).addClass('ahover');
	}, function() {
		$(this).removeClass('ahover');
		$(this).addClass('aboutus');
	})

	$(".navigation a").eq(2).click(function() {
		$("html,body").animate({
			scrollTop : $(".contact").offset().top
		}, 2000);
	})

	$(".navigation a").eq(2).hover(function() {
		$(this).addClass('chover');
		$(this).removeClass('contactus');

	}, function() {
		$(this).addClass('contactus');
		$(this).removeClass('chover');
	})

	$(".btn-top").click(function() {
		$("html,body").animate({
			scrollTop : 0
		}, 1000);

	})
})
var BaseInit = {
	init : function() {
		this.bindContentForm();
		// this.bindPhotoForm();
		this.bindPhotoHover();
	},

	getCookie : function(name) {
		var cookieValue = null;
		if(document.cookie && document.cookie != '') {
			var cookies = document.cookie.split(';');
			for(var i = 0; i < cookies.length; i++) {
				var cookie = jQuery.trim(cookies[i]);
				if(cookie.substring(0, name.length + 1) == (name + '=')) {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	},

	bindContentForm : function() {
		var element = this;

		var showlist = $(".shows-list")

		$(".story").find('input[name="submit"]').live('click', function(e) {
			e.preventDefault();
			var one = $(".shows-list div").eq(0);

			var template = $("#tp").clone();
			var val = $(".storycontent").val().replace(/\t/g, '');
			var name = $("#username").val().replace(/\t/, null);

			templateContent = template.html();
			if(val == '' || val.length < 10) {
				alert("内容不得少于十个字符！")
				return false;
			} else {
				$.ajax({
					type : "POST",
					url : "/publish/",
					dataType : "json",
					data : {
						'story' : val,
						'name' : name,
						'csrfmiddlewaretoken' : BaseInit.getCookie('csrftoken')
					},
					success : function(d) {

						templateContent = templateContent.replace(/\{content\}/g, d.content);
						templateContent = templateContent.replace(/\{username\}/g, d.username);
						templateContent = templateContent.replace(/\{addtime\}/g, d.var_date);
						templateContent = template.html(templateContent);
						templateContent.attr("id", 'story-' + d.id);
						one.before(template.show());
						$(".storycontent").val('');
						$("#username").val("");

					}
				})

			}

		})
	},

	bindPhotoHover : function() {
		
		$(".photos img").hover(function() {
			var src = $(this).attr("src")
			$(this).attr("src", src.replace(/-hover.jpg/g, "-thumb.jpg"))
		},
		function() {
			var src = $(this).attr("src")
			$(this).attr("src", src.replace(/-thumb.jpg/g, "-hover.jpg"))

		})
		$(".photos img").live('click',function(){

				
		})
	}
	// bindPhotoForm:function(){
	// $picture=$(".contact");
	// $(".contacts").find("input[name=button]").live('click',function(e){
	// e.preventDefault();
	//
	// $(".contacts form").submit();
	//
	//
	// })

	// }

}
