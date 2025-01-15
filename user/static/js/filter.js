//Filtro
const openFilterBtn = document.getElementById('openFilterBtn');
const closeFilterBtn = document.getElementById('closeFilterBtn');
const filterOverlay = document.getElementById('filterOverlay');

openFilterBtn.addEventListener('click', () => {
    filterOverlay.classList.add('show'); 
});

closeFilterBtn.addEventListener('click', () => {
    filterOverlay.classList.remove('show'); 
});

//SELECT
const genreSelect = document.getElementById("genre");
const availabilitySelect = document.getElementById("availability");

genreSelect.addEventListener("change", function () {
    if (genreSelect.value === "") {
        genreSelect.style.color = "#999999";
    } else {
        genreSelect.style.color = "black";
    }
});

availabilitySelect.addEventListener("change", function () {
    if (availabilitySelect.value === "") {
        availabilitySelect.style.color = "#999999";
    } else {
        availabilitySelect.style.color = "black";
    }
});
