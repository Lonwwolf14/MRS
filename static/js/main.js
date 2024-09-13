// Add your custom JavaScript here
function getRecommendations(userId) {
    fetch(`/recommendations/${userId}`)
        .then(response => response.json())
        .then(data => {
            const recommendationsList = document.getElementById('recommendations');
            recommendationsList.innerHTML = '';
            data.forEach(movie => {
                const li = document.createElement('li');
                li.textContent = `${movie.title} (${movie.genres})`;
                recommendationsList.appendChild(li);
            });
        })
        .catch(error => console.error('Error:', error));
}
