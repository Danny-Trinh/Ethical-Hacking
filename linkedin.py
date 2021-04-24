from linkedin_scraper import Person, actions
from selenium import webdriver
import os

driver = webdriver.Chrome()

email = "dtt574@utexas.edu"
password = os.environ.get('LinkedinPass')
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
person = Person("https://www.linkedin.com/in/reginaxchen/", driver=driver)
 