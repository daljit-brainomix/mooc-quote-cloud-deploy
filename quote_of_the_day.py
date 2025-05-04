import requests


def get_quote_of_the_day():
    url = "https://zenquotes.io/api/today"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()

        if data and isinstance(data, list):
            quote = data[0].get("q", "No quote found.")
            author = data[0].get("a", "Unknown")
            print(f'"{quote}"\n  — {author}')
        else:
            print("Unexpected response format.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching quote: {e}")


if __name__ == "__main__":
    get_quote_of_the_day()
