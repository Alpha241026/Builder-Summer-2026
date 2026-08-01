package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
)

// user defined type for book data
type Book struct {
	ID    int    `json:"id"`
	Title string `json:"title"`
}

// fake database
var books = []Book{
	{ID: 1, Title: "Dune"},
	{ID: 2, Title: "1984"},
	{ID: 3, Title: "Sapiens"},
}

// handler function for printing content when someone visits browser
func getBooks(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json") //telling browser to expect json data
	json.NewEncoder(w).Encode(books)                   //encoding go slice to json format to show on browser
}

// handler function for additonal sample home page
func home(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "Welcome to the Books API!")
}

func main() {
	http.HandleFunc("/books", getBooks) //register books API endpoint
	http.HandleFunc("/", home)          //registering home route

	fmt.Println("Server running on http://localhost:8080")

	err := http.ListenAndServe(":8080", nil) //starting server

	if err != nil { //printing error if server crashes (and exiting)
		log.Fatal(err)
	}
}
