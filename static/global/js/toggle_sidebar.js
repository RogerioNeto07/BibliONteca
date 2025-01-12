const button_toggle = document.getElementById('toggle');
const sidebar = document.getElementById('sidebar-menu');
const button_rotate = document.getElementById('button-togle-rotate')

button_toggle.addEventListener('click', () => {
    if (sidebar.style.display === 'none' || sidebar.style.display === ''){
        sidebar.style.display = 'block';
        button_rotate.textContent = 'chevron_left'
     } else {
        sidebar.style.display = 'none';
        button_rotate.textContent = 'chevron_right'

     } 
} )