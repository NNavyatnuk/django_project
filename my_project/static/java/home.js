document.addEventListener('DOMContentLoaded', function () {
    // Слайдер баннера
    let index = 0;
    const slider = document.getElementById('banner-slider');
    const slides = document.querySelectorAll('.banner-slide');

    function showSlide(i) {
        slider.style.transform = `translateX(-${i * 100}%)`;
    }

    setInterval(() => {
        index = (index + 1) % slides.length;
        showSlide(index);
    }, 5000);

    const cards = document.querySelectorAll('.movie-card');
    const modal = document.getElementById('movieModal');
    const modalPoster = document.getElementById('modalPoster');
    const modalTitle = document.getElementById('modalTitle');
    const modalRating = document.getElementById('modalRating');
    const modalPrice = document.getElementById('modalPrice');
    const modalDescription = document.getElementById('modalDescription');
    const modalInfo = document.getElementById('modalInfo');

    document.body.addEventListener('click', (e) => {
        if (!e.target.closest('.movie-card') && !e.target.closest('.modal')) {
            modal.style.display = 'none';
        }
    });

    cards.forEach(card => {
        card.addEventListener('click', (e) => {
            e.stopPropagation();

            modalPoster.src = card.dataset.poster;
            modalTitle.innerText = card.dataset.title;
            modalRating.innerText = "⭐ " + card.dataset.rating + " / 10";
            modalPrice.innerText = "Цена: " + card.dataset.price;
            modalDescription.innerText = card.dataset.description;
            modalInfo.innerHTML = `
                <strong>Жанр:</strong> ${card.dataset.genre}<br>
                <strong>Год:</strong> ${card.dataset.year}<br>
                <strong>Актеры:</strong> ${card.dataset.actors}<br>
                <strong>Режиссёр:</strong> ${card.dataset.director}
            `;

            const rect = card.getBoundingClientRect();
            modal.style.display = 'block';
            modal.style.top = `${window.scrollY + rect.top}px`;
            modal.style.left = `${rect.right + 20}px`;
        });
    });
});
