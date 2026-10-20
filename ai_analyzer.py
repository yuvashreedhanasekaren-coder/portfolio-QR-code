
import requests
from bs4 import BeautifulSoup

from config import PORTFOLIO_URL, OLLAMA_URL, AI_MODEL

def fetch_portfolio_content():
    response = requests.get(PORTFOLIO_URL, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.string.strip() if soup.title and soup.title.string else "No title"

    sections = {
        "About": "about",
        "Education": "education",
        "Skills": "skills",
        "Experience": "experience",
        "Projects": "projects",
        "Certificates": "certificates"
    }

    extracted_content = []

    for section_name, section_id in sections.items():
        section = soup.find(id=section_id)

        if section:
            section_text = section.get_text(separator=" ", strip=True)
            extracted_content.append(
                f"{section_name}:\n{section_text}"
            )

    text = "\n\n".join(extracted_content)

    return title, text


def create_analysis_prompt(title, text):
    return f"""
You are an accurate and professional portfolio analyzer.

Analyze the portfolio content using ONLY the information provided.

STRICT RULES:
1. Never invent or assume information.
2. Ignore navigation menus, buttons, filters, links, and labels such as "My Work", "View Document", "All", and "Discover my projects by category".
3. Do not include internship names or project names as technical skills.
4. Do not duplicate education qualifications.
5. Include only actual project names and their descriptions.
6. Do not repeat information.
7. If information is missing, write "Not specified".
8. Write a professional summary using only facts from the About, Skills, Education, and Experience sections.
9. Do not claim skills or abilities that are not explicitly mentioned.

Portfolio Title:
{title}

Portfolio Content:
{text[:6000]}

Return the analysis in EXACTLY this format:

Professional Category:
<main professional field>

Technical Skills:
<comma-separated technical skills>

Education:
<qualification, institution, and other available details>

Projects:
<List actual project names with short descriptions. Exclude buttons, filters, and website labels.>

Professional Summary:
<2-3 factual sentences summarizing the person's background, interests, skills, and current learning focus.>

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
