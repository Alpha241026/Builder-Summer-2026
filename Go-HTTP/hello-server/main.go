package main

import (
	"fmt"
	"log"
	"net/http"
)

// Handler function.
// Runs whenever someone visits "/".
func hello(w http.ResponseWriter, r *http.Request) {

	// Send this text back to the browser.
	fmt.Fprintln(w, "Hello from Go!")

}

func main() {

	// Register "/" to the hello() handler.
	http.HandleFunc("/", hello)

	fmt.Println("Server running on http://localhost:8080")

	// Start listening on port 8080.
	err := http.ListenAndServe(":8080", nil)

	// If the server crashes,
	// print the error and exit.
	if err != nil {
		log.Fatal(err)
	}

}
