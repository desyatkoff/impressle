function like(picture_uid) {
    const LIKE_COUNT = document.getElementById(`likes-count-${picture_uid}`);
    const LIKE_BUTTON = document.getElementById(`like-button-${picture_uid}`);


    fetch(`/like-picture/${picture_uid}`, {method: "POST"})
        .then((res) => res.json())
        .then((data) => {
            LIKE_COUNT.innerHTML = data["likes"];


            if (data["liked"] === true) {
                LIKE_BUTTON.className = "liked";
            } else {
                LIKE_BUTTON.className = "not-liked";
            }
        })
}
