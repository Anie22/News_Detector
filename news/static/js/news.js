const form = document.getElementById('form')
const newsHeading = document.getElementById('news_heading')
const newsSource = document.getElementById('news_source')
const newsLink = document.getElementById('news_url')
const error = document.getElementById('warning')
const error2 = document.getElementById('warning2')
const error3 = document.getElementById('warning3')
const model = document.getElementById('model');
const msg = document.getElementById('msg');
const buttonHolder =  document.getElementById('button')

model.style.display = 'none'

buttonHolder.innerHTML = `<button type="submit" class="bg-warning border-0 rounded-3 button col-12 fs-5 fw-semibold">Submit</button>`

form.addEventListener('submit', (e) => {
    e.preventDefault();

    let hasError = false;

    if(newsHeading.value.trim() == ''){
        error.textContent = 'Input required'
        hasError = true;
    } else {
        error.textContent = ''
    }

    if(newsSource.value.trim() == ''){
        error2.textContent = 'Input required'
        hasError = true
    } else {
        error2.textContent = ''
    }

    if(newsLink.value.trim() == ''){
        error3.textContent = 'Input required'
        hasError = true
    } else {
        error3.textContent = ''
    }

    if(!hasError) {

        // Create an object with the form data
        const formData = new FormData(form)

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
                buttonHolder.innerHTML = `<button type="submit" class="bg-warning border-0 rounded-3 button col-12 fs-5 fw-semibold">Submit</button>`
            }

            if (data.message === 'Saved and under verification') {

                const autoRedirect = setTimeout(() => {
                    model.style.display = 'none'
                    // Redirect to the news validation form page if login was successful
                    window.location.href = '/result';
                }, 3500);

                autoRedirect();

                return () => clearTimeout();
            }

            if (data.message !== 'Saved and under verification') {

                const autoRedirect = setTimeout(() => {
                    model.style.display = 'none'
                }, 7000);

                autoRedirect();

                return () => clearTimeout();
            }
        })
        .catch(error => console.error('Error:', error));
    }
})