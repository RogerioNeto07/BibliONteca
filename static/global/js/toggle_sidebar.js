const button_toggle = document.getElementById('toggle');
const sidebar = document.getElementById('sidebar-menu');
const button_rotate = document.getElementById('button-togle-rotate')
const body = document.querySelector('body')

button_toggle.addEventListener('click', () => {
    if (sidebar.style.display === 'block' || sidebar.style.display === ''){
        sidebar.style.display = 'none';
        button_rotate.textContent = 'chevron_right'
        body.style.display = 'grid'
        body.style.gridTemplateColumns = '24px auto'
        button_toggle.style.position = 'fixed'
        button_toggle.style.left = '0'

     } else {
        sidebar.style.display = 'block';
        button_rotate.textContent = 'chevron_left'
        body.style.display = 'grid'
        body.style.gridTemplateColumns = '220px 24px auto'
        button_toggle.style.position = 'fixed'
        button_toggle.style.left = '220px'
     } 
} )