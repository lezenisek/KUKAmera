import cv2
from skimage.morphology import skeletonize
import matplotlib.pyplot as plt
import pathlib
from skimage import io

img = cv2.imread('../bilder/smiley.png')
if img is None:
    raise FileNotFoundError("PNG file not found")

gray = cv2.cvtColor(
    img, cv2.COLOR_BGR2GRAY
)

# 3. Bild leicht glätten
blurred = cv2.GaussianBlur(
    gray, (5, 5), 0
)



# 4. Binärisieren
# Zeichnung = weiß (255)
# Hintergrund = schwarz (0)
_, binary = cv2.threshold(
    blurred,
    0,
    255,
    cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
)

# 5. Kleine Störungen entfernen
kernel = cv2.getStructuringElement(
    cv2.MORPH_ELLIPSE, (3, 3)
)



binary = cv2.morphologyEx(
    binary,
    cv2.MORPH_OPEN,
    kernel
)

skeleton = skeletonize(binary)


io.imsave('../bilder/skeleton.png', skeleton)

