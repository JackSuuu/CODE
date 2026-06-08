
import textract

# Extract text from an image file using Textract
text = textract.process("image.png")

# Print the extracted text
print(text.decode())