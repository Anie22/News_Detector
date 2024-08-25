const form = document.getElementById('form');
const email = document.getElementById('email');
const password = document.getElementById('password');
const error3 = document.getElementById('warning3');
const error4 = document.getElementById('warning4');
const model = document.getElementById('model')
const msg = document.getElementById('msg')

model.style.display = 'none'

form.addEventListener('submit', (e) => {
    e.preventDefault();

    let hasError = false;

    /* checks if the input is empty */
    if(email.value.trim() === '') {
        error3.textContent = 'Input Required';
        hasError = true;
    } else {
        error3.textContent = '';
    }

    if(password.value.trim() === '') {
        error4.textContent = 'Input Required';
        hasError = true;
    } else {
        error4.textContent = '';
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

            if (data.status === 200) {
                // Redirect to the news validation form page if login was successful
                window.location.href = '/detect-fake-news';
            }
        })
        .catch(error => console.error('Error:', error));
    }
});

/* removes the error message on input */
email.addEventListener('input', function() {
    error3.textContent = '';
});

password.addEventListener('input', function() {
    error4.textContent = '';
});
