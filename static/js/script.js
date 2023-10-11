//https://stackoverflow.com/questions/15400775/jquery-ui-datepicker-disable-array-of-dates
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

    var dates = ['14-10-2023', '15-10-2023', '16-10-2023'];

    $('#datepicker').datepicker
        ({
            beforeShowDay: function (date) {
                var string = jQuery.datepicker.formatDate('dd-mm-yy', date);
                if ($.inArray(string, dates) != -1) {
                    return [true, 'highlighted-date'];
                } else {
                    return [true, ''];
                }
            },
        });


});

