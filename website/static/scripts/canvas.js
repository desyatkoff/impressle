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

function change_color(color) {
    const BRIGHT_RED_BUTTON = document.getElementById("bright-red-button");
    const BRIGHT_ORANGE_BUTTON = document.getElementById("bright-orange-button");
    const BRIGHT_YELLOW_BUTTON = document.getElementById("bright-yellow-button");
    const BRIGHT_GREEN_BUTTON = document.getElementById("bright-green-button");
    const BRIGHT_LIGHTBLUE_BUTTON = document.getElementById("bright-lightblue-button");
    const BRIGHT_BLUE_BUTTON = document.getElementById("bright-blue-button");
    const BRIGHT_VIOLET_BUTTON = document.getElementById("bright-violet-button");
    const RED_BUTTON = document.getElementById("red-button");
    const ORANGE_BUTTON = document.getElementById("orange-button");
    const YELLOW_BUTTON = document.getElementById("yellow-button");
    const GREEN_BUTTON = document.getElementById("green-button");
    const LIGHTBLUE_BUTTON = document.getElementById("lightblue-button");
    const BLUE_BUTTON = document.getElementById("blue-button");
    const VIOLET_BUTTON = document.getElementById("violet-button");
    const DARK_RED_BUTTON = document.getElementById("dark-red-button");
    const DARK_ORANGE_BUTTON = document.getElementById("dark-orange-button");
    const DARK_YELLOW_BUTTON = document.getElementById("dark-yellow-button");
    const DARK_GREEN_BUTTON = document.getElementById("dark-green-button");
    const DARK_LIGHTBLUE_BUTTON = document.getElementById("dark-lightblue-button");
    const DARK_BLUE_BUTTON = document.getElementById("dark-blue-button");
    const DARK_VIOLET_BUTTON = document.getElementById("dark-violet-button");

    let hex;

    if (color == "bright-red") {
        hex = "ff4747";


        BRIGHT_RED_BUTTON.classList.add("selected-color-button");

        BRIGHT_ORANGE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_YELLOW_BUTTON.classList.remove("selected-color-button");
        BRIGHT_GREEN_BUTTON.classList.remove("selected-color-button");
        BRIGHT_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_BLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_VIOLET_BUTTON.classList.remove("selected-color-button");
        RED_BUTTON.classList.remove("selected-color-button");
        ORANGE_BUTTON.classList.remove("selected-color-button");
        YELLOW_BUTTON.classList.remove("selected-color-button");
        GREEN_BUTTON.classList.remove("selected-color-button");
        LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BLUE_BUTTON.classList.remove("selected-color-button");
        VIOLET_BUTTON.classList.remove("selected-color-button");
        DARK_RED_BUTTON.classList.remove("selected-color-button");
        DARK_ORANGE_BUTTON.classList.remove("selected-color-button");
        DARK_YELLOW_BUTTON.classList.remove("selected-color-button");
        DARK_GREEN_BUTTON.classList.remove("selected-color-button");
        DARK_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        DARK_BLUE_BUTTON.classList.remove("selected-color-button");
        DARK_VIOLET_BUTTON.classList.remove("selected-color-button");
    } else if (color == "red") {
        hex = "ff0000";

        RED_BUTTON.classList.add("selected-color-button");

        BRIGHT_RED_BUTTON.classList.remove("selected-color-button");
        BRIGHT_ORANGE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_YELLOW_BUTTON.classList.remove("selected-color-button");
        BRIGHT_GREEN_BUTTON.classList.remove("selected-color-button");
        BRIGHT_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_BLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_VIOLET_BUTTON.classList.remove("selected-color-button");
        ORANGE_BUTTON.classList.remove("selected-color-button");
        YELLOW_BUTTON.classList.remove("selected-color-button");
        GREEN_BUTTON.classList.remove("selected-color-button");
        LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BLUE_BUTTON.classList.remove("selected-color-button");
        VIOLET_BUTTON.classList.remove("selected-color-button");
        DARK_RED_BUTTON.classList.remove("selected-color-button");
        DARK_ORANGE_BUTTON.classList.remove("selected-color-button");
        DARK_YELLOW_BUTTON.classList.remove("selected-color-button");
        DARK_GREEN_BUTTON.classList.remove("selected-color-button");
        DARK_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        DARK_BLUE_BUTTON.classList.remove("selected-color-button");
        DARK_VIOLET_BUTTON.classList.remove("selected-color-button");
    } else if (color == "dark-red") {
        hex = "990000";

        DARK_RED_BUTTON.classList.add("selected-color-button");

        BRIGHT_RED_BUTTON.classList.remove("selected-color-button");
        BRIGHT_ORANGE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_YELLOW_BUTTON.classList.remove("selected-color-button");
        BRIGHT_GREEN_BUTTON.classList.remove("selected-color-button");
        BRIGHT_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_BLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_VIOLET_BUTTON.classList.remove("selected-color-button");
        RED_BUTTON.classList.remove("selected-color-button");
        ORANGE_BUTTON.classList.remove("selected-color-button");
        YELLOW_BUTTON.classList.remove("selected-color-button");
        GREEN_BUTTON.classList.remove("selected-color-button");
        LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BLUE_BUTTON.classList.remove("selected-color-button");
        VIOLET_BUTTON.classList.remove("selected-color-button");
        DARK_ORANGE_BUTTON.classList.remove("selected-color-button");
        DARK_YELLOW_BUTTON.classList.remove("selected-color-button");
        DARK_GREEN_BUTTON.classList.remove("selected-color-button");
        DARK_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        DARK_BLUE_BUTTON.classList.remove("selected-color-button");
        DARK_VIOLET_BUTTON.classList.remove("selected-color-button");
    }

    if (color == "bright-orange") {
        hex = "ffa347";


        BRIGHT_ORANGE_BUTTON.classList.add("selected-color-button");

        BRIGHT_RED_BUTTON.classList.remove("selected-color-button");
        BRIGHT_YELLOW_BUTTON.classList.remove("selected-color-button");
        BRIGHT_GREEN_BUTTON.classList.remove("selected-color-button");
        BRIGHT_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_BLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_VIOLET_BUTTON.classList.remove("selected-color-button");
        RED_BUTTON.classList.remove("selected-color-button");
        ORANGE_BUTTON.classList.remove("selected-color-button");
        YELLOW_BUTTON.classList.remove("selected-color-button");
        GREEN_BUTTON.classList.remove("selected-color-button");
        LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BLUE_BUTTON.classList.remove("selected-color-button");
        VIOLET_BUTTON.classList.remove("selected-color-button");
        DARK_RED_BUTTON.classList.remove("selected-color-button");
        DARK_ORANGE_BUTTON.classList.remove("selected-color-button");
        DARK_YELLOW_BUTTON.classList.remove("selected-color-button");
        DARK_GREEN_BUTTON.classList.remove("selected-color-button");
        DARK_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        DARK_BLUE_BUTTON.classList.remove("selected-color-button");
        DARK_VIOLET_BUTTON.classList.remove("selected-color-button");
    } else if (color == "orange") {
        hex = "ff7f00";


        ORANGE_BUTTON.classList.add("selected-color-button");

        BRIGHT_RED_BUTTON.classList.remove("selected-color-button");
        BRIGHT_ORANGE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_YELLOW_BUTTON.classList.remove("selected-color-button");
        BRIGHT_GREEN_BUTTON.classList.remove("selected-color-button");
        BRIGHT_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_BLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_VIOLET_BUTTON.classList.remove("selected-color-button");
        RED_BUTTON.classList.remove("selected-color-button");
        YELLOW_BUTTON.classList.remove("selected-color-button");
        GREEN_BUTTON.classList.remove("selected-color-button");
        LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BLUE_BUTTON.classList.remove("selected-color-button");
        VIOLET_BUTTON.classList.remove("selected-color-button");
        DARK_RED_BUTTON.classList.remove("selected-color-button");
        DARK_ORANGE_BUTTON.classList.remove("selected-color-button");
        DARK_YELLOW_BUTTON.classList.remove("selected-color-button");
        DARK_GREEN_BUTTON.classList.remove("selected-color-button");
        DARK_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        DARK_BLUE_BUTTON.classList.remove("selected-color-button");
        DARK_VIOLET_BUTTON.classList.remove("selected-color-button");
    } else if (color == "dark-orange") {
        hex = "994c00";


        DARK_ORANGE_BUTTON.classList.add("selected-color-button");

        BRIGHT_RED_BUTTON.classList.remove("selected-color-button");
        BRIGHT_ORANGE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_YELLOW_BUTTON.classList.remove("selected-color-button");
        BRIGHT_GREEN_BUTTON.classList.remove("selected-color-button");
        BRIGHT_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_BLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_VIOLET_BUTTON.classList.remove("selected-color-button");
        RED_BUTTON.classList.remove("selected-color-button");
        ORANGE_BUTTON.classList.remove("selected-color-button");
        YELLOW_BUTTON.classList.remove("selected-color-button");
        GREEN_BUTTON.classList.remove("selected-color-button");
        LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BLUE_BUTTON.classList.remove("selected-color-button");
        VIOLET_BUTTON.classList.remove("selected-color-button");
        DARK_RED_BUTTON.classList.remove("selected-color-button");
        DARK_YELLOW_BUTTON.classList.remove("selected-color-button");
        DARK_GREEN_BUTTON.classList.remove("selected-color-button");
        DARK_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        DARK_BLUE_BUTTON.classList.remove("selected-color-button");
        DARK_VIOLET_BUTTON.classList.remove("selected-color-button");
    }

    if (color == "bright-yellow") {
        hex = "ffff47";


        BRIGHT_YELLOW_BUTTON.classList.add("selected-color-button");

        BRIGHT_RED_BUTTON.classList.remove("selected-color-button");
        BRIGHT_ORANGE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_GREEN_BUTTON.classList.remove("selected-color-button");
        BRIGHT_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_BLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_VIOLET_BUTTON.classList.remove("selected-color-button");
        RED_BUTTON.classList.remove("selected-color-button");
        ORANGE_BUTTON.classList.remove("selected-color-button");
        YELLOW_BUTTON.classList.remove("selected-color-button");
        GREEN_BUTTON.classList.remove("selected-color-button");
        LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BLUE_BUTTON.classList.remove("selected-color-button");
        VIOLET_BUTTON.classList.remove("selected-color-button");
        DARK_RED_BUTTON.classList.remove("selected-color-button");
        DARK_ORANGE_BUTTON.classList.remove("selected-color-button");
        DARK_YELLOW_BUTTON.classList.remove("selected-color-button");
        DARK_GREEN_BUTTON.classList.remove("selected-color-button");
        DARK_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        DARK_BLUE_BUTTON.classList.remove("selected-color-button");
        DARK_VIOLET_BUTTON.classList.remove("selected-color-button");
    } else if (color == "yellow") {
        hex = "ffff00";


        YELLOW_BUTTON.classList.add("selected-color-button");

        BRIGHT_RED_BUTTON.classList.remove("selected-color-button");
        BRIGHT_ORANGE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_YELLOW_BUTTON.classList.remove("selected-color-button");
        BRIGHT_GREEN_BUTTON.classList.remove("selected-color-button");
        BRIGHT_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_BLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_VIOLET_BUTTON.classList.remove("selected-color-button");
        RED_BUTTON.classList.remove("selected-color-button");
        ORANGE_BUTTON.classList.remove("selected-color-button");
        GREEN_BUTTON.classList.remove("selected-color-button");
        LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BLUE_BUTTON.classList.remove("selected-color-button");
        VIOLET_BUTTON.classList.remove("selected-color-button");
        DARK_RED_BUTTON.classList.remove("selected-color-button");
        DARK_ORANGE_BUTTON.classList.remove("selected-color-button");
        DARK_YELLOW_BUTTON.classList.remove("selected-color-button");
        DARK_GREEN_BUTTON.classList.remove("selected-color-button");
        DARK_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        DARK_BLUE_BUTTON.classList.remove("selected-color-button");
        DARK_VIOLET_BUTTON.classList.remove("selected-color-button");
    } else if (color == "dark-yellow") {
        hex = "999900";


        DARK_YELLOW_BUTTON.classList.add("selected-color-button");

        BRIGHT_RED_BUTTON.classList.remove("selected-color-button");
        BRIGHT_ORANGE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_YELLOW_BUTTON.classList.remove("selected-color-button");
        BRIGHT_GREEN_BUTTON.classList.remove("selected-color-button");
        BRIGHT_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_BLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_VIOLET_BUTTON.classList.remove("selected-color-button");
        RED_BUTTON.classList.remove("selected-color-button");
        ORANGE_BUTTON.classList.remove("selected-color-button");
        YELLOW_BUTTON.classList.remove("selected-color-button");
        GREEN_BUTTON.classList.remove("selected-color-button");
        LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BLUE_BUTTON.classList.remove("selected-color-button");
        VIOLET_BUTTON.classList.remove("selected-color-button");
        DARK_RED_BUTTON.classList.remove("selected-color-button");
        DARK_ORANGE_BUTTON.classList.remove("selected-color-button");
        DARK_GREEN_BUTTON.classList.remove("selected-color-button");
        DARK_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        DARK_BLUE_BUTTON.classList.remove("selected-color-button");
        DARK_VIOLET_BUTTON.classList.remove("selected-color-button");
    }

    if (color == "bright-green") {
        hex = "47ff47";


        BRIGHT_GREEN_BUTTON.classList.add("selected-color-button");

        BRIGHT_RED_BUTTON.classList.remove("selected-color-button");
        BRIGHT_ORANGE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_YELLOW_BUTTON.classList.remove("selected-color-button");
        BRIGHT_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_BLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_VIOLET_BUTTON.classList.remove("selected-color-button");
        RED_BUTTON.classList.remove("selected-color-button");
        ORANGE_BUTTON.classList.remove("selected-color-button");
        YELLOW_BUTTON.classList.remove("selected-color-button");
        GREEN_BUTTON.classList.remove("selected-color-button");
        LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BLUE_BUTTON.classList.remove("selected-color-button");
        VIOLET_BUTTON.classList.remove("selected-color-button");
        DARK_RED_BUTTON.classList.remove("selected-color-button");
        DARK_ORANGE_BUTTON.classList.remove("selected-color-button");
        DARK_YELLOW_BUTTON.classList.remove("selected-color-button");
        DARK_GREEN_BUTTON.classList.remove("selected-color-button");
        DARK_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        DARK_BLUE_BUTTON.classList.remove("selected-color-button");
        DARK_VIOLET_BUTTON.classList.remove("selected-color-button");
    } else if (color == "green") {
        hex = "00ff00";


        GREEN_BUTTON.classList.add("selected-color-button");

        BRIGHT_RED_BUTTON.classList.remove("selected-color-button");
        BRIGHT_ORANGE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_YELLOW_BUTTON.classList.remove("selected-color-button");
        BRIGHT_GREEN_BUTTON.classList.remove("selected-color-button");
        BRIGHT_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_BLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_VIOLET_BUTTON.classList.remove("selected-color-button");
        RED_BUTTON.classList.remove("selected-color-button");
        ORANGE_BUTTON.classList.remove("selected-color-button");
        YELLOW_BUTTON.classList.remove("selected-color-button");
        LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BLUE_BUTTON.classList.remove("selected-color-button");
        VIOLET_BUTTON.classList.remove("selected-color-button");
        DARK_RED_BUTTON.classList.remove("selected-color-button");
        DARK_ORANGE_BUTTON.classList.remove("selected-color-button");
        DARK_YELLOW_BUTTON.classList.remove("selected-color-button");
        DARK_GREEN_BUTTON.classList.remove("selected-color-button");
        DARK_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        DARK_BLUE_BUTTON.classList.remove("selected-color-button");
        DARK_VIOLET_BUTTON.classList.remove("selected-color-button");
    } else if (color == "dark-green") {
        hex = "009900";


        DARK_GREEN_BUTTON.classList.add("selected-color-button");

        BRIGHT_RED_BUTTON.classList.remove("selected-color-button");
        BRIGHT_ORANGE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_YELLOW_BUTTON.classList.remove("selected-color-button");
        BRIGHT_GREEN_BUTTON.classList.remove("selected-color-button");
        BRIGHT_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_BLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_VIOLET_BUTTON.classList.remove("selected-color-button");
        RED_BUTTON.classList.remove("selected-color-button");
        ORANGE_BUTTON.classList.remove("selected-color-button");
        YELLOW_BUTTON.classList.remove("selected-color-button");
        GREEN_BUTTON.classList.remove("selected-color-button");
        LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BLUE_BUTTON.classList.remove("selected-color-button");
        VIOLET_BUTTON.classList.remove("selected-color-button");
        DARK_RED_BUTTON.classList.remove("selected-color-button");
        DARK_ORANGE_BUTTON.classList.remove("selected-color-button");
        DARK_YELLOW_BUTTON.classList.remove("selected-color-button");
        DARK_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        DARK_BLUE_BUTTON.classList.remove("selected-color-button");
        DARK_VIOLET_BUTTON.classList.remove("selected-color-button");
    }

    if (color == "bright-lightblue") {
        hex = "47ffff";


        BRIGHT_LIGHTBLUE_BUTTON.classList.add("selected-color-button");

        BRIGHT_RED_BUTTON.classList.remove("selected-color-button");
        BRIGHT_ORANGE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_YELLOW_BUTTON.classList.remove("selected-color-button");
        BRIGHT_GREEN_BUTTON.classList.remove("selected-color-button");
        BRIGHT_BLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_VIOLET_BUTTON.classList.remove("selected-color-button");
        RED_BUTTON.classList.remove("selected-color-button");
        ORANGE_BUTTON.classList.remove("selected-color-button");
        YELLOW_BUTTON.classList.remove("selected-color-button");
        GREEN_BUTTON.classList.remove("selected-color-button");
        LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BLUE_BUTTON.classList.remove("selected-color-button");
        VIOLET_BUTTON.classList.remove("selected-color-button");
        DARK_RED_BUTTON.classList.remove("selected-color-button");
        DARK_ORANGE_BUTTON.classList.remove("selected-color-button");
        DARK_YELLOW_BUTTON.classList.remove("selected-color-button");
        DARK_GREEN_BUTTON.classList.remove("selected-color-button");
        DARK_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        DARK_BLUE_BUTTON.classList.remove("selected-color-button");
        DARK_VIOLET_BUTTON.classList.remove("selected-color-button");
    } else if (color == "lightblue") {
        hex = "00ffff";


        LIGHTBLUE_BUTTON.classList.add("selected-color-button");

        BRIGHT_RED_BUTTON.classList.remove("selected-color-button");
        BRIGHT_ORANGE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_YELLOW_BUTTON.classList.remove("selected-color-button");
        BRIGHT_GREEN_BUTTON.classList.remove("selected-color-button");
        BRIGHT_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_BLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_VIOLET_BUTTON.classList.remove("selected-color-button");
        RED_BUTTON.classList.remove("selected-color-button");
        ORANGE_BUTTON.classList.remove("selected-color-button");
        YELLOW_BUTTON.classList.remove("selected-color-button");
        GREEN_BUTTON.classList.remove("selected-color-button");
        BLUE_BUTTON.classList.remove("selected-color-button");
        VIOLET_BUTTON.classList.remove("selected-color-button");
        DARK_RED_BUTTON.classList.remove("selected-color-button");
        DARK_ORANGE_BUTTON.classList.remove("selected-color-button");
        DARK_YELLOW_BUTTON.classList.remove("selected-color-button");
        DARK_GREEN_BUTTON.classList.remove("selected-color-button");
        DARK_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        DARK_BLUE_BUTTON.classList.remove("selected-color-button");
        DARK_VIOLET_BUTTON.classList.remove("selected-color-button");
    } else if (color == "dark-lightblue") {
        hex = "009999";


        DARK_LIGHTBLUE_BUTTON.classList.add("selected-color-button");

        BRIGHT_RED_BUTTON.classList.remove("selected-color-button");
        BRIGHT_ORANGE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_YELLOW_BUTTON.classList.remove("selected-color-button");
        BRIGHT_GREEN_BUTTON.classList.remove("selected-color-button");
        BRIGHT_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_BLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_VIOLET_BUTTON.classList.remove("selected-color-button");
        RED_BUTTON.classList.remove("selected-color-button");
        ORANGE_BUTTON.classList.remove("selected-color-button");
        YELLOW_BUTTON.classList.remove("selected-color-button");
        GREEN_BUTTON.classList.remove("selected-color-button");
        LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BLUE_BUTTON.classList.remove("selected-color-button");
        VIOLET_BUTTON.classList.remove("selected-color-button");
        DARK_RED_BUTTON.classList.remove("selected-color-button");
        DARK_ORANGE_BUTTON.classList.remove("selected-color-button");
        DARK_YELLOW_BUTTON.classList.remove("selected-color-button");
        DARK_GREEN_BUTTON.classList.remove("selected-color-button");
        DARK_BLUE_BUTTON.classList.remove("selected-color-button");
        DARK_VIOLET_BUTTON.classList.remove("selected-color-button");
    }

    if (color == "bright-blue") {
        hex = "4747ff";


        BRIGHT_BLUE_BUTTON.classList.add("selected-color-button");

        BRIGHT_RED_BUTTON.classList.remove("selected-color-button");
        BRIGHT_ORANGE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_YELLOW_BUTTON.classList.remove("selected-color-button");
        BRIGHT_GREEN_BUTTON.classList.remove("selected-color-button");
        BRIGHT_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_VIOLET_BUTTON.classList.remove("selected-color-button");
        RED_BUTTON.classList.remove("selected-color-button");
        ORANGE_BUTTON.classList.remove("selected-color-button");
        YELLOW_BUTTON.classList.remove("selected-color-button");
        GREEN_BUTTON.classList.remove("selected-color-button");
        LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BLUE_BUTTON.classList.remove("selected-color-button");
        VIOLET_BUTTON.classList.remove("selected-color-button");
        DARK_RED_BUTTON.classList.remove("selected-color-button");
        DARK_ORANGE_BUTTON.classList.remove("selected-color-button");
        DARK_YELLOW_BUTTON.classList.remove("selected-color-button");
        DARK_GREEN_BUTTON.classList.remove("selected-color-button");
        DARK_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        DARK_BLUE_BUTTON.classList.remove("selected-color-button");
        DARK_VIOLET_BUTTON.classList.remove("selected-color-button");
    } else if (color == "blue") {
        hex = "0000ff";


        BLUE_BUTTON.classList.add("selected-color-button");

        BRIGHT_RED_BUTTON.classList.remove("selected-color-button");
        BRIGHT_ORANGE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_YELLOW_BUTTON.classList.remove("selected-color-button");
        BRIGHT_GREEN_BUTTON.classList.remove("selected-color-button");
        BRIGHT_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_BLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_VIOLET_BUTTON.classList.remove("selected-color-button");
        RED_BUTTON.classList.remove("selected-color-button");
        ORANGE_BUTTON.classList.remove("selected-color-button");
        YELLOW_BUTTON.classList.remove("selected-color-button");
        GREEN_BUTTON.classList.remove("selected-color-button");
        LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        VIOLET_BUTTON.classList.remove("selected-color-button");
        DARK_RED_BUTTON.classList.remove("selected-color-button");
        DARK_ORANGE_BUTTON.classList.remove("selected-color-button");
        DARK_YELLOW_BUTTON.classList.remove("selected-color-button");
        DARK_GREEN_BUTTON.classList.remove("selected-color-button");
        DARK_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        DARK_BLUE_BUTTON.classList.remove("selected-color-button");
        DARK_VIOLET_BUTTON.classList.remove("selected-color-button");
    } else if (color == "dark-blue") {
        hex = "000099";


        DARK_BLUE_BUTTON.classList.add("selected-color-button");

        BRIGHT_RED_BUTTON.classList.remove("selected-color-button");
        BRIGHT_ORANGE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_YELLOW_BUTTON.classList.remove("selected-color-button");
        BRIGHT_GREEN_BUTTON.classList.remove("selected-color-button");
        BRIGHT_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_BLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_VIOLET_BUTTON.classList.remove("selected-color-button");
        RED_BUTTON.classList.remove("selected-color-button");
        ORANGE_BUTTON.classList.remove("selected-color-button");
        YELLOW_BUTTON.classList.remove("selected-color-button");
        GREEN_BUTTON.classList.remove("selected-color-button");
        LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BLUE_BUTTON.classList.remove("selected-color-button");
        VIOLET_BUTTON.classList.remove("selected-color-button");
        DARK_RED_BUTTON.classList.remove("selected-color-button");
        DARK_ORANGE_BUTTON.classList.remove("selected-color-button");
        DARK_YELLOW_BUTTON.classList.remove("selected-color-button");
        DARK_GREEN_BUTTON.classList.remove("selected-color-button");
        DARK_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        DARK_VIOLET_BUTTON.classList.remove("selected-color-button");
    }

    if (color == "bright-violet") {
        hex = "a347ff";


        BRIGHT_VIOLET_BUTTON.classList.add("selected-color-button");

        BRIGHT_RED_BUTTON.classList.remove("selected-color-button");
        BRIGHT_ORANGE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_YELLOW_BUTTON.classList.remove("selected-color-button");
        BRIGHT_GREEN_BUTTON.classList.remove("selected-color-button");
        BRIGHT_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_BLUE_BUTTON.classList.remove("selected-color-button");
        RED_BUTTON.classList.remove("selected-color-button");
        ORANGE_BUTTON.classList.remove("selected-color-button");
        YELLOW_BUTTON.classList.remove("selected-color-button");
        GREEN_BUTTON.classList.remove("selected-color-button");
        LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BLUE_BUTTON.classList.remove("selected-color-button");
        VIOLET_BUTTON.classList.remove("selected-color-button");
        DARK_RED_BUTTON.classList.remove("selected-color-button");
        DARK_ORANGE_BUTTON.classList.remove("selected-color-button");
        DARK_YELLOW_BUTTON.classList.remove("selected-color-button");
        DARK_GREEN_BUTTON.classList.remove("selected-color-button");
        DARK_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        DARK_BLUE_BUTTON.classList.remove("selected-color-button");
        DARK_VIOLET_BUTTON.classList.remove("selected-color-button");
    } else if (color == "violet") {
        hex = "7f00ff";


        VIOLET_BUTTON.classList.add("selected-color-button");

        BRIGHT_RED_BUTTON.classList.remove("selected-color-button");
        BRIGHT_ORANGE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_YELLOW_BUTTON.classList.remove("selected-color-button");
        BRIGHT_GREEN_BUTTON.classList.remove("selected-color-button");
        BRIGHT_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_BLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_VIOLET_BUTTON.classList.remove("selected-color-button");
        RED_BUTTON.classList.remove("selected-color-button");
        ORANGE_BUTTON.classList.remove("selected-color-button");
        YELLOW_BUTTON.classList.remove("selected-color-button");
        GREEN_BUTTON.classList.remove("selected-color-button");
        LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BLUE_BUTTON.classList.remove("selected-color-button");
        DARK_RED_BUTTON.classList.remove("selected-color-button");
        DARK_ORANGE_BUTTON.classList.remove("selected-color-button");
        DARK_YELLOW_BUTTON.classList.remove("selected-color-button");
        DARK_GREEN_BUTTON.classList.remove("selected-color-button");
        DARK_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        DARK_BLUE_BUTTON.classList.remove("selected-color-button");
        DARK_VIOLET_BUTTON.classList.remove("selected-color-button");
    } else if (color == "dark-violet") {
        hex = "4c0099";


        DARK_VIOLET_BUTTON.classList.add("selected-color-button");

        BRIGHT_RED_BUTTON.classList.remove("selected-color-button");
        BRIGHT_ORANGE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_YELLOW_BUTTON.classList.remove("selected-color-button");
        BRIGHT_GREEN_BUTTON.classList.remove("selected-color-button");
        BRIGHT_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_BLUE_BUTTON.classList.remove("selected-color-button");
        BRIGHT_VIOLET_BUTTON.classList.remove("selected-color-button");
        RED_BUTTON.classList.remove("selected-color-button");
        ORANGE_BUTTON.classList.remove("selected-color-button");
        YELLOW_BUTTON.classList.remove("selected-color-button");
        GREEN_BUTTON.classList.remove("selected-color-button");
        LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        BLUE_BUTTON.classList.remove("selected-color-button");
        VIOLET_BUTTON.classList.remove("selected-color-button");
        DARK_RED_BUTTON.classList.remove("selected-color-button");
        DARK_ORANGE_BUTTON.classList.remove("selected-color-button");
        DARK_YELLOW_BUTTON.classList.remove("selected-color-button");
        DARK_GREEN_BUTTON.classList.remove("selected-color-button");
        DARK_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        DARK_BLUE_BUTTON.classList.remove("selected-color-button");
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
