import cv2
import pytesseract
import platform


if platform.system() == "Windows":
    print("El script se está ejecutando en Windows.")
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # your path may be different

else:
    print("El script se está ejecutando en un sistema operativo diferente a Windows.")
    # Establece la ubicación del ejecutable de Tesseract
    pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

def extract_text_from_image(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding to convert the image to black and white
    _, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
    # Use pytesseract to perform OCR on the image
    text = pytesseract.image_to_string(binary_image)
    
    return text
