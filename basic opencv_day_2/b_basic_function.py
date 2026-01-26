import cv2

## 1. convert color image to grayscale

# img = cv2.imread("resources/lena.png")
# cv2.imshow("Original Image", img)
# img_gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print(img_gray.shape)
# print(img.shape)
# cv2.imshow("GrayScale image", img_gray)
# cv2.waitKey(0)





### 2. convert  to blur image
# img = cv2.imread("resources/lena.png")
# img_gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img_blur = cv2.GaussianBlur(img_gray, (7,7), 0)
# cv2.imshow("GrayScale image", img_gray)
# cv2.imshow("Blurred Image", img_blur)
# cv2.waitKey(0)




### 3. Convert to canny image edge detection algorithm 

img = cv2.imread("resources/lena.png")
img_gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7,7), 0)
img_canny = cv2.Canny(img_blur, 100,100)
cv2.imshow("GrayScale image", img_gray)
cv2.imshow("Blurred Image", img_blur)
cv2.imshow("Canny Image", img_canny)
cv2.waitKey(0)



