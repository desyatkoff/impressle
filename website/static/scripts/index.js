// I'm very sorry for this shit, I don't know javascript ._.


function view_picture(picture_uid) {
    // A function that gives a new +1 view for the picture without opening full view


    const VIEWS_COUNT = document.getElementById(`views-count-${picture_uid}`);


    fetch(`/view-picture/${picture_uid}`, {method: "POST"})
        .then((res) => res.json())
        .then((data) => {
            VIEWS_COUNT.innerHTML = data["views"];
        })
}


function full_view_picture(picture_uid) {
    // A function that redirects to picture's full view


    window.location.replace(`/picture/${picture_uid}`)
}


function like(picture_uid) {
    // A function that gives a new +1 like for the picture
    

    const LIKE_COUNT = document.getElementById(`likes-count-${picture_uid}`);
    const LIKE_BUTTON = document.getElementById(`like-button-${picture_uid}`);
    const DISLIKE_COUNT = document.getElementById(`dislikes-count-${picture_uid}`);
    const DISLIKE_BUTTON = document.getElementById(`dislike-button-${picture_uid}`);


    fetch(`/like-picture/${picture_uid}`, {method: "POST"})
        .then((res) => res.json())
        .then((data) => {
            LIKE_COUNT.innerHTML = data["likes"];
            DISLIKE_COUNT.innerHTML = data["dislikes"];


            if (data["liked"] === true) {
                LIKE_BUTTON.classList.add("liked");
                LIKE_BUTTON.classList.remove("not-liked");
                DISLIKE_BUTTON.classList.add("not-disliked");
                DISLIKE_BUTTON.classList.remove("disliked");
            } else {
                LIKE_BUTTON.classList.add("not-liked");
                LIKE_BUTTON.classList.remove("liked");
            }
        })
}


function dislike(picture_uid) {
    // A function that gives a new +1 dislike for the picture


    const LIKE_COUNT = document.getElementById(`likes-count-${picture_uid}`);
    const LIKE_BUTTON = document.getElementById(`like-button-${picture_uid}`);
    const DISLIKE_COUNT = document.getElementById(`dislikes-count-${picture_uid}`);
    const DISLIKE_BUTTON = document.getElementById(`dislike-button-${picture_uid}`);


    fetch(`/dislike-picture/${picture_uid}`, {method: "POST"})
        .then((res) => res.json())
        .then((data) => {
            LIKE_COUNT.innerHTML = data["likes"];
            DISLIKE_COUNT.innerHTML = data["dislikes"];


            if (data["disliked"] === true) {
                LIKE_BUTTON.classList.add("not-liked");
                LIKE_BUTTON.classList.remove("liked");
                DISLIKE_BUTTON.classList.add("disliked");
                DISLIKE_BUTTON.classList.remove("not-disliked");
            } else {
                DISLIKE_BUTTON.classList.add("not-disliked");
                DISLIKE_BUTTON.classList.remove("disliked");
            }
        })
}


function comment(picture_uid) {
    // A function that redirects to picture's full view and automatically focuses on comment input


    window.location.replace(`/picture/${picture_uid}#comment-text`)
}


function download_picture(picture_uid) {
    // A function for downloading a picture as .png by it's UID


    window.location.replace(`/download-picture/${picture_uid}`);
    
}


function follow(user_uid) {
    // A function that gives a new +1 follower for the user
    

    const FOLLOWERS_COUNT = document.getElementById(`followers-count-${user_uid}`);
    const FOLLOW_BUTTON = document.getElementById(`follow-button-${user_uid}`);


    fetch(`/follow-user/${user_uid}`, {method: "POST"})
        .then((res) => res.json())
        .then((data) => {
            FOLLOWERS_COUNT.innerHTML = data["followers"];


            if (data["followed"] === true) {
                FOLLOW_BUTTON.classList.add("following");
                FOLLOW_BUTTON.classList.remove("not-following");
                FOLLOW_BUTTON.textContent = "Unfollow";
            } else {
                FOLLOW_BUTTON.classList.add("not-following");
                FOLLOW_BUTTON.classList.remove("following");
                FOLLOW_BUTTON.textContent = "Follow";
            }
        })
}


window.onclick = function(event) {
    let alert_card = document.getElementById("alert");
    let alert_close_button = document.getElementById("alert-close");


    if (event.target == alert_close_button) {
        alert_card.style.display = "none";
    }
} 

