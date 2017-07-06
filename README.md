# Image2Word
transfer image to characters


brew install tesseract
pip install pytesseract
try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
# lang 指定中文简体
text = pytesseract.image_to_string(Image.open('dufu-denggao1.jpeg'), lang='chi_sim')
print(text)
