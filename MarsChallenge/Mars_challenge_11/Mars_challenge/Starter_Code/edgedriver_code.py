##because of technical difficulties with chrome, I attempted to do the assignment using edge.
##These are my notes and attempt.
##This file is not part of the assignment. But can help if attempting this challenge :)
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from selenium import webdriver


# Set the path to the Microsoft Edge WebDriver executable
edge_driver_path = r'C:\Users\msedgedriver.exe'
executable_path = {'executable_path': edge_driver_path}

# Open Edge Browser 

browser = Browser('edge')
