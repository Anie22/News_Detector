const year = document.getElementById('year')
const greetings = document.getElementById('greeting')

const autoYear = () => {
    const date = new Date()
    const currentYear =  date.getFullYear()
    year.textContent = currentYear
}

autoYear()

const autoGreet = () => {
    const hour = new Date()
    const currentTime = hour.getHours()

    if(currentTime >= 4 && currentTime <= 11){
        greetings.textContent = 'Good Morning'
    } else if(currentTime >= 12 && currentTime <= 15) {
        greetings.textContent = 'Good Afternoon'
    } else if(currentTime >= 16 && currentTime <= 21){
        greetings.textContent = 'Good Evening'
    }
}

autoGreet()