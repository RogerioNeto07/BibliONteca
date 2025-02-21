document.addEventListener('DOMContentLoaded', function () {
    const stars = document.querySelectorAll('.star-rating .star');
    const ratingInput = document.getElementById('star-rating-input');

    stars.forEach((star) => {
        star.addEventListener('click', function () {
            const rating = this.getAttribute('data-rating');
            ratingInput.value = rating;

            stars.forEach(s => {
                const starRating = s.getAttribute('data-rating');
                if (starRating <= rating) {
                    s.classList.add('selected');
                    s.style.color = 'gold';
                } else {
                    s.classList.remove('selected');
                    s.style.color = 'gray';
                }
            });
        });
    });
});
