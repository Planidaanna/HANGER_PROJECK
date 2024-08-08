document.getElementById('filterImage').onclick = function() {
    const form = document.getElementById('filterForm');
   
    if (form.style.display === "none" || form.style.display === "") {
        form.style.display = "block"; 
    } else {
        form.style.display = "none"; 
    }
};

function addToFavorites(element) {
    const collectionId = element.getAttribute('data-id');
    fetch(`/favorites/${collectionId}/`, {
        method: 'GET',
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
    .then(response => {
        if (response.redirected) {
            window.location.href = response.url; // Перенаправление на страницу (например, на favorites.html)
        } else {
            alert('Добавлено в избранное');
        }
    })
    .catch(error => console.error('Ошибка:', error));
}
