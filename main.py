import numpy as np
import cv2
import matplotlib.pyplot as plt
import pytesseract
from PIL import Image



# img_ori = cv2.imread("9.jpg")
img_ori = Image.open("10.png")
result = pytesseract.image_to_string(img_ori, lang='kor')
print(result)


