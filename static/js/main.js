document.addEventListener('DOMContentLoaded', () => {
    const recommendationForm = document.getElementById('recommendationForm');
    const recommendationsDiv = document.getElementById('recommendations');
    const resultsSection = document.getElementById('results');

    recommendationForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const title = document.getElementById('movieTitle').value;
        const genre = document.getElementById('genre').value;
        const minRating = document.getElementById('minRating').value;
        const numRecommendations = document.getElementById('numRecommendations').value || 10;

        let url = '/recommendations?';
        if (title) url += `title=${encodeURIComponent(title)}&`;
        if (genre) url += `genre=${encodeURIComponent(genre)}&`;
        if (minRating) url += `min_rating=${minRating}&`;
        url += `n=${numRecommendations}`;

        fetch(url)
            .then(response => response.json())
            .then(data => {
                recommendationsDiv.innerHTML = '';
                if (data.length === 0) {
                    recommendationsDiv.innerHTML = '<p class="no-results fade-in">No recommendations found. Try adjusting your criteria.</p>';
                    return;
                }
                resultsSection.style.display = 'block';
                data.forEach((movie, index) => {
                    const movieCard = document.createElement('div');
                    movieCard.className = 'movie-card fade-in';
                    movieCard.style.animationDelay = `${index * 0.1}s`;
                    movieCard.innerHTML = `
                        <div class="movie-poster" style="background-image: url('https://image.tmdb.org/t/p/w500${movie.poster_path}')"></div>
                        <div class="movie-info">
                            <h3>${movie.title}</h3>
                            <p class="rating"><i class="fas fa-star"></i> ${movie.rating.toFixed(1)}</p>
                            <p class="genres"><i class="fas fa-film"></i> ${movie.genres}</p>
                            <button class="more-info-btn" data-movie-id="${movie.id}">More Info</button>
                        </div>
                    `;
                    recommendationsDiv.appendChild(movieCard);
                });
                addMoreInfoEventListeners();
            })
            .catch(error => {
                console.error('Error:', error);
                recommendationsDiv.innerHTML = '<p class="error fade-in">An error occurred while fetching recommendations. Please try again.</p>';
            });
    });

    function addMoreInfoEventListeners() {
        const moreInfoButtons = document.querySelectorAll('.more-info-btn');
        moreInfoButtons.forEach(button => {
            button.addEventListener('click', () => {
                const movieId = button.getAttribute('data-movie-id');
                fetchMovieDetails(movieId);
            });
        });
    }

    function fetchMovieDetails(movieId) {
        fetch(`/movie/${movieId}`)
            .then(response => response.json())
            .then(movie => {
                showMovieModal(movie);
            })
            .catch(error => {
                console.error('Error fetching movie details:', error);
            });
    }

    function showMovieModal(movie) {
        const modal = document.createElement('div');
        modal.className = 'movie-modal';
        modal.innerHTML = `
            <div class="modal-content">
                <span class="close-modal">&times;</span>
                <h2>${movie.title}</h2>
                <img src="https://image.tmdb.org/t/p/w500${movie.poster_path}" alt="${movie.title} poster">
                <p><strong>Rating:</strong> ${movie.rating.toFixed(1)}</p>
                <p><strong>Genres:</strong> ${movie.genres}</p>
                <p><strong>Overview:</strong> ${movie.overview}</p>
            </div>
        `;
        document.body.appendChild(modal);

        const closeModal = modal.querySelector('.close-modal');
        closeModal.addEventListener('click', () => {
            document.body.removeChild(modal);
        });
    }
});
