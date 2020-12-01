try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    # text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    value = Image.open(filename)
    text = pytesseract.image_to_string(value, config='')
    # text = pytesseract.image_to_string(new_image, config='--psm 11')
    return text  # Then we will print the text in the image
