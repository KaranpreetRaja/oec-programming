const fileInput = document.querySelector('input[type="file"]');

// Handle the file selection event
fileInput.addEventListener('change', (event) => {
    const file = event.target.files[0];
    const formData = new FormData();

    // Append the file to the form data
    formData.append('image', file);

    // Send the form data to the Flask backend using fetch
    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response from the backend
        console.log(data);
    })
    .catch(error => {
        // Handle any errors
        console.error(error);
    });
});