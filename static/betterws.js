/*
    ws.js
*/

"use strict"

var ws,
    prev_data;

function establish_websocket(port) {
    if ("WebSocket" in window) {
        ws = new WebSocket("ws://" + document.domain + ":" + port.toString() + "/updated");

        ws.onstart = function () {
            console.log('onstart' + ws);
            ws.send('started');
        };

        ws.onmessage = function (msg) {
            load_data();
        };

        ws.onclose = function (msg) {
            $("#updated").html('Server Disconnected');
            $("#updated").css('backgroundColor', '#FFCCFF');
            $("#updated").fadeIn('fast');
        };

        load_data();
    } else {
        alert("Websocket Not Supported")
    }
}

function load_data() {
    // load data from /data 
    // use an ajax request? 
    var url = "/data";
    $.ajax({
        url: url,
        success: function (data) {
            display_data(data);
        },
    });
    return true;
}

function display_data(data) {
    // format at check the data for differences from load_data

    if (data && (data != prev_data) && data.state) {
        if (prev_data) {
            console.log("data.state: ", data.state, "prev_value.state: ", prev_data.state);
            $('div#current-state').html(data.state);
            $('div#state-list').prepend('<h3>' + data.state + ' ' + data.time + '</h3>');
        }
        else {
            console.log("data.state ", data.state, " no prev_data");
            console.log("data.time ", data.time, " but here's the time");
        }
    }

    prev_data = data

    $("#updated").fadeIn('fast');
    setTimeout(function () {
        $("#updated").fadeOut('slow');
    }, 2500);
    
}

$(document).ready(function () {
    // initial document setup and stuff
    $("#updated").fadeOut(0);
    $("#main").on(load_data);
})