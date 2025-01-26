// Sets background images for project cards by using their img sources as CSS variables
document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.specific-projects-card-item');
    
    cards.forEach(card => {
        const img = card.querySelector('img');
        if (img) {
            card.style.setProperty('--preview-url', `url('${img.src}')`);
        }
    });
});