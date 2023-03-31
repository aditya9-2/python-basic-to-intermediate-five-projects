import cv2

# Configurable Parameters
source = "githubimage.jpg"
destination = "newimage2.png"

# Percent by which the image is resized
scale_percent = 50

image = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# cv2.imshow("title", image)

# Calculate the 50 percent of the original image
new_width = int(image.shape[1] * scale_percent / 100)
new_height = int(image.shape[0] * scale_percent / 100)

# Resize image
output = cv2.resize(image, (new_width, new_height))

cv2.imwrite(destination, output)
# cv2.waitKey(0)