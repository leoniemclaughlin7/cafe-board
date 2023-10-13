//https://stackoverflow.com/questions/15400775/jquery-ui-datepicker-disable-array-of-dates
document.addEventListener("DOMContentLoaded", function () {

    console.log("JavaScript loaded");
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

    $('#timepicker').timepicker
        ({
            startTime: '10:00',
            interval: 120,
            timeFormat: 'HH:mm',
            disableTimeRanges: [["02:00", "04:00"], ["06:00", "08:00"]]
        });

});
