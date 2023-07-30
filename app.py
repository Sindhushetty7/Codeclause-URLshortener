import requests

def shorten_url(url):
    try:
        response = requests.get(f'http://tinyurl.com/api-create.php?url={url}')
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print("Error occurred while shortening the URL:", e)
        return None

if __name__ == "__main__":
    url_to_shorten = input("Enter URL to shorten: ")
    shortened_url = shorten_url(url_to_shorten)
    if shortened_url:
        print("Shortened URL:", shortened_url)
    else:
        print("URL shortening failed.")
