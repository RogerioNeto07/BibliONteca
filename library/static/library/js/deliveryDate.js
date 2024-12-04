const dateToday = new Date();
let dateDelivery = new Date();

dateDelivery.setDate(dateToday.getDate() + 15);
const dateFormat = dateDelivery.toLocaleDateString('pt-br');

document.querySelector('.date').textContent = dateFormat;