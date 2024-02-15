// Check if username is already taken  
document.addEventListener("DOMContentLoaded", function () {
    let usernameInput = document.getElementById("id_username");
  
    usernameInput.addEventListener("keyup", function () {
      let username = this.value;
  
      fetch("/check_username/?username=" + username)
        .then((response) => response.json())
        .then((data) => {
          if (data.is_taken) {
            usernameInput.setCustomValidity(
              "This username is already taken."
            );
          } else {
            usernameInput.setCustomValidity("");
          }
        })
        .catch(() => {});
    });
  });
  

// Show/hide password (registration form)
  function togglePassword() {
    let passwordInput = document.getElementById("password");
    let toggleButton = document.getElementById("togglePasswordButton");
    if (passwordInput.type === "password") {
      passwordInput.type = "text";
      toggleButton.textContent = "Hide Password";
    } else {
      passwordInput.type = "password";
      toggleButton.textContent = "Show Password";
    }
}

// My Trees viewing back-to-top button
document.addEventListener("DOMContentLoaded", function () {
    // Select the scrollable content
    let overlayContainer = document.querySelector('.scrollable-content');

    // Add event listener to the scrollable content
    if (overlayContainer) {
        overlayContainer.addEventListener("scroll", function () {
            // Check if the scrollable content has been scrolled down by 20px
            if (overlayContainer.scrollTop > 50) {
                document.getElementById("myBtn").style.display = "block";
            } else {
                document.getElementById("myBtn").style.display = "none";
            }
        });
    }
});

// Function to scroll back to top inside the scrollable content
function topFunction() {
    let overlayContainer = document.querySelector('.scrollable-content');
    if (overlayContainer) {
        overlayContainer.scrollTop = 0;
    }
}




// Define topFunction globally if it's used in HTML
function topFunction() {
    let overlayContainer = document.querySelector('.scrollable-content');
    overlayContainer.scrollTop = 0;
}
  

// Password conformation and view/hide password (tree_detail.html)
function toggleTreePassword() {
        let passwordInput = document.getElementById("tree-confirm-password");
        let toggleButton = document.getElementById("toggleTreePasswordButton");
        if (passwordInput.type === "password") {
            passwordInput.type = "text";
            toggleButton.textContent = "Hide Password";
        } else {
            passwordInput.type = "password";
            toggleButton.textContent = "Show Password";
        }
    }
