document.getElementById('filterImage').onclick = function() {
    const form = document.getElementById('filterForm');
   
    if (form.style.display === "none" || form.style.display === "") {
        form.style.display = "block"; 
    } else {
        form.style.display = "none"; 
    }
};


