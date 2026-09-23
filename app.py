from ai_analyzer import fetch_portfolio_content, analyze_with_ollama
from qr_generator import generate_qr_code


def run_application():
    print("Starting Portfolio QR Generator...")

    print("\nGenerating QR code...")
    generate_qr_code()
    print("QR code generated successfully.")

    print("\nFetching portfolio content...")
    title, text = fetch_portfolio_content()
    print(f"Portfolio Title: {title}")

    print("\nAnalyzing portfolio with local AI...")
    analysis = analyze_with_ollama(title, text)

    print("\n===== AI PORTFOLIO ANALYSIS =====")
    print(analysis)
    print("=================================")


if __name__ == "__main__":
    run_application()