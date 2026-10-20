
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
You are a professional portfolio analyzer.

Analyze the portfolio content provided below.

IMPORTANT RULES:
1. Use ONLY the information explicitly available in the portfolio content.
2. Do NOT invent, assume, or add any details.
3. Do NOT repeat information.
4. Ignore navigation menus, buttons, links, and website labels.
5. Do NOT treat menu items as skills or work experience.
6. If any information is not available, write "Not specified".
7. Keep the analysis clear, accurate, and professional.

Portfolio Title:
{title}

Portfolio Content:
{text[:6000]}

Return the result in EXACTLY this format:

Professional Category:
<main professional field>

Technical Skills:
<technical skills explicitly mentioned in the portfolio>

Education:
<education details explicitly mentioned in the portfolio>

Projects:
<project names with a short description, only if available>

Professional Summary:
<accurate 2-3 sentence summary of the portfolio>

Do not add any extra headings or explanations.
"""


def analyze_with_ollama(title, text):
    prompt = create_analysis_prompt(title, text)

    response = requests.post(
        OLLAMA_URL,
        json={
    "model": AI_MODEL,
    "prompt": prompt,
    "stream": False,
    "options": {
        "temperature": 0.1
    }
},
       timeout=300
    )

    response.raise_for_status()

    return response.json()["response"]


if __name__ == "__main__":
    title, text = fetch_portfolio_content()

    print("Portfolio Title:")
    print(title)

    print("\nAI Analysis:")
    print(analyze_with_ollama(title, text))
