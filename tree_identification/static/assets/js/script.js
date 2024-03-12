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


// Password confirmation and view/hide password (profile page)
function toggleProfilePassword() {
  let passwordInput = document.getElementById("profile-confirm-password");
  let toggleButton = document.getElementById("toggleProfilePasswordButton");
  if (passwordInput.type === "password") {
      passwordInput.type = "text";
      toggleButton.textContent = "Hide Password";
  } else {
      passwordInput.type = "password";
      toggleButton.textContent = "Show Password";
  }
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


function toggleLoginPassword() {
    let passwordInput = document.getElementById("login-password");
    let toggleButton = document.getElementById("toggleLoginPasswordButton");

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

// Profile Update Form Validation
document.addEventListener("DOMContentLoaded", function () {
    let emailInput = document.getElementById("emailField");
    let updateProfileForm = document.getElementById('updateProfileForm');

    emailInput.addEventListener("change", function () {
        checkEmailAvailability(this.value);
    });

    updateProfileForm.addEventListener('submit', function(event) {
        // Perform all form validations
        let valid = performValidations();

        // Check email availability asynchronously
        checkEmailAvailability(emailInput.value, function(isAvailable) {
            if (!isAvailable) {
                valid = false;
            }

            // If any validation fails, prevent form submission
            if (!valid) {
                event.preventDefault();
            }
        });
    });
});

function performValidations() {
    let emailField = document.getElementById('emailField');
    let currentPasswordField = document.getElementById('currentPasswordField');
    let newPasswordField = document.getElementById('newPasswordField');
    let confirmNewPasswordField = document.getElementById('confirmNewPasswordField');
    let valid = true;

    // Reset error messages
    document.getElementById('emailError').textContent = '';
    document.getElementById('currentPasswordError').textContent = '';
    document.getElementById('newPasswordError').textContent = '';

    // Email regex validation
    let emailRegex = /\S+@\S+\.\S+/;
    if (!emailRegex.test(emailField.value)) {
        document.getElementById('emailError').textContent = 'Please enter a valid email address.';
        valid = false;
    }

    // Current password length check
    if (currentPasswordField.value.length < 8) {
        document.getElementById('currentPasswordError').textContent = 'Your current password must be at least 8 characters.';
        valid = false;
    }

    // New password length check
    if (newPasswordField.value.length > 0 && newPasswordField.value.length < 8) {
        document.getElementById('newPasswordError').textContent = 'New password must be at least 8 characters.';
        valid = false;
    }

    // Password match check
    if (newPasswordField.value !== confirmNewPasswordField.value) {
        document.getElementById('newPasswordError').textContent = 'New passwords do not match.';
        valid = false;
    }

    return valid;
}

function checkEmailAvailability(email, callback) {
    fetch("/check_email/?email=" + email)
        .then(response => response.json())
        .then(data => {
            let emailError = document.getElementById('emailError');
            if (data.is_taken) {
                emailError.textContent = 'This email is already taken.';
                if (callback) callback(false);
            } else {
                emailError.textContent = '';
                if (callback) callback(true);
            }
        })
        .catch(() => {
            document.getElementById('emailCheckError').textContent = 'An error occurred while checking the email.';
            if (callback) callback(false);
        });
      }




