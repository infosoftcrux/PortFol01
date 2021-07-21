(function ($) {
    "use strict"


    // Navbar on scrolling
    $(window).scroll(function () {
        if ($(this).scrollTop() > 200) {
            $('.navbar').fadeIn('slow').css('display', 'flex');
        }
        else {
            $('.navbar').fadeOut('slow').css('display', 'none');
        }
    });

    // Typed Initiate
    if ($('.typed-text-output').length == 1) {
        var typed_str = $('.typed-text').text();
        var typed = new Typed('.typed-text-output', {
            strings: typed_str.split(', '),
            typeSpeed: 50,
            backSpeed: 30,
            smartBackspace: false,
            backDelay: 1000,
            loop: true
        });

    }
    // Smooth scrolling on the navbar links
    $(".navbar-nav a").on('click', function (event) {
        if (this.hash !== "") {
            event.preventDefault();
            var hash = this.hash;
            $('html , body').animate({
                scrollTop: $(hash).offset().top - 40
            }, 1100, 'swing');
            if ($(this).parents('.navbar-nav').length) {
                $('.navbar-nav .active').removeClass('active');
                $(this).closest('a').addClass('active');
            }
        }
    });
    $("#homeaboutbtn").on('click', function (event) {
        if (this.hash !== "") {
            event.preventDefault();
            var hash2 = this.hash;
            $('html , body').animate({
                scrollTop: $(hash2).offset().top - 45
            }, 1100, 'swing');
        }
    });

    // Onscroll events
    $(window).scroll(function (event) {
        var scrollPos = $(document).scrollTop();
        $('#navbarCollapse a').each(function () {
            var currLink = $(this);
            var refElement = $(currLink.attr("href"));
            if (refElement.position().top <= scrollPos && refElement.position().top + refElement.height() > scrollPos) {
                $('#navbarCollapse a').removeClass("active");
                currLink.addClass("active");
            }
            else {
                currLink.removeClass("active");
            }
        });
    });
    // Portfolio isotope and filter
    var PortfolioIsoTape = $('.portfolio-container').isotope({ itemSelector: '.portfolio-item', layoutMode: 'fitRows' });
    $('#portfolio-filters li').on('click', function () {
        $('#portfolio-filters li').removeClass('active');
        $(this).addClass('active');
        PortfolioIsoTape.isotope({ filter: $(this).data('filter') });
    });

    // for managing youtube links
    $('.videostatus').find('a').each(function () {
        var statlink = $(this).attr('href');
        if (statlink == "") {
            $(this).attr('href', '#')
            $(this).parent().removeClass('d-flex')
            $(this).parent().addClass('d-none')
        }
    });

    // for managing social links 
    $('.socialbtn').find('a').each(function () {
        var stlink = $(this).attr('href');
        if (stlink == "") {
            // $(this).attr('href', '#')
            $(this).addClass('d-none');
        }
    });

   

    // Skillbar
    $('.skill').waypoint(function () {
        $('.progress .progress-bar').each(function () {
            $(this).css('width', $(this).attr("aria-valuenow") + '%');
        });
    }, { offset: '80%' });


   

    
})(jQuery);