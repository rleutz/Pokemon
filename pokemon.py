# Import required modules
from textwrap import indent
import requests, random, json

# Set API URL parts
base_url = 'https://pokeapi.co/api/v2/'
api = 'pokemon'

# Set parameters for rest call
params = {'limit': 20, 'offset': 0}

session = requests.Session()

# Create a list to store results
results = []

# Continue making REST API calls until complete
while True:
    # Display status
    print(f"Getting list {params['offset']} through {params['limit']+params['offset']}")

    # Build URL for REST connection
    url = f"{base_url}{api}"

    # Make reston connection
    response = session.get(url, params=params)

    # Convert to JSON
    json_out = response.json()

    # Add the response json to the results list
    results.extend(json_out['results'])

    # Check if there is a key named next in the JSON output.
    # If not, then you have no more pages, so exit the loop.
    if not json_out['next']:
        break

    # Configure the params for the next set of 20 results
    params['offset'] += params['limit']

# Let's get a random pokemon
random_pokemon = random.randint(1,len(results))

print(random_pokemon)

# Now let's get the pokemon name of the randomly selected position
poke_name = results[random_pokemon]["name"]

url = results[random_pokemon]["url"]

# Now let's get all of the random pokemon's abilities
response = session.get(url)

print(json.dumps(response.json()["abilities"], indent=2))


