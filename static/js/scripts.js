$(document).ready(function() {
    // Tu código jQuery aquí
    $('.skull-img').click(function() {
        var skull = $(this);
        skull.addClass('vibrate');
        setTimeout(function() {
            skull.removeClass('vibrate');
        }, 200);
    });
});