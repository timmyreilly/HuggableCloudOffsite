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
        }
    }
}

function load_data() {
    // load data from /data 
    // use an ajax request? 
}

function display_data(data) {
    // format at check the data for differences from load_data
}

$(document).ready(function () {
    // initial document setup and stuff
})