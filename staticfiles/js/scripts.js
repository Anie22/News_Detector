const year = document.getElementById('year')

const autoYear = () => {
    const date = new Date()
    const currentYear =  date.getFullYear()
    year.textContent = currentYear
}

autoYear()