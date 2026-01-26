import cv2

### 1. Resizing Images

img = cv2.imread("resources/lena.png")
# print(img.shape)
# resized_img = cv2.resize(img, (300,200))
# print(resized_img.shape)
# cv2.imshow("output",img)
# cv2.imshow("resized_output", resized_img)
# cv2.waitKey(0)



### Cropping Image


crop_img = img[0:200, 200:500]
cv2.imshow("output", img)
cv2.imshow("crop_output", crop_img)
cv2.waitKey(0)