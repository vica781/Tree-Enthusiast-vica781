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
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  // Check the scroll position of the overlay container
  let overlayContainer = document.querySelector('.scrollable-content');
  if (overlayContainer.scrollTop > 5 || document.documentElement.scrollTop > 5) {
    document.getElementById("myBtn").style.display = "block";
  } else {
    document.getElementById("myBtn").style.display = "none";
  }
}

function topFunction() {
  // Scroll to the top of the overlay container
  let overlayContainer = document.querySelector('.scrollable-content');
  overlayContainer.scrollTop = 0;
}  