import cv2
import numpy as np

image = cv2.imread('images\\clean3.jpg')

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

browns = []
for row in hsv_image:
    new_row = []
    for column in row:
        hue = column[0]
        saturation = column[1]
        brightness = column[2]
        if (brightness < 20) or (saturation > 20):
            new_row.append(0)
        else:
            new_row.append(255)
    browns.append(new_row)

browns = np.array(browns).astype(np.uint8)
comparison = np.hstack((cv2.resize(image, (0,0), None, .25, .25), cv2.resize(cv2.cvtColor(browns, cv2.COLOR_GRAY2BGR), (0,0), None, .25, .25)))

cv2.imwrite('clean3_browns.png', browns)
cv2.imwrite('clean3_comparison.png', comparison)

cv2.imshow('comparison', comparison)
cv2.waitKey(0)