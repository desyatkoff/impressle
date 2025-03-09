// I'm very sorry for this shit, I don't know javascript ._.


let canvas = document.getElementById("main-canvas");
let context = canvas.getContext("2d");

let brush_color = "#7f00ff";
let brush_width = "8";

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
        context.lineTo(get_x(event), get_y(event));
        context.strokeStyle = brush_color;
        context.lineWidth = brush_width;
        context.lineCap = "round";
        context.lineJoin = "round";
        context.stroke();
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


function reset_selected_color() {
    // A function that removes selected color white border for all color buttons


    document.getElementById("pastel-red-button").classList.remove("selected-color-button");
    document.getElementById("pastel-orange-button").classList.remove("selected-color-button");
    document.getElementById("pastel-yellow-button").classList.remove("selected-color-button");
    document.getElementById("pastel-green-button").classList.remove("selected-color-button");
    document.getElementById("pastel-lightblue-button").classList.remove("selected-color-button");
    document.getElementById("pastel-blue-button").classList.remove("selected-color-button");
    document.getElementById("pastel-violet-button").classList.remove("selected-color-button");
    document.getElementById("red-button").classList.remove("selected-color-button");
    document.getElementById("orange-button").classList.remove("selected-color-button");
    document.getElementById("yellow-button").classList.remove("selected-color-button");
    document.getElementById("green-button").classList.remove("selected-color-button");
    document.getElementById("lightblue-button").classList.remove("selected-color-button");
    document.getElementById("blue-button").classList.remove("selected-color-button");
    document.getElementById("violet-button").classList.remove("selected-color-button");
    document.getElementById("dark-red-button").classList.remove("selected-color-button");
    document.getElementById("dark-orange-button").classList.remove("selected-color-button");
    document.getElementById("dark-yellow-button").classList.remove("selected-color-button");
    document.getElementById("dark-green-button").classList.remove("selected-color-button");
    document.getElementById("dark-lightblue-button").classList.remove("selected-color-button");
    document.getElementById("dark-blue-button").classList.remove("selected-color-button");
    document.getElementById("dark-violet-button").classList.remove("selected-color-button");
    document.getElementById("light1-button").classList.remove("selected-color-button");
    document.getElementById("light2-button").classList.remove("selected-color-button");
    document.getElementById("light3-button").classList.remove("selected-color-button");
    document.getElementById ("dark1-button").classList.remove("selected-color-button");
    document.getElementById("dark2-button").classList.remove("selected-color-button");
    document.getElementById("dark3-button").classList.remove("selected-color-button");
}

function change_color(color) {
    // A function that updates `brush_color` variable and gives a white border for selected color button


    let hex;

    if (color == "pastel-red") {
        hex = "ff4747";

        reset_selected_color();

        document.getElementById("pastel-red-button").classList.add("selected-color-button");
    } else if (color == "red") {
        hex = "ff0000";

        reset_selected_color();

        document.getElementById("red-button").classList.add("selected-color-button");
    } else if (color == "dark-red") {
        hex = "990000";

        reset_selected_color();

        document.getElementById("dark-red-button").classList.add("selected-color-button");
    }

    if (color == "pastel-orange") {
        hex = "ffa347";

        reset_selected_color();

        document.getElementById("pastel-orange-button").classList.add("selected-color-button");
    } else if (color == "orange") {
        hex = "ff7f00";

        reset_selected_color();

        document.getElementById("orange-button").classList.add("selected-color-button");
    } else if (color == "dark-orange") {
        hex = "994c00";

        reset_selected_color();

        document.getElementById("dark-orange-button").classList.add("selected-color-button");
    }

    if (color == "pastel-yellow") {
        hex = "ffff47";

        reset_selected_color();

        document.getElementById("pastel-yellow-button").classList.add("selected-color-button");
    } else if (color == "yellow") {
        hex = "ffff00";

        reset_selected_color();

        document.getElementById("yellow-button").classList.add("selected-color-button");
    } else if (color == "dark-yellow") {
        hex = "999900";

        reset_selected_color();

        document.getElementById("dark-yellow-button").classList.add("selected-color-button");
    }

    if (color == "pastel-green") {
        hex = "47ff47";

        reset_selected_color();

        document.getElementById("pastel-green-button").classList.add("selected-color-button");
    } else if (color == "green") {
        hex = "00ff00";

        reset_selected_color();

        document.getElementById("green-button").classList.add("selected-color-button");
    } else if (color == "dark-green") {
        hex = "009900";

        reset_selected_color();

        document.getElementById("dark-green-button").classList.add("selected-color-button");
    }

    if (color == "pastel-lightblue") {
        hex = "47ffff";

        reset_selected_color();

        document.getElementById("pastel-lightblue-button").classList.add("selected-color-button");
    } else if (color == "lightblue") {
        hex = "00ffff";

        reset_selected_color();

        document.getElementById("lightblue-button").classList.add("selected-color-button");
    } else if (color == "dark-lightblue") {
        hex = "009999";

        reset_selected_color();

        document.getElementById("dark-lightblue-button").classList.add("selected-color-button");
    }

    if (color == "pastel-blue") {
        hex = "4747ff";

        reset_selected_color();

        document.getElementById("pastel-blue-button").classList.add("selected-color-button");
    } else if (color == "blue") {
        hex = "0000ff";

        reset_selected_color();

        document.getElementById("blue-button").classList.add("selected-color-button");
    } else if (color == "dark-blue") {
        hex = "000099";

        reset_selected_color();

        document.getElementById("dark-blue-button").classList.add("selected-color-button");
    }

    if (color == "pastel-violet") {
        hex = "a347ff";

        reset_selected_color();

        document.getElementById("pastel-violet-button").classList.add("selected-color-button");
    } else if (color == "violet") {
        hex = "7f00ff";

        reset_selected_color();

        document.getElementById("violet-button").classList.add("selected-color-button");
    } else if (color == "dark-violet") {
        hex = "4c0099";

        reset_selected_color();

        document.getElementById("dark-violet-button").classList.add("selected-color-button");
    } else if (color == "light1") {
        hex = "e6e6e6";

        reset_selected_color();

        document.getElementById("light1-button").classList.add("selected-color-button");
    } else if (color == "light2") {
        hex = "d9d9d9";

        reset_selected_color();

        document.getElementById("light2-button").classList.add("selected-color-button");
    } else if (color == "light3") {
        hex = "cccccc";

        reset_selected_color();

        document.getElementById("light3-button").classList.add("selected-color-button");
    } else if (color == "dark1") {
        hex = "262626";

        reset_selected_color();

        document.getElementById("dark-button").classList.add("selected-color-button");
    } else if (color == "dark2") {
        hex = "1a1a1a";

        reset_selected_color();

        document.getElementById("dark2-button").classList.add("selected-color-button");
    } else if (color == "dark3") {
        hex = "0d0d0d";

        reset_selected_color();

        document.getElementById("dark3-button").classList.add("selected-color-button");
    }


    brush_color = `#${hex}`;
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

setInterval(function() {
    brush_width = document.getElementById("width-input").value;
    document.getElementById("width-span").textContent = brush_width;
}, 100)

document.getElementById("canvas-form").addEventListener("submit", (element) => {
    element.preventDefault();
    const IMAGE_DATA = canvas.toDataURL("image/png");
    document.getElementById("image-data").value = IMAGE_DATA;


    element.target.submit();
});

