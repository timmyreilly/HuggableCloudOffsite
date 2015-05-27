var ws,                 // websocket
    prev_data;          // remember data fetched last time

function establish_websocket(port) {
    if ("WebSocket" in window) {
        ws = new WebSocket("ws://" + document.domain + ":" + port.toString() + "/updated");
        ws.onstart = function () {
            ws.send('started');
        }
        ws.onmessage = function (msg) {
            load_data();
        };
        ws.onclose = function (msg) {
            $("#updated").html('SERVER DISCONNECT');
            $("#updated").css('backgroundColor', '#FFCCFF');
            $("#updated").fadeIn('fast');

        };

        // load the initial data 
        load_data();
    } else {
        alert("WebSocket not supported");
    }
}

function load_data() {
    // load data from /data, optionally providing a query parameter read from
    // the #format select

    var format = $('select#format option:selected')[0].value;
    var url = '/data' + (format ? "?format=" + format : "");
    $.ajax({
        url: url,
        success: function (data) {
            display_data(data);
        },
    });
    return true;
}

function display_data(data) {
    // show the data acquired by load_data()

    if (data && (data != prev_data)) {      // if there is data, and it's changed

        // compute a message to display comparing current data with previous data
        var msg, delta_msg;
        if (prev_data) {
            console.log("data.value:", data.value, "prev_data.value:", prev_data.value);
            var delta_value = data.value - prev_data.value;
            delta_msg = ' (<b>' + delta_value.toFixed(3) + 's</b> since last update)';
        }
        else {
            console.log("data.value:", data.value, "no prev_data");
            delta_msg = ' (first data point)';
        }
        msg = "<b>" + data.value.toFixed(3) + 's</b> since ' +
              '<a href="http://en.wikipedia.org/wiki/Unix_time">the Epoch</a>';

        // update the contents of several HTML divs via jQuery
        $('div#value').html(msg + delta_msg);
        $('div#contents').html(data.contents);

        // remember this data, in case want to compare it to next update
        prev_data = data;

        // a little UI sparkle - show the #updated div, then after a little
        // while, fade it away
        $("#updated").fadeIn('fast');
        setTimeout(function () { $("#updated").fadeOut('slow'); }, 2500);
    }
}

$(document).ready(function () {
    // inital document setup - hide the #updated message, and provide a
    // "loading..." message
    $("div#updated").fadeOut(0);
    $("div#contents").append("awaiting data...");
    $("select#format").on('change', load_data);
    $("div#contents, div#value").on('click', load_data);
});