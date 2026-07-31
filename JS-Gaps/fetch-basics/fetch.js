// Find the Fetch button
const button = document.querySelector("#b1");

// When the button is clicked,
// execute the getBooks() function.
button.addEventListener("click", getBooks);

// async allows us to use 'await'
// while waiting for network requests.
async function getBooks() {

    // Send a GET request to the Flask server.
    // fetch() returns a Response object,
    // not the actual JSON.
    const response = await fetch("http://127.0.0.1:5000/books");

    // Convert the response body into a
    // JavaScript array of objects.
    const data = await response.json();

    // Display the title of the first book
    // inside the paragraph.
    document.querySelector("#bookTitle").textContent = data[0].title;

}