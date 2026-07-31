
---

# JS Notes

## The Browser's Three Jobs

```text
1. Listen to the user
        ↓
2. Talk to the backend
        ↓
3. Update the page
```

These map to:

```text
Event → Fetch → DOM
```

This is essentially the entire Pulse V1 frontend.

---

## DOM

The DOM (Document Object Model) is JavaScript's in-memory representation of the HTML page.

Common operations:

```javascript
document.querySelector(...)
```

Find an element.

```javascript
document.createElement(...)
```

Create a new HTML element.

```javascript
element.append(...)
```

Attach an element to the page.

```javascript
element.textContent = ...
```

Change displayed text.

```javascript
element.classList.add(...)
```

Modify CSS classes.

---

## Events

Events let JavaScript react to user actions.

```javascript
button.addEventListener("click", handler);
```

Flow:

```text
User clicks
        ↓
Browser fires "click"
        ↓
JavaScript function executes
```

---

## Fetch API

`fetch()` sends an HTTP request from the browser.

```javascript
const response = await fetch(url);
```

Returns a **Response object**, not JSON directly.

Useful properties:

```javascript
response.ok
response.status
```

Convert body:

```javascript
const data = await response.json();
```

---

## async / await

Many browser operations take time.

Instead of blocking the page,

JavaScript waits asynchronously.

```javascript
async function loadData() {

    const response = await fetch(...);

    const data = await response.json();

}
```

Mental model:

```text
async

↓

This function is allowed to pause.

await

↓

Pause until this operation finishes.
```

---

## Common Flow

Every frontend API call follows the same shape.

```text
User Action
        ↓
Event Listener
        ↓
fetch()
        ↓
Server
        ↓
JSON Response
        ↓
Update DOM
```

---

## Difference from Python Requests

Python:

```python
response = requests.get(...)
```

Program waits naturally.

Browser:

```javascript
const response = await fetch(...)
```

Browser must stay responsive,

so asynchronous waiting is required.

---

## Pulse Connection

Pulse will repeatedly perform this cycle:

```text
Click Endpoint
        ↓
GET /projects
        ↓
Receive JSON
        ↓
Render Sidebar

-----------------------

Click Send
        ↓
POST /execute
        ↓
Receive Response
        ↓
Render Response Panel
```

---

## Takeaway

> **The frontend doesn't contain business logic. It gathers user input, communicates with the backend over HTTP, and renders the backend's response.**

---