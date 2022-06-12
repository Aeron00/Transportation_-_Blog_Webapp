var nav = document.getElementById('nav_bar');
window.onscroll = function () {
    if (window.pageYOffset > 100) {
        nav.className = "navbar navbar-expand-lg navbar-white fixed-top bg-dark bg-opacity-50";
    }
    else {
        nav.className = "navbar navbar-expand-lg navbar-dark fixed-top bg-dark";
    }
}



// $(document).ready(function () {
//     $('.menu').click(function () {
//         $('ul').toggleClass('active');
//     })
// })


// $(document).ready(function () {
//     if($('.sideTabs a').length)
// 		{
// 			var links = $('.sideTabs a');
// 	    	links.each(function()
// 	    	{
//                 var ele = $(this);
//                 console.log(ele)
// 	    		var target = ele.data('scroll-to');
// 	    		ele.on('click', function(e)
// 	    		{
//                     e.preventDefault();
//                     $('html, body').animate({ scrollTop: $(target).offset().top-90});
// 	    		});
// 	    	});
// 		}	
// });

