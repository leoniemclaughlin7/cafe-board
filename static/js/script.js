
document.addEventListener("DOMContentLoaded", function () {
    // Menu collapsibles
    $('#collapseOne').click(function () {
        $('#CollapsibleOne').collapse('toggle');
    });
    $('#collapseTwo').click(function () {
        $('#CollapsibleTwo').collapse('toggle');
    });
    $('#collapseThree').click(function () {
        $('#CollapsibleThree').collapse('toggle');
    });

    // Timeout function for messages taken from I Think Therefore I Blog walkthrough
    setTimeout(function () {
        let messages = document.getElementById("msg");
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }, 3000);

    // Datepicker initialisation and ability to disable dates that are fully booked, inspiration: https://stackoverflow.com/questions/15400775/jquery-ui-datepicker-disable-array-of-dates
    const dates = JSON.parse(document.getElementById('unavailableDates').textContent);

    $('#datepicker').datepicker
        ({
            beforeShowDay: function (date) {
                var string = jQuery.datepicker.formatDate('yy-mm-dd', date);
                if ($.inArray(string, dates) != -1) {
                    return [true, 'highlighted-date'];
                } else {
                    return [true, ''];


                }
            },
        });

    // Jquery timepicker, offical docs: https://timepicker.co/#
    $('#timepicker').timepicker
        ({
            startTime: '10:00',
            interval: 60,
            timeFormat: 'HH:mm',
            minTime: '10:00',
            maxTime: '23:00',

        });
});
