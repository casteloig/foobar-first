/*
Copyright © 2021 NAME HERE <EMAIL ADDRESS>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/
package cmd

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"strconv"

	"github.com/spf13/cobra"
)

var FACTORIAL_URL = "http://localhost/api/maths/factorial"
var FIBONACCI_URL = "http://localhost/api/maths/fibonacci"

var factorial string
var fibonacci string

// mathsCmd represents the maths command
var mathsCmd = &cobra.Command{
	Use:   "maths",
	Short: "A brief description of your command",
	Long: `A longer description that spans multiple lines and likely contains examples
and usage of using your command. For example:

Cobra is a CLI library for Go that empowers applications.
This application is a tool to generate the needed files
to quickly create a Cobra application.`,
	Run: func(cmd *cobra.Command, args []string) {

		factorial, _ := cmd.Flags().GetString("factorial")
		if factorial != "" {
			n, _ := strconv.Atoi(factorial)
			callFactorial(n)
		}

		fibonacci, _ := cmd.Flags().GetString("fibonacci")
		if fibonacci != "" {
			fmt.Println("por que entramos aqui")
			n, _ := strconv.Atoi(fibonacci)
			callFibonacci(n)
		}
	},
}

func init() {
	rootCmd.AddCommand(mathsCmd)
	mathsCmd.Flags().StringVarP(&factorial, "factorial", "a", "", "Make request factorial")
	mathsCmd.Flags().StringVarP(&fibonacci, "fibonacci", "b", "", "Make request fibonacci")
	// Here you will define your flags and configuration settings.

	// Cobra supports Persistent Flags which will work for this command
	// and all subcommands, e.g.:
	// mathsCmd.PersistentFlags().String("foo", "", "A help for foo")

	// Cobra supports local flags which will only run when this command
	// is called directly, e.g.:
	// mathsCmd.Flags().BoolP("toggle", "t", false, "Help message for toggle")
}

func callFactorial(number int) {

	m := make(map[string]int)
	m["number"] = number
	jsonString, _ := json.Marshal(m)

	req, err := http.NewRequest("POST", FACTORIAL_URL, bytes.NewBuffer(jsonString))
	if err != nil {
		fmt.Println("Error creating the request")
		os.Exit(0)
	}
	req.Header.Set("Content-Type", "application/json")

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Println("Error sending the request")
		os.Exit(0)
	}

	//We Read the response body on the line below.
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatalln(err)
	}
	//Convert the body to type string
	fmt.Printf("factorial: %s\n", string(body))
}

func callFibonacci(number int) {

	m := make(map[string]int)
	m["number"] = number
	jsonString, _ := json.Marshal(m)

	req, err := http.NewRequest("POST", FIBONACCI_URL, bytes.NewBuffer(jsonString))
	if err != nil {
		fmt.Println("Error creating the request")
		os.Exit(0)
	}
	req.Header.Set("Content-Type", "application/json")

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Println("Error sending the request")
		os.Exit(0)
	}

	//We Read the response body on the line below.
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatalln(err)
	}
	//Convert the body to type string
	fmt.Printf("fibonacci: %s\n", string(body))
}
