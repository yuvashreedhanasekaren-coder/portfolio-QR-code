import requests
from bs4 import BeautifulSoup
from config import PORTFOLIO_URL


def fetch_portfolio_content():
    response = requests.get(PORTFOLIO_URL, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.string.strip() if soup.title and soup.title.string else "No title"

    for element in soup(["script", "style", "noscript"]):
        element.decompose()

    text = soup.get_text(separator=" ", strip=True)

    return title, text


if __name__ == "__main__":
    title, text = fetch_portfolio_content()

    print("Portfolio Title:")
    print(title)

    print("\nPortfolio Content:")
    print(text[:1000])