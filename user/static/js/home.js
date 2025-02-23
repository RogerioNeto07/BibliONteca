document.querySelectorAll('.book-section').forEach((section) => {
    const prevBtn = section.querySelector('.prev-btn');
    const nextBtn = section.querySelector('.next-btn');
    const carouselTrack = section.querySelector('.carousel-track');
    let currentIndex = 0;

    function moveCarousel() {
        const bookCards = section.querySelectorAll('.book-card');
        const cardWidth = bookCards[0].offsetWidth + 16;
        const totalCards = bookCards.length;

        carouselTrack.style.transform = `translateX(-${currentIndex * cardWidth}px)`;

        prevBtn.style.display = totalCards > 1 ? 'block' : 'none';
        nextBtn.style.display = totalCards > 1 ? 'block' : 'none';
    }

    moveCarousel();

    prevBtn.addEventListener('click', () => {
        const totalCards = section.querySelectorAll('.book-card').length;

        if (currentIndex > 0) {
            currentIndex -= 3;
        } else {
            currentIndex = totalCards - 1;
        }
        moveCarousel();
    });

    nextBtn.addEventListener('click', () => {
        const totalCards = section.querySelectorAll('.book-card').length;

        if (currentIndex < totalCards - 4) {
            currentIndex += 3;
        } else {
            currentIndex = 0;
        }
        moveCarousel();
    });
});

