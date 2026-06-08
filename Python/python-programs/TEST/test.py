import os
import pytesseract
from PIL import Image

current_dir = os.getcwd()
print(f"The current directory: {current_dir}")

file_path = current_dir + '/Pic.png'

# with open(file_path, 'r') as FILE:
#     line_1 = FILE.readline()
#     print(line_1)

# Load the image
img = Image.open(file_path)

# Convert the image to grayscale
img = img.convert('L')

# Use pytesseract to recognize text in the image
text = pytesseract.image_to_string(img)

# Print the recognized text
print(text)



