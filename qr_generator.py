import os
import qrcode

from config import PORTFOLIO_URL

def generate_qr_code():
    output_directory = "static"
    output_file = os.path.join(output_directory, "portfolio_qr.png")

    os.makedirs(output_directory, exist_ok=True)

    qr = qrcode.make(PORTFOLIO_URL)
    qr.save(output_file)

    return output_file

if __name__ == "__main__":
    generate_qr_code()