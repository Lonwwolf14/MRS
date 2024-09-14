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

        const params = new URLSearchParams({
            ...(title && { title }),
            ...(genre && { genre }),
            ...(minRating && { min_rating: minRating }),
            n: numRecommendations
        });

        fetchRecommendations(`/recommendations?${params}`);
    });

    async function fetchRecommendations(url) {
        recommendationsDiv.innerHTML = '<p class="loading pulse">Loading recommendations...</p>';
        resultsSection.style.display = 'block';

        try {
            const response = await fetch(url);
            if (!response.ok) throw new Error('Network response was not ok');
            const data = await response.json();
            displayRecommendations(data);
        } catch (error) {
            console.error('Error:', error);
            recommendationsDiv.innerHTML = '<p class="error shake-x">An error occurred while fetching recommendations. Please try again.</p>';
        }
    }

    function displayRecommendations(data) {
        recommendationsDiv.innerHTML = '';
        if (data.length === 0) {
                    recommendationsDiv.innerHTML = `
                        <div class="no-results-container bounce-in">
                            <i class="fas fa-film fa-4x"></i>
                            <h3>No Recommendations Found</h3>
                            <p>Try adjusting your search criteria for better results.</p>
                        </div>
                    `;
            return;
        }

        const fragment = document.createDocumentFragment();
        data.forEach((movie, index) => {
            const movieCard = createMovieCard(movie);
            movieCard.classList.add(`fade-in`, `delay-${index % 5 + 1}`);
            fragment.appendChild(movieCard);
        });
        recommendationsDiv.appendChild(fragment);

        addHoverEffects();
        addMoreInfoEventListeners();
    }

    function createMovieCard(movie) {
        const movieCard = document.createElement('div');
        movieCard.className = 'movie-card';
        movieCard.innerHTML = `
            <div class="movie-poster" style="background-image: url('${movie.poster_path ? `https://image.tmdb.org/t/p/w500${movie.poster_path}` : '/static/images/default-movie-poster.jpg'}')"></div>
            <div class="movie-info">
                <h3>${movie.title}</h3>
                <p class="rating"><i class="fas fa-star"></i> ${movie.rating.toFixed(1)}</p>
                <button class="more-info-btn" data-movie-id="${movie.id}">More Info</button>
            </div>
        `;
        return movieCard;
    }

    function addHoverEffects() {
        const movieCards = document.querySelectorAll('.movie-card');
        movieCards.forEach(card => {
            card.addEventListener('mouseenter', () => {
                card.style.animationPlayState = 'running'; // Resume animation
                card.classList.add('pulse');
            });
    
            card.addEventListener('mouseleave', () => {
                card.style.animationPlayState = 'paused'; // Pause animation
                card.classList.remove('pulse'); // Remove class immediately to reset
            });
        });
    }
    
    

    function addMoreInfoEventListeners() {
        const moreInfoButtons = document.querySelectorAll('.more-info-btn');
        moreInfoButtons.forEach(button => {
            button.addEventListener('click', () => {
                const movieId = button.getAttribute('data-movie-id');
                fetchMovieDetails(movieId);
            });
        });
    }

    async function fetchMovieDetails(movieId) {
        try {
            const response = await fetch(`/movie/${movieId}`);
            if (!response.ok) throw new Error('Network response was not ok');
            const movie = await response.json();
            showMovieModal(movie);
        } catch (error) {
            console.error('Error fetching movie details:', error);
            alert('Failed to fetch movie details. Please try again.');
        }
    }

    function showMovieModal(movie) {
        const modal = document.createElement('div');
        modal.className = 'movie-modal fade-in';
        modal.innerHTML = `
            <div class="modal-content slide-in">
                <span class="close-modal">&times;</span>
                <h2>${movie.title}</h2>
                <img src="${movie.poster_path ? `https://image.tmdb.org/t/p/w500${movie.poster_path}` : '/static/images/default-movie-poster.jpg'}" alt="${movie.title} poster">
                <p><strong>Rating:</strong> ${movie.vote_average?.toFixed(1) ?? 'N/A'}</p>
                <p><strong>Genres:</strong> ${movie.genres?.map(g => g.name).join(', ') ?? 'N/A'}</p>
                <p><strong>Overview:</strong> ${movie.overview ?? 'No overview available.'}</p>
            </div>
        `;
        document.body.appendChild(modal);

        const closeModal = modal.querySelector('.close-modal');
        closeModal.addEventListener('click', () => document.body.removeChild(modal));

        modal.addEventListener('click', (e) => {
            if (e.target === modal) document.body.removeChild(modal);
        });
    }
});