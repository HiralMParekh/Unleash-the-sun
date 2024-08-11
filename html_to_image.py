from selenium import webdriver
from PIL import Image
import time

# Absolute path to your HTML file
html_file = 'file:///absolute/path/to/leaflet_map.html'

# Set up Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode
options.add_argument('--window-size=1200x800')  # Set window size
driver = webdriver.Chrome(options=options)

# Load the HTML file
driver.get(html_file)

# Give it some time to render
time.sleep(5)  # Increase if needed

# Save screenshot of the map
screenshot_path = 'map_image.png'
driver.save_screenshot(screenshot_path)

# Close the WebDriver
driver.quit()

# Open the screenshot with Pillow (optional, for verification)
image = Image.open(screenshot_path)
image.show()
