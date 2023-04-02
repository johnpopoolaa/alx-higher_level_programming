#!/usr/bin/python3

"""
Script that uses the GitHub API to display your id
"""

import requests
import sys

if __name__ == "__main__":
    # Check if the correct number of arguments was given
    if len(sys.argv) != 3:
        print("Usage: {} username token".format(sys.argv[0]))
        sys.exit(1)

    # Get the username and token from the command line arguments
    johnpopoolaa = sys.argv[1]
    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 = sys.argv[2]

    # Make a GET request to the GitHub API to get the authenticated user's info
    response = requests.get(
            "https://api.github.com/user", auth=(
                johnpopoolaa, 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))

    # Check if the response was successful
    if response.status_code == 200:
        # Display the user's ID
        user_id = response.json()["id"]
        print("Your user ID is:", user_id)
    else:
        # Display an error message if the response was not successful
        print("Error:", response.status_code)
