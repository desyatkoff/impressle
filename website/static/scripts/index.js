function like(post_id) {
    const LIKE_COUNT = document.getElementById(`likes_count_${post_id}`);
    const LIKE_BUTTON = document.getElementById(`like_button_${post_id}`);


    fetch(`/like-post/${post_id}`, {method: "POST"})
        .then((res) => res.json())
        .then((data) => {
            LIKE_COUNT.innerHTML = data["likes"];


            if (data["liked"] === true) {
                LIKE_BUTTON.className = "liked";
            } else {
                LIKE_BUTTON.className = "not_liked";
            }
        })
}
