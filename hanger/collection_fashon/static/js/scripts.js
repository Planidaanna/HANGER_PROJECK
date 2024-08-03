document.getElementById('filterImage').onclick = function() {
    const form = document.getElementById('filterForm');
    //  видимость формы
    if (form.style.display === "none" || form.style.display === "") {
        form.style.display = "block"; 
    } else {
        form.style.display = "none"; 
    }
};

document.querySelectorAll('.favorit-img').forEach(function(img) {
    img.addEventListener('click', function() {
        const collectionId = this.getAttribute('data-id');
        fetch('/add_to_favorites', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}'  // Для защиты от CSRF-атак
            },
            body: JSON.stringify({ id: collectionId })
        })
        .then(response => {
            if (response.ok) {
                alert('Элемент добавлен в избранное!');
            } else {
                alert('Ошибка при добавлении в избранное.');
            }
        })
        .catch(error => {
            console.error('Ошибка:', error);
        });
    });
});