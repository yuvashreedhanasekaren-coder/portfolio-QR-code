import requests
from bs4 import BeautifulSoup

from config import PORTFOLIO_URL, OLLAMA_URL, AI_MODEL


def fetch_portfolio_content():
    response = requests.get(PORTFOLIO_URL, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.string.strip() if soup.title and soup.title.string else "No title"

    for element in soup(["script", "style", "noscript"]):
        element.decompose()

    text = soup.get_text(separator=" ", strip=True)

    return title, text


def create_analysis_prompt(title, text):
    return f"""
Analyze the following portfolio website.

Portfolio title:
{title}

Portfolio content:
{text[:6000]}

Return the analysis in exactly this format:

Category:
<main professional category>

Skills:
<important technical skills separated by commas>

Summary:
<a short 2-3 sentence summary of the portfolio>
"""


def analyze_with_ollama(title, text):
    prompt = create_analysis_prompt(title, text)

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": AI_MODEL,
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )

    response.raise_for_status()

    return response.json()["response"]


if __name__ == "__main__":
    title, text = fetch_portfolio_content()

    print("Portfolio Title:")
    print(title)

    print("\nPortfolio Content:")
    print(text[:1000])

    print("\nAI Analysis:")
    print(analyze_with_ollama(title, text))