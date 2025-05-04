from flask import Flask
import requests

PORT = 5000
app = Flask(__name__)


@app.route("/")
def quote_of_the_day():
    try:
        response = requests.get("https://zenquotes.io/api/today")
        response.raise_for_status()
        data = response.json()

        if data and isinstance(data, list):
            quote = data[0].get("q", "No quote found.")
            author = data[0].get("a", "Unknown")
            return f'<h1>"{quote}"</h1><p>— {author}</p>'
        else:
            return "Unexpected response format.", 500
    except requests.exceptions.RequestException as e:
        return f"Error fetching quote: {e}", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
