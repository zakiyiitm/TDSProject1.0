import pytesseract
from PIL import Image
import re

# Path to Tesseract executable (adjust the path if necessary)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open the image containing the credit card number
image_path = '/data/credit_card.png'
image = Image.open(image_path)

# Use Tesseract to extract text from the image
extracted_text = pytesseract.image_to_string(image)

# Use a regular expression to find the credit card number (16 digits)
card_number = re.search(r'\d{4}\s*\d{4}\s*\d{4}\s*\d{4}', extracted_text)

if card_number:
    # Remove spaces and write the card number to /data/credit-card.txt
    clean_card_number = card_number.group().replace(' ', '')
    with open('/data/credit-card.txt', 'w') as file:
        file.write(clean_card_number)
else:
    print("No valid credit card number found in the image.")
