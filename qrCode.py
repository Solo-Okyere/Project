import qrcode
from PIL import Image

# 1. Your hosted Valentine page URL
valentine_url = "https://favorite-assets--okyeresolomon.replit.app/"

# 2. Create QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(valentine_url)
qr.make(fit=True)

# 3. Generate the QR code image
img = qr.make_image(fill_color="red", back_color="#05070a")

# 4. Save the QR code
img.save("valentine_qr.png")
print("QR code saved as valentine_qr.png")

# 5. Display the QR code immediately
img.show()  # <-- this opens the QR code image in your default image viewer
