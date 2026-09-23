from flask import Flask, render_template
from ai_analyzer import fetch_portfolio_content, analyze_with_ollama
from qr_generator import generate_qr_code

app = Flask(__name__)


@app.route("/")
def home():
    generate_qr_code()

    title, text = fetch_portfolio_content()

    analysis = "AI analysis will be available after the local model is installed."

    return render_template(
        "index.html",
        title=title,
        analysis=analysis
    )


if __name__ == "__main__":
    app.run(debug=True)