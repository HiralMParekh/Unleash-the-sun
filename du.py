import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

# Load the image
# image = cv2.imread('path_to_image.jpg')

# Read the image
image = cv2.imread('/content/drive/MyDrive/Colab Notebooks/pixelcheck.png')

# Check if the image was successfully loaded
if image is None:
    print("Error: Image file could not be loaded. Please check the path.")
else:
    # Convert the image from BGR (OpenCV format) to RGB (matplotlib format)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply GaussianBlur to reduce noise and improve contour detection
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply Canny edge detection to find edges in the image
edges = cv2.Canny(blurred, 50, 150)

# Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter and find the largest contour by area
contour_areas = [(cv2.contourArea(c), c) for c in contours]
largest_contour = max(contour_areas, key=lambda x: x[0])[1]
angle_degrees = 22.990099100827187
# Calculate the area of the largest contour
area = cv2.contourArea(largest_contour)
angle_radians = math.radians(angle_degrees)
cosine_value = math.cos(angle_radians)
scale=156543.03*cosine_value/2**20
meter_area=scale*area 
print("Area of the object:", meter_area)

# Draw the contour on the image to highlight the object
highlighted_image = image.copy()
cv2.drawContours(highlighted_image, [largest_contour], -1, (0, 255, 0), 2)
# print(highlighted_image)

# Display the original image with the highlighted object
plt.imshow(cv2.cvtColor(highlighted_image, cv2.COLOR_BGR2RGB))
plt.title('Highlighted Object')
plt.axis('off')
plt.show()