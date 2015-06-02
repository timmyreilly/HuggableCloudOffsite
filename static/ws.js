var ws,                 // websocket
    prev_data;          // remember data fetched last time


function establish_websocket(port) {
    if ("WebSocket" in window) {
        ws = new WebSocket("ws://" + document.domain + ":" + port.toString() + "/updated");

        ws.onstart = function () {
            console.log('onstart I guess...' + ws);
            ws.send('started');
        };
        ws.onmessage = function (msg) {
            load_data();
        };

        ws.onclose = function (msg) {
            $("#updated").html('SERVER DISCONNECTEDDDDD');
            $("#updated").css('backgroundColor', '#FFCCFF');
            $("#updated").fadeIn('fast');
        };
        //load the initial data
        console.log('loading default stuff...');
        load_data();
    } else {
        alert("WEBSOCKETTT NOT SUPPORTEED");
    }
}

function load_data() {
    // load data from /data
    var url = '/data';
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
    
    if(data && (data != prev_data)) {
        if(prev_data) {
            console.log("data.state: ", data.state, "prev_value.state: ", prev_data.state);
            $('div#value').html(data.state);
            $('div#contents').html(data.time);
            $('div#other').html(data.time);
        }
        else {
            console.log("data.state: ", data.state, " no prev_data");
            console.log("data.time: ", data.time, " but here's the time");
        }
    }
    

    prev_data = data 

        $("#updated").fadeIn('fast');
        setTimeout(function() { $("#updated").fadeOut('slow'); }, 2500);
}

// OLD CODE
        // compute a message to display comparing current data with previous data
        //var msg, delta_msg;
        //if (prev_data) {
        //    console.log("data.state", data.state, "prev_data.state", prev_data.state);
        //    var delta_value = "we think it's changed";
        //    delta_msg = ' (<b>' + delta_value + '</b> okay...)';
        //}
        //else {
        //    console.log("data.state", data.state, "no prev_data");
        //    console.log("data.time", data.time, "current time of request...");
        //    delta_msg = ' (first data point)';
        //}
        ////msg = "<b>" + data.state + "</b> is the current cloud state at this time -> " + "<b>" + data.time "</b>";
        //// this is the message that will be sent to the client?
        //msg = "this is the message";


        //$('div#value').html(msg + delta_msg);
        //$('div#contents').html(data.state);
        //$('div#other').html(data.time);
        //if (data.state != data.prev_state) {
        //    $('div#state-list').prepend('<h3>' + data.state + ' is different from ' + data.prev_state)
        //}
        //$('div#state-list').prepend('<h2>' + data.state + data.time + '</h2>');

        //// remember this data, in case we want to compare it to next update...
        //prev_data = data;
        //prev_state = data.state;

        // A little UI Sparkle - show the update div then after a little while fade it away...


$(document).ready(function() {
    // intial document setup - hide the #updated message and provide a 'loading...' message

    $("div#updated").fadeOut(0);
    //$("div#contents").append("loading...");
    $("div#contents, div#value").on('click', load_data);
    $("div#contents, div#value").on(load_data);
})
