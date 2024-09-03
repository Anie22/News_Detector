const form = document.getElementById('form');
const fullName = document.getElementById('full_name');
const userName = document.getElementById('user_name');
const email = document.getElementById('email');
const password = document.getElementById('password');
const confirm_Password = document.getElementById('password2');
const error1 = document.getElementById('warning');
const error2 = document.getElementById('warning2');
const error3 = document.getElementById('warning3');
const error4 = document.getElementById('warning4');
const error5 = document.getElementById('warning5');
const model = document.getElementById('model')
const msg = document.getElementById('msg')

model.style.display = 'none'

form.addEventListener('submit', (e) => {
    e.preventDefault();

    let hasError = false;

    /* checks if the input is empty */
    if(fullName.value.trim() === '') {
        error1.textContent = 'Input Required';
        hasError = true;
    } else {
        error1.textContent = '';
    }

    if(userName.value.trim() == '') {
        error2.textContent = 'Input Required';
        hasError = true;
    } else {
        error2.textContent = '';
    }

    if(email.value.trim() == '') {
        error3.textContent = 'Input Required';
        hasError = true;
    } else {
        error3.textContent = '';
    }

    if(password.value.trim() == '') {
        error4.textContent = 'Input Required';
        hasError = true;
    } else {
        error4.textContent = '';
    }

    if(confirm_Password.value.trim() == '') {
        error5.textContent = 'Input Required';
        hasError = true;
    } else if(password.value != confirm_Password.value) {
        error5.textContent = 'Passwords do not match';
        hasError = true;
    } else {
        error5.textContent = '';
    }

    if(!hasError) {
        // Create an object with the form data
        const formData = new FormData(form);

        // Send an AJAX request to the server
        fetch('', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
            }
        })
        .then(response => response.json())
        .then(data => {
            // Handle the JSON response from the server
            if (data.message) {
                model.style.display = 'flex'
                msg.textContent = data.message
            }

            if (data.message === 'Sign up successfully') {

                const autoRedirect = setTimeout(() => {
                    model.style.display = 'none'
                    // Redirect to login page if registration was successful
                    window.location.href = '/account/login/';
                }, 2000);

                autoRedirect();

                return () => clearTimeout();
            }

            if (data.message !== 'Sign up successfully') {

                const autoRedirect = setTimeout(() => {
                    model.style.display = 'none'
                }, 2000);

                autoRedirect();

                return () => clearTimeout();
            }
        })
        .catch(error => console.error('Error:', error));
    }
});

/* removes the error message on input */
fullName.addEventListener('input', function() {
    error1.textContent = '';
});

userName.addEventListener('input', function() {
    error2.textContent = '';
});

email.addEventListener('input', function() {
    error3.textContent = '';
});

password.addEventListener('input', function() {
    error4.textContent = '';
});

confirm_Password.addEventListener('input', function() {
    error5.textContent = '';
});