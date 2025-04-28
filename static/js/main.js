// Simple JS for future enhancements
console.log("Frontend is live!");

window.onload = () => {
    document.querySelectorAll('.form-container').forEach(el => {
        el.classList.add('loaded');
    });
}
