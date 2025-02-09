let canvas = document.getElementById("main-canvas");
let context = canvas.getContext("2d");

let brush_color = "#7f00ff";
let eraser_color = "#1a1a1a";

let width = "8";

let mode = "draw";

let is_mousedown = false;


context.fillStyle = "#1a1a1a";
context.fillRect(0, 0, canvas.width, canvas.height);


function start(event) {
    is_mousedown = true;
    context.beginPath();
    context.moveTo(get_x(event), get_y(event));

    event.preventDefault();
}

function draw(event) {
    if (is_mousedown == true) {
        if (mode == "draw") {
            context.lineTo(get_x(event), get_y(event));
            context.strokeStyle = brush_color;
            context.lineWidth = width;
            context.lineCap = "round";
            context.lineJoin = "round";
            context.stroke();
        }
        else if (mode == "erase") {
            context.lineTo(get_x(event), get_y(event));
            context.strokeStyle = eraser_color;
            context.lineWidth = width;
            context.lineCap = "round";
            context.lineJoin = "round";
            context.stroke();
        }
    }

    event.preventDefault();
}

function stop(event) {
    if (is_mousedown == true) {
        context.stroke();
        context.closePath();
        is_mousedown = false;
    }

    event.preventDefault();
}

function get_x(event) {
    if (event.pageX == undefined) {
        return event.targetTouches[0].pageX - canvas.offsetLeft;
    }
    else {
        return event.pageX - canvas.offsetLeft;
    }
}

function get_y(event) {
    if (event.pageY == undefined) {
        return event.targetTouches[0].pageY - canvas.offsetTop;
    }
    else {
        return event.pageY - canvas.offsetTop;
    }
}

function reset_canvas() {
    context.fillRect(0, 0, canvas.width, canvas.height);
}


canvas.addEventListener("touchstart", start, false);
canvas.addEventListener("touchmove", draw, false);
canvas.addEventListener("touchend", stop, false);
canvas.addEventListener("mousedown", start, false);
canvas.addEventListener("mousemove", draw, false);
canvas.addEventListener("mouseup", stop, false);
canvas.addEventListener("mouseout", stop, false);

document.addEventListener("keydown", function(event) {
    if (event.shiftKey) {
        if (mode == "draw") {
            mode = "erase";
        }
        else {
            mode = "draw";
        }
    }
});

setInterval(function() {
    width = document.getElementById("width-input").value;
    document.getElementById("width-span").textContent = width;
}, 100)

document.getElementById("canvas-form").addEventListener("submit", (element) => {
    element.preventDefault();
    const IMAGE_DATA = canvas.toDataURL("image/png");
    document.getElementById("image-data").value = IMAGE_DATA;


    element.target.submit();
});
