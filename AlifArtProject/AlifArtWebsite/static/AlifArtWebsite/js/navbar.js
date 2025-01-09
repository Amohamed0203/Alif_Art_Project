// navbar.js
document.addEventListener("DOMContentLoaded", function () {
    const navbarContainer = document.getElementById("navbar");

    // Load the navbar.html content
    fetch("navbar.html")
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.text();
        })
        .then(data => {
            navbarContainer.innerHTML = data;
        })
        .catch(error => {
            console.error("Error loading the navbar:", error);
        });
});
