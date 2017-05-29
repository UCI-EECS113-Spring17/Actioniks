'use strict';

$(document).ready(function () {
    $('.menu-item').click(function () {
        $('.menu-item').each(function () {
            $(this).removeClass('active');
        });
        $(this).addClass('active');
        var id = $(this).attr('id');
        $('.main').find('.row').children().each(function () {
            if ($(this).hasClass(id)) {
                $(this).css('display', 'block');
            } else $(this).css('display', 'none');
        });
    });
});