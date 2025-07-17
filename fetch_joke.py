import requests

def fetch_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        setup = data.get('setup')
        punchline = data.get('punchline')
        if setup and punchline:
            print("Here's a random joke for you:")
            print(f"\n{setup}\n{punchline}")
        else:
            print("Received an unexpected response from the API.")
    except requests.RequestException as e:
        print(f"Failed to fetch joke: {e}")

def main():
    fetch_joke()

if __name__ == "__main__":
    main() 