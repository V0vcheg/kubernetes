package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
)

func helloHandler(w http.ResponseWriter, r *http.Request) {
	apiKey := os.Getenv("API_KEY")
	log.Printf("Received request, using API key: %s", apiKey)
	fmt.Fprintf(w, "Hello from User-Service, using API key: %s", apiKey)
}

func main() {
	f, err := os.OpenFile("/var/log/user.log", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	log.SetOutput(f)

	log.Println("User service started with key : " + os.Getenv("API_KEY"))

	http.HandleFunc("/", helloHandler)
	http.ListenAndServe(":3002", nil)
}
