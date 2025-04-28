// Sample destination list (you could replace this with an API call later)
const destinations = [
    "New York", "Paris", "London", "Tokyo", "Los Angeles",
    "Berlin", "Sydney", "Rome", "Amsterdam", "Barcelona"
  ];
  
  // Get the input field and suggestion list
  const destinationInput = document.getElementById('destination');
  const suggestionsList = document.getElementById('suggestions-list');
  
  // ✅ Only run the logic if the input exists
  if (destinationInput && suggestionsList) {
    // Function to filter and display suggestions
    function showSuggestions(value) {
      // Clear previous suggestions
      suggestionsList.innerHTML = '';
    
      // Filter destinations based on input value
      const filteredDestinations = destinations.filter(destination =>
        destination.toLowerCase().includes(value.toLowerCase())
      );
    
      // If there are no suggestions, hide the list
      if (filteredDestinations.length === 0) {
        suggestionsList.style.display = 'none';
      } else {
        suggestionsList.style.display = 'block';
        // Add filtered suggestions to the list
        filteredDestinations.forEach(destination => {
          const listItem = document.createElement('li');
          listItem.classList.add('list-group-item');
          listItem.textContent = destination;
          // When a suggestion is clicked, set it as the input value
          listItem.addEventListener('click', () => {
            destinationInput.value = destination;
            suggestionsList.style.display = 'none';
          });
          suggestionsList.appendChild(listItem);
        });
      }
    }
  
    // Listen for input and call showSuggestions
    destinationInput.addEventListener('input', (e) => {
      showSuggestions(e.target.value);
    });
  }
  