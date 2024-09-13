// Add your custom JavaScript here
function getRecommendations() {
    const genre = document.getElementById('genre').value;
    const url = new URL('/recommendations', window.location.origin);
    
    if (genre) {
        url.searchParams.append('genre', genre);
    }

    fetch(url)
        .then(response => response.json())
        .then(data => {
            const recommendationsList = document.getElementById('recommendations');
            recommendationsList.innerHTML = '';
            data.forEach(movie => {
                const li = document.createElement('li');
                li.textContent = `${movie.title} (Rating: ${movie.rating})`;
                recommendationsList.appendChild(li);
            });
        })
        .catch(error => console.error('Error:', error));
}
