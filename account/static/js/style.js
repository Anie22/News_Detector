const form = document.getElementById('form');
const email = document.getElementById('email');
const password = document.getElementById('password');
const error = document.getElementById('warning');
const error2 = document.getElementById('warning2');
const model = document.getElementById('model');
const msg = document.getElementById('msg');
const buttonHolder =  document.getElementById('button')

model.style.display = 'none'

buttonHolder.innerHTML = `<button type="submit" class="bg-warning border-0 rounded-3 button col-12 fs-5 fw-semibold">Login</button>`
form.addEventListener('submit', (e) => {
    e.preventDefault();

    let hasError = false;

    /* checks if the input is empty */
    if(email.value.trim() === '') {
        error.textContent = 'Input Required';
        hasError = true;
    } else {
        error.textContent = '';
    }

    if(password.value.trim() === '') {
        error2.textContent = 'Input Required';
        hasError = true;
    } else {
        error2.textContent = '';
    }

    if(!hasError) {
        // Create an object with the form data
        const formData = new FormData(form);

        buttonHolder.innerHTML = `
                                <div class="loader rounded-3">
                                    <div class="loader-box d-flex align-items-center justify-content-center">
                                        <div class="load"></div>
                                    </div>
                                </div>`

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
                buttonHolder.innerHTML = `<button type="submit" class="bg-warning border-0 rounded-3 button col-12 fs-5 fw-semibold">Login</button>`
            }

            if (data.message === 'Login successfully') {

                const autoRedirect = setTimeout(() => {
                    model.style.display = 'none'
                    // Redirect to the news validation form page if login was successful
                    window.location.href = '';
                }, 2000);

                autoRedirect();

                return () => clearTimeout();
            }

            if (data.message !== 'Login successfully') {

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
email.addEventListener('input', function() {
    error.textContent = '';
});

password.addEventListener('input', function() {
    error2.textContent = '';
});
