# Star Wars API Project

This project is a Python script that interacts with the Star Wars API (SWAPI) to fetch data about Star Wars characters. The script saves the fetched data into a JSON file and an SQLite database, ensuring no duplicate entries are added to the database.

## How It Works

The script performs the following steps:

1. Prompts the user to fetch Star Wars character data.
2. Sends a GET request to the SWAPI to retrieve data for a specific character.
3. Checks the response status and parses the JSON data.
4. Saves the JSON data to a file named after the character (sanitized to be a valid filename).
5. Connects to an SQLite database and creates a table if it doesn't exist.
