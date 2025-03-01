// I'm very sorry for this shit, I don't know javascript ._.


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
    const PASTEL_RED_BUTTON = document.getElementById("pastel-red-button");
    const PASTEL_ORANGE_BUTTON = document.getElementById("pastel-orange-button");
    const PASTEL_YELLOW_BUTTON = document.getElementById("pastel-yellow-button");
    const PASTEL_GREEN_BUTTON = document.getElementById("pastel-green-button");
    const PASTEL_LIGHTBLUE_BUTTON = document.getElementById("pastel-lightblue-button");
    const PASTEL_BLUE_BUTTON = document.getElementById("pastel-blue-button");
    const PASTEL_VIOLET_BUTTON = document.getElementById("pastel-violet-button");
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
    const LIGHT1_BUTTON = document.getElementById("light1-button");
    const LIGHT2_BUTTON = document.getElementById("light2-button");
    const LIGHT3_BUTTON = document.getElementById("light3-button");
    const DARK1_BUTTON = document.getElementById ("dark1-button");
    const DARK2_BUTTON = document.getElementById("dark2-button");
    const DARK3_BUTTON = document.getElementById("dark3-button");

    let hex;

    if (color == "pastel-red") {
        hex = "ff4747";


        PASTEL_RED_BUTTON.classList.add("selected-color-button");

        PASTEL_ORANGE_BUTTON.classList.remove("selected-color-button");
        PASTEL_YELLOW_BUTTON.classList.remove("selected-color-button");
        PASTEL_GREEN_BUTTON.classList.remove("selected-color-button");
        PASTEL_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_BLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_VIOLET_BUTTON.classList.remove("selected-color-button");
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
        LIGHT1_BUTTON.classList.remove("selected-color-button");
        LIGHT2_BUTTON.classList.remove("selected-color-button");
        LIGHT3_BUTTON.classList.remove("selected-color-button");
        DARK1_BUTTON.classList.remove("selected-color-button");
        DARK2_BUTTON.classList.remove("selected-color-button");
        DARK3_BUTTON.classList.remove("selected-color-button");
    } else if (color == "red") {
        hex = "ff0000";

        RED_BUTTON.classList.add("selected-color-button");

        PASTEL_RED_BUTTON.classList.remove("selected-color-button");
        PASTEL_ORANGE_BUTTON.classList.remove("selected-color-button");
        PASTEL_YELLOW_BUTTON.classList.remove("selected-color-button");
        PASTEL_GREEN_BUTTON.classList.remove("selected-color-button");
        PASTEL_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_BLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_VIOLET_BUTTON.classList.remove("selected-color-button");
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
        LIGHT1_BUTTON.classList.remove("selected-color-button");
        LIGHT2_BUTTON.classList.remove("selected-color-button");
        LIGHT3_BUTTON.classList.remove("selected-color-button");
        DARK1_BUTTON.classList.remove("selected-color-button");
        DARK2_BUTTON.classList.remove("selected-color-button");
        DARK3_BUTTON.classList.remove("selected-color-button");
    } else if (color == "dark-red") {
        hex = "990000";

        DARK_RED_BUTTON.classList.add("selected-color-button");

        PASTEL_RED_BUTTON.classList.remove("selected-color-button");
        PASTEL_ORANGE_BUTTON.classList.remove("selected-color-button");
        PASTEL_YELLOW_BUTTON.classList.remove("selected-color-button");
        PASTEL_GREEN_BUTTON.classList.remove("selected-color-button");
        PASTEL_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_BLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_VIOLET_BUTTON.classList.remove("selected-color-button");
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
        LIGHT1_BUTTON.classList.remove("selected-color-button");
        LIGHT2_BUTTON.classList.remove("selected-color-button");
        LIGHT3_BUTTON.classList.remove("selected-color-button");
        DARK1_BUTTON.classList.remove("selected-color-button");
        DARK2_BUTTON.classList.remove("selected-color-button");
        DARK3_BUTTON.classList.remove("selected-color-button");
    }

    if (color == "pastel-orange") {
        hex = "ffa347";


        PASTEL_ORANGE_BUTTON.classList.add("selected-color-button");

        PASTEL_RED_BUTTON.classList.remove("selected-color-button");
        PASTEL_YELLOW_BUTTON.classList.remove("selected-color-button");
        PASTEL_GREEN_BUTTON.classList.remove("selected-color-button");
        PASTEL_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_BLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_VIOLET_BUTTON.classList.remove("selected-color-button");
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
        LIGHT1_BUTTON.classList.remove("selected-color-button");
        LIGHT2_BUTTON.classList.remove("selected-color-button");
        LIGHT3_BUTTON.classList.remove("selected-color-button");
        DARK1_BUTTON.classList.remove("selected-color-button");
        DARK2_BUTTON.classList.remove("selected-color-button");
        DARK3_BUTTON.classList.remove("selected-color-button");
    } else if (color == "orange") {
        hex = "ff7f00";


        ORANGE_BUTTON.classList.add("selected-color-button");

        PASTEL_RED_BUTTON.classList.remove("selected-color-button");
        PASTEL_ORANGE_BUTTON.classList.remove("selected-color-button");
        PASTEL_YELLOW_BUTTON.classList.remove("selected-color-button");
        PASTEL_GREEN_BUTTON.classList.remove("selected-color-button");
        PASTEL_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_BLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_VIOLET_BUTTON.classList.remove("selected-color-button");
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
        LIGHT1_BUTTON.classList.remove("selected-color-button");
        LIGHT2_BUTTON.classList.remove("selected-color-button");
        LIGHT3_BUTTON.classList.remove("selected-color-button");
        DARK1_BUTTON.classList.remove("selected-color-button");
        DARK2_BUTTON.classList.remove("selected-color-button");
        DARK3_BUTTON.classList.remove("selected-color-button");
    } else if (color == "dark-orange") {
        hex = "994c00";


        DARK_ORANGE_BUTTON.classList.add("selected-color-button");

        PASTEL_RED_BUTTON.classList.remove("selected-color-button");
        PASTEL_ORANGE_BUTTON.classList.remove("selected-color-button");
        PASTEL_YELLOW_BUTTON.classList.remove("selected-color-button");
        PASTEL_GREEN_BUTTON.classList.remove("selected-color-button");
        PASTEL_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_BLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_VIOLET_BUTTON.classList.remove("selected-color-button");
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
        LIGHT1_BUTTON.classList.remove("selected-color-button");
        LIGHT2_BUTTON.classList.remove("selected-color-button");
        LIGHT3_BUTTON.classList.remove("selected-color-button");
        DARK1_BUTTON.classList.remove("selected-color-button");
        DARK2_BUTTON.classList.remove("selected-color-button");
        DARK3_BUTTON.classList.remove("selected-color-button");
    }

    if (color == "pastel-yellow") {
        hex = "ffff47";


        PASTEL_YELLOW_BUTTON.classList.add("selected-color-button");

        PASTEL_RED_BUTTON.classList.remove("selected-color-button");
        PASTEL_ORANGE_BUTTON.classList.remove("selected-color-button");
        PASTEL_GREEN_BUTTON.classList.remove("selected-color-button");
        PASTEL_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_BLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_VIOLET_BUTTON.classList.remove("selected-color-button");
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
        LIGHT1_BUTTON.classList.remove("selected-color-button");
        LIGHT2_BUTTON.classList.remove("selected-color-button");
        LIGHT3_BUTTON.classList.remove("selected-color-button");
        DARK1_BUTTON.classList.remove("selected-color-button");
        DARK2_BUTTON.classList.remove("selected-color-button");
        DARK3_BUTTON.classList.remove("selected-color-button");
    } else if (color == "yellow") {
        hex = "ffff00";


        YELLOW_BUTTON.classList.add("selected-color-button");

        PASTEL_RED_BUTTON.classList.remove("selected-color-button");
        PASTEL_ORANGE_BUTTON.classList.remove("selected-color-button");
        PASTEL_YELLOW_BUTTON.classList.remove("selected-color-button");
        PASTEL_GREEN_BUTTON.classList.remove("selected-color-button");
        PASTEL_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_BLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_VIOLET_BUTTON.classList.remove("selected-color-button");
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
        LIGHT1_BUTTON.classList.remove("selected-color-button");
        LIGHT2_BUTTON.classList.remove("selected-color-button");
        LIGHT3_BUTTON.classList.remove("selected-color-button");
        DARK1_BUTTON.classList.remove("selected-color-button");
        DARK2_BUTTON.classList.remove("selected-color-button");
        DARK3_BUTTON.classList.remove("selected-color-button");
    } else if (color == "dark-yellow") {
        hex = "999900";


        DARK_YELLOW_BUTTON.classList.add("selected-color-button");

        PASTEL_RED_BUTTON.classList.remove("selected-color-button");
        PASTEL_ORANGE_BUTTON.classList.remove("selected-color-button");
        PASTEL_YELLOW_BUTTON.classList.remove("selected-color-button");
        PASTEL_GREEN_BUTTON.classList.remove("selected-color-button");
        PASTEL_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_BLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_VIOLET_BUTTON.classList.remove("selected-color-button");
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
        LIGHT1_BUTTON.classList.remove("selected-color-button");
        LIGHT2_BUTTON.classList.remove("selected-color-button");
        LIGHT3_BUTTON.classList.remove("selected-color-button");
        DARK1_BUTTON.classList.remove("selected-color-button");
        DARK2_BUTTON.classList.remove("selected-color-button");
        DARK3_BUTTON.classList.remove("selected-color-button");
    }

    if (color == "pastel-green") {
        hex = "47ff47";


        PASTEL_GREEN_BUTTON.classList.add("selected-color-button");

        PASTEL_RED_BUTTON.classList.remove("selected-color-button");
        PASTEL_ORANGE_BUTTON.classList.remove("selected-color-button");
        PASTEL_YELLOW_BUTTON.classList.remove("selected-color-button");
        PASTEL_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_BLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_VIOLET_BUTTON.classList.remove("selected-color-button");
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
        LIGHT1_BUTTON.classList.remove("selected-color-button");
        LIGHT2_BUTTON.classList.remove("selected-color-button");
        LIGHT3_BUTTON.classList.remove("selected-color-button");
        DARK1_BUTTON.classList.remove("selected-color-button");
        DARK2_BUTTON.classList.remove("selected-color-button");
        DARK3_BUTTON.classList.remove("selected-color-button");
    } else if (color == "green") {
        hex = "00ff00";


        GREEN_BUTTON.classList.add("selected-color-button");

        PASTEL_RED_BUTTON.classList.remove("selected-color-button");
        PASTEL_ORANGE_BUTTON.classList.remove("selected-color-button");
        PASTEL_YELLOW_BUTTON.classList.remove("selected-color-button");
        PASTEL_GREEN_BUTTON.classList.remove("selected-color-button");
        PASTEL_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_BLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_VIOLET_BUTTON.classList.remove("selected-color-button");
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
        LIGHT1_BUTTON.classList.remove("selected-color-button");
        LIGHT2_BUTTON.classList.remove("selected-color-button");
        LIGHT3_BUTTON.classList.remove("selected-color-button");
        DARK1_BUTTON.classList.remove("selected-color-button");
        DARK2_BUTTON.classList.remove("selected-color-button");
        DARK3_BUTTON.classList.remove("selected-color-button");
    } else if (color == "dark-green") {
        hex = "009900";


        DARK_GREEN_BUTTON.classList.add("selected-color-button");

        PASTEL_RED_BUTTON.classList.remove("selected-color-button");
        PASTEL_ORANGE_BUTTON.classList.remove("selected-color-button");
        PASTEL_YELLOW_BUTTON.classList.remove("selected-color-button");
        PASTEL_GREEN_BUTTON.classList.remove("selected-color-button");
        PASTEL_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_BLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_VIOLET_BUTTON.classList.remove("selected-color-button");
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
        LIGHT1_BUTTON.classList.remove("selected-color-button");
        LIGHT2_BUTTON.classList.remove("selected-color-button");
        LIGHT3_BUTTON.classList.remove("selected-color-button");
        DARK1_BUTTON.classList.remove("selected-color-button");
        DARK2_BUTTON.classList.remove("selected-color-button");
        DARK3_BUTTON.classList.remove("selected-color-button");
    }

    if (color == "pastel-lightblue") {
        hex = "47ffff";


        PASTEL_LIGHTBLUE_BUTTON.classList.add("selected-color-button");

        PASTEL_RED_BUTTON.classList.remove("selected-color-button");
        PASTEL_ORANGE_BUTTON.classList.remove("selected-color-button");
        PASTEL_YELLOW_BUTTON.classList.remove("selected-color-button");
        PASTEL_GREEN_BUTTON.classList.remove("selected-color-button");
        PASTEL_BLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_VIOLET_BUTTON.classList.remove("selected-color-button");
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
        LIGHT1_BUTTON.classList.remove("selected-color-button");
        LIGHT2_BUTTON.classList.remove("selected-color-button");
        LIGHT3_BUTTON.classList.remove("selected-color-button");
        DARK1_BUTTON.classList.remove("selected-color-button");
        DARK2_BUTTON.classList.remove("selected-color-button");
        DARK3_BUTTON.classList.remove("selected-color-button");
    } else if (color == "lightblue") {
        hex = "00ffff";


        LIGHTBLUE_BUTTON.classList.add("selected-color-button");

        PASTEL_RED_BUTTON.classList.remove("selected-color-button");
        PASTEL_ORANGE_BUTTON.classList.remove("selected-color-button");
        PASTEL_YELLOW_BUTTON.classList.remove("selected-color-button");
        PASTEL_GREEN_BUTTON.classList.remove("selected-color-button");
        PASTEL_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_BLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_VIOLET_BUTTON.classList.remove("selected-color-button");
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
        LIGHT1_BUTTON.classList.remove("selected-color-button");
        LIGHT2_BUTTON.classList.remove("selected-color-button");
        LIGHT3_BUTTON.classList.remove("selected-color-button");
        DARK1_BUTTON.classList.remove("selected-color-button");
        DARK2_BUTTON.classList.remove("selected-color-button");
        DARK3_BUTTON.classList.remove("selected-color-button");
    } else if (color == "dark-lightblue") {
        hex = "009999";


        DARK_LIGHTBLUE_BUTTON.classList.add("selected-color-button");

        PASTEL_RED_BUTTON.classList.remove("selected-color-button");
        PASTEL_ORANGE_BUTTON.classList.remove("selected-color-button");
        PASTEL_YELLOW_BUTTON.classList.remove("selected-color-button");
        PASTEL_GREEN_BUTTON.classList.remove("selected-color-button");
        PASTEL_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_BLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_VIOLET_BUTTON.classList.remove("selected-color-button");
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
        LIGHT1_BUTTON.classList.remove("selected-color-button");
        LIGHT2_BUTTON.classList.remove("selected-color-button");
        LIGHT3_BUTTON.classList.remove("selected-color-button");
        DARK1_BUTTON.classList.remove("selected-color-button");
        DARK2_BUTTON.classList.remove("selected-color-button");
        DARK3_BUTTON.classList.remove("selected-color-button");
    }

    if (color == "pastel-blue") {
        hex = "4747ff";


        PASTEL_BLUE_BUTTON.classList.add("selected-color-button");

        PASTEL_RED_BUTTON.classList.remove("selected-color-button");
        PASTEL_ORANGE_BUTTON.classList.remove("selected-color-button");
        PASTEL_YELLOW_BUTTON.classList.remove("selected-color-button");
        PASTEL_GREEN_BUTTON.classList.remove("selected-color-button");
        PASTEL_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_VIOLET_BUTTON.classList.remove("selected-color-button");
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
        LIGHT1_BUTTON.classList.remove("selected-color-button");
        LIGHT2_BUTTON.classList.remove("selected-color-button");
        LIGHT3_BUTTON.classList.remove("selected-color-button");
        DARK1_BUTTON.classList.remove("selected-color-button");
        DARK2_BUTTON.classList.remove("selected-color-button");
        DARK3_BUTTON.classList.remove("selected-color-button");
    } else if (color == "blue") {
        hex = "0000ff";


        BLUE_BUTTON.classList.add("selected-color-button");

        PASTEL_RED_BUTTON.classList.remove("selected-color-button");
        PASTEL_ORANGE_BUTTON.classList.remove("selected-color-button");
        PASTEL_YELLOW_BUTTON.classList.remove("selected-color-button");
        PASTEL_GREEN_BUTTON.classList.remove("selected-color-button");
        PASTEL_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_BLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_VIOLET_BUTTON.classList.remove("selected-color-button");
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
        LIGHT1_BUTTON.classList.remove("selected-color-button");
        LIGHT2_BUTTON.classList.remove("selected-color-button");
        LIGHT3_BUTTON.classList.remove("selected-color-button");
        DARK1_BUTTON.classList.remove("selected-color-button");
        DARK2_BUTTON.classList.remove("selected-color-button");
        DARK3_BUTTON.classList.remove("selected-color-button");
    } else if (color == "dark-blue") {
        hex = "000099";


        DARK_BLUE_BUTTON.classList.add("selected-color-button");

        PASTEL_RED_BUTTON.classList.remove("selected-color-button");
        PASTEL_ORANGE_BUTTON.classList.remove("selected-color-button");
        PASTEL_YELLOW_BUTTON.classList.remove("selected-color-button");
        PASTEL_GREEN_BUTTON.classList.remove("selected-color-button");
        PASTEL_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_BLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_VIOLET_BUTTON.classList.remove("selected-color-button");
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
        LIGHT1_BUTTON.classList.remove("selected-color-button");
        LIGHT2_BUTTON.classList.remove("selected-color-button");
        LIGHT3_BUTTON.classList.remove("selected-color-button");
        DARK1_BUTTON.classList.remove("selected-color-button");
        DARK2_BUTTON.classList.remove("selected-color-button");
        DARK3_BUTTON.classList.remove("selected-color-button");
    }

    if (color == "pastel-violet") {
        hex = "a347ff";


        PASTEL_VIOLET_BUTTON.classList.add("selected-color-button");

        PASTEL_RED_BUTTON.classList.remove("selected-color-button");
        PASTEL_ORANGE_BUTTON.classList.remove("selected-color-button");
        PASTEL_YELLOW_BUTTON.classList.remove("selected-color-button");
        PASTEL_GREEN_BUTTON.classList.remove("selected-color-button");
        PASTEL_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_BLUE_BUTTON.classList.remove("selected-color-button");
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
        LIGHT1_BUTTON.classList.remove("selected-color-button");
        LIGHT2_BUTTON.classList.remove("selected-color-button");
        LIGHT3_BUTTON.classList.remove("selected-color-button");
        DARK1_BUTTON.classList.remove("selected-color-button");
        DARK2_BUTTON.classList.remove("selected-color-button");
        DARK3_BUTTON.classList.remove("selected-color-button");
    } else if (color == "violet") {
        hex = "7f00ff";


        VIOLET_BUTTON.classList.add("selected-color-button");

        PASTEL_RED_BUTTON.classList.remove("selected-color-button");
        PASTEL_ORANGE_BUTTON.classList.remove("selected-color-button");
        PASTEL_YELLOW_BUTTON.classList.remove("selected-color-button");
        PASTEL_GREEN_BUTTON.classList.remove("selected-color-button");
        PASTEL_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_BLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_VIOLET_BUTTON.classList.remove("selected-color-button");
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
        LIGHT1_BUTTON.classList.remove("selected-color-button");
        LIGHT2_BUTTON.classList.remove("selected-color-button");
        LIGHT3_BUTTON.classList.remove("selected-color-button");
        DARK1_BUTTON.classList.remove("selected-color-button");
        DARK2_BUTTON.classList.remove("selected-color-button");
        DARK3_BUTTON.classList.remove("selected-color-button");
    } else if (color == "dark-violet") {
        hex = "4c0099";


        DARK_VIOLET_BUTTON.classList.add("selected-color-button");

        PASTEL_RED_BUTTON.classList.remove("selected-color-button");
        PASTEL_ORANGE_BUTTON.classList.remove("selected-color-button");
        PASTEL_YELLOW_BUTTON.classList.remove("selected-color-button");
        PASTEL_GREEN_BUTTON.classList.remove("selected-color-button");
        PASTEL_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_BLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_VIOLET_BUTTON.classList.remove("selected-color-button");
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
        LIGHT1_BUTTON.classList.remove("selected-color-button");
        LIGHT2_BUTTON.classList.remove("selected-color-button");
        LIGHT3_BUTTON.classList.remove("selected-color-button");
        DARK1_BUTTON.classList.remove("selected-color-button");
        DARK2_BUTTON.classList.remove("selected-color-button");
        DARK3_BUTTON.classList.remove("selected-color-button");
    } else if (color == "light1") {
        hex = "e6e6e6";


        LIGHT1_BUTTON.classList.add("selected-color-button");

        PASTEL_RED_BUTTON.classList.remove("selected-color-button");
        PASTEL_ORANGE_BUTTON.classList.remove("selected-color-button");
        PASTEL_YELLOW_BUTTON.classList.remove("selected-color-button");
        PASTEL_GREEN_BUTTON.classList.remove("selected-color-button");
        PASTEL_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_BLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_VIOLET_BUTTON.classList.remove("selected-color-button");
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
        LIGHT2_BUTTON.classList.remove("selected-color-button");
        LIGHT3_BUTTON.classList.remove("selected-color-button");
        DARK1_BUTTON.classList.remove("selected-color-button");
        DARK2_BUTTON.classList.remove("selected-color-button");
        DARK3_BUTTON.classList.remove("selected-color-button");
    } else if (color == "light2") {
        hex = "d9d9d9";


        LIGHT2_BUTTON.classList.add("selected-color-button");

        PASTEL_RED_BUTTON.classList.remove("selected-color-button");
        PASTEL_ORANGE_BUTTON.classList.remove("selected-color-button");
        PASTEL_YELLOW_BUTTON.classList.remove("selected-color-button");
        PASTEL_GREEN_BUTTON.classList.remove("selected-color-button");
        PASTEL_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_BLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_VIOLET_BUTTON.classList.remove("selected-color-button");
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
        LIGHT1_BUTTON.classList.remove("selected-color-button");
        LIGHT3_BUTTON.classList.remove("selected-color-button");
        DARK1_BUTTON.classList.remove("selected-color-button");
        DARK2_BUTTON.classList.remove("selected-color-button");
        DARK3_BUTTON.classList.remove("selected-color-button");
    } else if (color == "light3") {
        hex = "cccccc";


        LIGHT3_BUTTON.classList.add("selected-color-button");

        PASTEL_RED_BUTTON.classList.remove("selected-color-button");
        PASTEL_ORANGE_BUTTON.classList.remove("selected-color-button");
        PASTEL_YELLOW_BUTTON.classList.remove("selected-color-button");
        PASTEL_GREEN_BUTTON.classList.remove("selected-color-button");
        PASTEL_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_BLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_VIOLET_BUTTON.classList.remove("selected-color-button");
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
        LIGHT1_BUTTON.classList.remove("selected-color-button");
        LIGHT2_BUTTON.classList.remove("selected-color-button");
        DARK1_BUTTON.classList.remove("selected-color-button");
        DARK2_BUTTON.classList.remove("selected-color-button");
        DARK3_BUTTON.classList.remove("selected-color-button");
    } else if (color == "dark1") {
        hex = "262626";


        DARK1_BUTTON.classList.add("selected-color-button");

        PASTEL_RED_BUTTON.classList.remove("selected-color-button");
        PASTEL_ORANGE_BUTTON.classList.remove("selected-color-button");
        PASTEL_YELLOW_BUTTON.classList.remove("selected-color-button");
        PASTEL_GREEN_BUTTON.classList.remove("selected-color-button");
        PASTEL_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_BLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_VIOLET_BUTTON.classList.remove("selected-color-button");
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
        LIGHT1_BUTTON.classList.remove("selected-color-button");
        LIGHT2_BUTTON.classList.remove("selected-color-button");
        LIGHT3_BUTTON.classList.remove("selected-color-button");
        DARK2_BUTTON.classList.remove("selected-color-button");
        DARK3_BUTTON.classList.remove("selected-color-button");
    } else if (color == "dark2") {
        hex = "1a1a1a";


        DARK2_BUTTON.classList.add("selected-color-button");

        PASTEL_RED_BUTTON.classList.remove("selected-color-button");
        PASTEL_ORANGE_BUTTON.classList.remove("selected-color-button");
        PASTEL_YELLOW_BUTTON.classList.remove("selected-color-button");
        PASTEL_GREEN_BUTTON.classList.remove("selected-color-button");
        PASTEL_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_BLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_VIOLET_BUTTON.classList.remove("selected-color-button");
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
        LIGHT1_BUTTON.classList.remove("selected-color-button");
        LIGHT2_BUTTON.classList.remove("selected-color-button");
        LIGHT3_BUTTON.classList.remove("selected-color-button");
        DARK1_BUTTON.classList.remove("selected-color-button");
        DARK3_BUTTON.classList.remove("selected-color-button");
    } else if (color == "dark3") {
        hex = "0d0d0d";


        DARK3_BUTTON.classList.add("selected-color-button");

        PASTEL_RED_BUTTON.classList.remove("selected-color-button");
        PASTEL_ORANGE_BUTTON.classList.remove("selected-color-button");
        PASTEL_YELLOW_BUTTON.classList.remove("selected-color-button");
        PASTEL_GREEN_BUTTON.classList.remove("selected-color-button");
        PASTEL_LIGHTBLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_BLUE_BUTTON.classList.remove("selected-color-button");
        PASTEL_VIOLET_BUTTON.classList.remove("selected-color-button");
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
        LIGHT1_BUTTON.classList.remove("selected-color-button");
        LIGHT2_BUTTON.classList.remove("selected-color-button");
        LIGHT3_BUTTON.classList.remove("selected-color-button");
        DARK1_BUTTON.classList.remove("selected-color-button");
        DARK2_BUTTON.classList.remove("selected-color-button");
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
