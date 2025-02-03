let canvas = document.getElementById("main-canvas");
let context = canvas.getContext("2d");
let stroke_color = "#7f00ff";
let stroke_width = "4";
let is_drawing = false;


context.fillStyle = "#1a1a1a";
context.fillRect(0, 0, canvas.width, canvas.height);


function start(event) {
    is_drawing = true;
    context.beginPath();
    context.moveTo(get_x(event), get_y(event));

    event.preventDefault();
}


function draw(event) {
    if (is_drawing) {
        context.lineTo(get_x(event), get_y(event));
        context.strokeStyle = stroke_color;
        context.lineWidth = stroke_width;
        context.lineCap = "round";
        context.lineJoin = "round";
        context.stroke();
    }

    event.preventDefault();
}


function stop(event) {
    if (is_drawing) {
        context.stroke();
        context.closePath();
        is_drawing = false;
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

canvas.addEventListener("touchstart", start, false);
canvas.addEventListener("touchmove", draw, false);
canvas.addEventListener("touchend", stop, false);
canvas.addEventListener("mousedown", start, false);
canvas.addEventListener("mousemove", draw, false);
canvas.addEventListener("mouseup", stop, false);
canvas.addEventListener("mouseout", stop, false);

document.getElementById("canvas-form").addEventListener("submit", (element) => {
    element.preventDefault();
    const IMAGE_DATA = canvas.toDataURL("image/png");
    document.getElementById("image-data").value = IMAGE_DATA;


    element.target.submit();
});
