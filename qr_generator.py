import qrcode
from config import PORTFOLIO_URL

def generate_qr_code():
    qr = qrcode.make(PORTFOLIO_URL)
    qr.save("static/portfolio_qr.png")

if __name__ == "__main__":
    generate_qr_code()