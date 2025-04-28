// static/booking/js/script.js
document.addEventListener('DOMContentLoaded', function () {
    console.log('Page loaded and JS is working!');

    // Add any interactive features you'd like here
    // For example, a simple alert when a property card is clicked:
    const propertyCards = document.querySelectorAll('.property-card');

    propertyCards.forEach(card => {
        card.addEventListener('click', () => {
            alert('You clicked a property card!');
        });
    });
});
