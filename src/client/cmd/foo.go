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
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"

	"github.com/spf13/cobra"
)

var token string
var FOO_URL = "http://localhost/api/foo"
var FOOS_URL = "http://localhost/api/foos"

// fooCmd represents the foo command
var fooCmd = &cobra.Command{
	Use:   "foo",
	Short: "A brief description of your command",
	Long: `A longer description that spans multiple lines and likely contains examples
and usage of using your command. For example:

Cobra is a CLI library for Go that empowers applications.
This application is a tool to generate the needed files
to quickly create a Cobra application.`,
	Run: func(cmd *cobra.Command, args []string) {

		token, _ := cmd.Flags().GetString("token")
		fmt.Printf("This is the token: %s\n", token)
		if token != "" {
			callFoos(token)
		} else {
			callFoo()
		}
	},
}

func init() {
	rootCmd.AddCommand(fooCmd)
	fooCmd.Flags().StringVarP(&token, "token", "t", "", "Make request to token")
	// Here you will define your flags and configuration settings.

	// Cobra supports Persistent Flags which will work for this command
	// and all subcommands, e.g.:
	// fooCmd.PersistentFlags().String("foo", "", "A help for foo")

	// Cobra supports local flags which will only run when this command
	// is called directly, e.g.:
	// fooCmd.Flags().BoolP("toggle", "t", false, "Help message for toggle")
}

func callFoo() {
	resp, err := http.Get(FOO_URL)
	if err != nil {
		fmt.Println("Error in the request")
		os.Exit(0)
	}

	//We Read the response body on the line below.
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatalln(err)
	}
	//Convert the body to type string
	fmt.Printf("foo: %s\n", string(body))
}

func callFoos(tok string) {
	var bearer = "Bearer " + tok

	req, err := http.NewRequest("GET", FOOS_URL, nil)
	if err != nil {
		fmt.Println("Error creating the request")
		os.Exit(0)
	}

	req.Header.Add("Authorization", bearer)
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
	fmt.Printf("foos: %s\n", string(body))
}
