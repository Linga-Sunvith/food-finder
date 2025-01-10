document.getElementById("search-button").addEventListener("click", function() {
    let query = document.getElementById("search-bar").value;
    if(query) {
        window.location.href = `/search?query=${query}`;
    }
});


