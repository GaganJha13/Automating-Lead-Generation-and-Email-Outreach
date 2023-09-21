import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# Set up the web driver (make sure the webdriver executable is in your PATH)
driver = webdriver.Chrome()

# URL of the Google Maps page
url = "https://www.google.com/maps/search/industry name+in+industry location" # type industry name and location here

# Open the webpage using the web driver
driver.get(url)

# Wait for the page to load (adjust the sleep duration as needed)
time.sleep(1)

# Part name
cafe_elements1 = driver.find_elements(By.CLASS_NAME, 'class name') # type class name here
cafe_names = [element.text for element in cafe_elements1]

# Part address
cafe_elements2 = driver.find_elements(By.CLASS_NAME, 'class name') # type class name here
cafe_address = [element.text if element.text else "" for element in cafe_elements2]

# Close the web driver
driver.quit()

# Create a list of dictionaries, each representing a cafe
cafe_data = []
for name, address in zip(cafe_names, cafe_address):
    cafe_data.append({"Names": name, "Address": address,"Email-Id":"sendermail@gmail.com"})

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(cafe_data)

# Save the data to a CSV file with each cafe's data on a separate line
df.to_csv('pagedata.csv', index=False)

print("Done")
