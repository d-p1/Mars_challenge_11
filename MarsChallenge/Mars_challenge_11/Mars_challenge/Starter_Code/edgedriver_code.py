##because of technical difficulties with chrome, i attempted to do the assignment using edge.
##These are my notes, and attempt
##this file is not part of the assignment.
from msedge.selenium_tools import Edge, EdgeOptions
from bs4 import BeautifulSoup as soup

# Set the path to the Microsoft Edge WebDriver executable
edge_driver_path = r'C:\Users\msedgedriver.exe'

# Configure the Edge WebDriver options
options = EdgeOptions()
options.use_chromium = True  # Use Chromium-based Edge

# Create the WebDriver instance
browser = Edge(executable_path=edge_driver_path, options=options)

# Visit the desired URL
url = 'https://static.bc-edx.com/data/web/mars_news/index.html'
browser.get(url)

# For example, you can get the page source using BeautifulSoup
page_source = soup(browser.page_source, 'html.parser')

# Print the title as a check
print(page_source.title)

# Don't forget to close the browser when you're done
browser.quit()
