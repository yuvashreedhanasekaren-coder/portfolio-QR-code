
import os
import requests

from flask import Flask, render_template
from ai_analyzer import fetch_portfolio_content, analyze_with_ollama
from qr_generator import generate_qr_code

app = Flask(__name__)


@app.route("/")
def home():

    qr_file = os.path.join(app.root_path, "static", "portfolio_qr.png")

    # QR Code Generation
    try:
        if not os.path.exists(qr_file):
            generate_qr_code()
    except Exception:
        app.logger.exception("QR code generation failed")

    # Portfolio Content Extraction
    try:
        title, text = fetch_portfolio_content()

    except requests.RequestException:
        app.logger.exception("Portfolio fetching failed")

        return render_template(
            "index.html",
            title="Portfolio Unavailable",
            analysis="Unable to fetch portfolio content. Please check your internet connection or portfolio URL."
        )

    # AI Analysis
    try:
        analysis = analyze_with_ollama(title, text)

    except Exception:
        app.logger.exception("AI analysis failed")

        analysis = (
            "AI analysis is currently unavailable. "
            "Please make sure Ollama is running and the local AI model is installed."
        )

    return render_template(
        "index.html",
        title=title,
        analysis=analysis
    )


if __name__ == "__main__":
    app.run(debug=True)
