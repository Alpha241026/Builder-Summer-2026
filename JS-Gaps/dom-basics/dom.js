// Find the button element from the HTML page
const button = document.querySelector("#b1");

// Register an event listener.
// Whenever the button is clicked,
// call the addElement() function.
button.addEventListener("click", addElement);

function addElement() {

    // Create a brand new <li> element.
    // Right now it only exists in memory,
    // not on the webpage.
    const newEl = document.createElement("li");

    // Set the text inside the new list item.
    newEl.textContent = "El4";

    // Find the unordered list (<ul>)
    // and append the new element to it.
    // Once appended, it becomes visible
    // on the webpage.
    document.querySelector("#Unli").append(newEl);

}