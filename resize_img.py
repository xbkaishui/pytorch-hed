import cv2
from loguru import logger 

image = cv2.imread('./images/12_full.jpg')
logger.info("image shape {}", image.shape)

height, width, channel = image.shape

# size_decrease = (480, 320)
size_decrease = (int(width/2), int(height/2))
img_decrease = cv2.resize(image, size_decrease, interpolation=cv2.INTER_CUBIC)
cv2.imwrite('./images/12_full_2.jpg', img_decrease)