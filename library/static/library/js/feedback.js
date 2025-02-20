document.addEventListener('DOMContentLoaded', function () {
    const stars = document.querySelectorAll('.star-rating .star');

    stars.forEach((star, index) => {
        star.addEventListener('click', () => {
            stars.forEach(s => s.classList.remove('selected'));

            for (let i = 0; i <= index; i++) {
                stars[i].classList.add('selected');
            }
        });
    });
});
