document.addEventListener("DOMContentLoaded", function () {

    $('#collapseOne').click(function () {
        $('#CollapsibleOne').collapse('toggle');
    });
    $('#collapseTwo').click(function () {
        $('#CollapsibleTwo').collapse('toggle');
    });
    $('#collapseThree').click(function () {
        $('#CollapsibleThree').collapse('toggle');
    });

    setTimeout(function () {
        let messages = document.getElementById("msg");
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }, 3000);

});
