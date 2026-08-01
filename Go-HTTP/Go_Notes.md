# Go net/http Notes

## Execution Flow

Client (Browser)

↓

Request

↓

Go Server

↓

Handler Function

↓

Response

↓

Browser


Every HTTP server follows the same lifecycle:

Register Routes
↓

Start Server
↓

Receive Request
↓

Handler Executes
↓

Write Response
↓

Repeat Forever


## Core Components

### Handler Function

```go
func hello(w http.ResponseWriter, r *http.Request)

r → Read information sent by the client.
w → Write the response back to the client.
Registering Routes
http.HandleFunc("/", hello)

Associates a URL path with a handler function.

Equivalent Flask idea:

@app.route("/")
Starting the Server
http.ListenAndServe(":8080", nil)

Starts listening on port 8080.

nil means use the default ServeMux (router).

Sending Plain Text
fmt.Fprintln(w, "Hello")

Unlike fmt.Println(), this writes to the browser instead of the terminal.

Returning JSON
w.Header().Set("Content-Type","application/json")
json.NewEncoder(w).Encode(data)
Tell browser to expect JSON.
Encode Go objects directly into JSON.
Send them as the HTTP response.
Mental Model

Request
↓

Read Request (r)
↓

Business Logic
↓

Create Response
↓

Write Response (w)


---