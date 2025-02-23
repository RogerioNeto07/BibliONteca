const openFilterBtn = document.getElementById('openFilterBtn');
const closeFilterBtn = document.getElementById('closeFilterBtn');
const filterOverlay = document.getElementById('filterOverlay');
const genreSelect = document.getElementById("genre");
const availabilitySelect = document.getElementById("availability");

openFilterBtn.addEventListener('click', () => {
    filterOverlay.classList.add('show');
});

closeFilterBtn.addEventListener('click', () => {
    filterOverlay.classList.remove('show');
});

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

const filterForm = document.getElementById('filterForm');
filterForm.addEventListener('submit', function (e) {
    const genre = genreSelect.value;
    const availability = availabilitySelect.value;

    let url = new URL(window.location.href);
    
    if (genre) url.searchParams.set('genre', genre);
    
    if (availability) url.searchParams.set('availability', availability);

    window.location.href = url.toString();
    e.preventDefault();
});
