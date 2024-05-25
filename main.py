import json
import requests
import sqlite3

counter = 1


while True:
    userInput = input("Do you want to fetch star wars character ?(yes, no)")
    if userInput == "yes":
        response = requests.get("https://swapi.dev/api/people/" + str(counter))

        if response.status_code == 200:
            data = response.json()

            filename = f"{data['name'].replace(' ', '_').replace('/', '_')}.json"
            with open(filename, 'w') as json_file:
                json.dump(data, json_file, indent=4)

            print("Character name: " + data["name"] + ", " + "Birth year: " + data['birth_year'] )

            conn = sqlite3.connect("star_wars.db")
            cursor = conn.cursor()

            cursor.execute(
                ''' 
                    CREATE TABLE IF NOT EXISTS characters (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        birth_year TEXT
                    )
                '''
            )

            cursor.execute('''INSERT INTO characters (name, birth_year) VALUES (?,?)''', (data["name"], data['birth_year']))

            conn.commit()
            conn.close()
            counter += 1

        else:
            print(f"Failed to retrieve data: {response.status_code}")
            break
    elif userInput == "no" :
        break
    else :
        print("Please type yes or no") 


