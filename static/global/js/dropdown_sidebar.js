const toggleBook = document.getElementById('toggle-book');
const contentBook = document.getElementById('dropdown-book');

toggleBook.addEventListener('click', () => {
 if (contentBook.style.display === 'none'){
    contentBook.style.display = 'block';
    localStorage.setItem('bookState', 'open');
 } else {
    contentBook.style.display = 'none';
    localStorage.setItem('bookState', 'closed');
 } 
});

const contentUser = document.getElementById('dropdown-user');
const toggleUser = document.getElementById('toggle-user');

toggleUser.addEventListener('click', () => {
 if (contentUser.style.display === 'none'){
    contentUser.style.display = 'block';
    localStorage.setItem('userState', 'open');
} else {
    contentUser.style.display = 'none';
    localStorage.setItem('userState', 'closed');
 }
});

const contentLoan = document.getElementById('dropdown-loan');
const toggleLoan = document.getElementById('toggle-loan');

toggleLoan.addEventListener('click', () => {
 if (contentLoan.style.display === 'none'){
    contentLoan.style.display = 'block';
    localStorage.setItem('loanState', 'open');
} else {
    contentLoan.style.display = 'none';
    localStorage.setItem('loanState', 'closed');
 }
});

window.addEventListener('load', ()=> {
    const bookState = localStorage.getItem('bookState');
    const contentBook = document.getElementById('dropdown-book');
    
    const userState = localStorage.getItem('userState');
    const contentUser = document.getElementById('dropdown-user');

    const loanState = localStorage.getItem('loanState');
    const contentLoan = document.getElementById('dropdown-loan');

    bookState==='open' ? contentBook.style.display = 'block' : contentBook.style.display = 'none';
    userState==='open' ? contentUser.style.display = 'block': contentUser.style.display = 'none';
    loanState==='open' ? contentLoan.style.display = 'block': contentLoan.style.display = 'none';
});