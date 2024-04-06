import cv2
import numpy as np

# Load the image
image = cv2.imread('img.jpg')
#cv2.imshow('same',image)
# Check if the image is loaded successfully
if image is None:
    print("Error: Unable to load the image.")
    exit()

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow('gray',gray)

# Apply bilateral filter to keep edges sharp and blur low frequency regions. It reduces noise.
blurred = cv2.bilateralFilter(gray,5,6,6)
#cv2.imshow('blurred',blurred)

# Threshold the blurred image to get the black boundaries
_, thresh = cv2.threshold(blurred, 175, 255, cv2.THRESH_BINARY)
#cv2.imshow('thresh',thresh)

# Find contours of the black boundaries basicallu object of interest is white part and blue is considered as black
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterate over each contour
for contour in contours:
    # Skip small contours
    if cv2.contourArea(contour) < 100:
        continue

    # Create a mask for the current contour
    mask = np.zeros_like(gray)
    cv2.drawContours(mask, [contour], 0, 255, -1)

    # Extract pixels within the contour
    masked_image = cv2.bitwise_and(image, image, mask=mask)

    # Calculate the average color within the contour
    average_color = np.mean(masked_image[mask == 255], axis=0).astype(int)

    # Change the color of pixels within the contour to the average color
    image[mask == 255] = average_color

# Display the result after applying fastNlMeanDenoising so that blue regions get blurred
result = cv2.fastNlMeansDenoisingColored(image, None, 20, 5, 15, 10)
cv2.imshow('Modified Image', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
