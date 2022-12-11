# this is a module = file
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# python3 built-in modules
import csv
from time import sleep 

# See https://pypi.org/project/selenium/

browser = object

def get_csv_data(filename):

    data = [] # list(array) of dicts(key:value)
    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def simple_test():
    browser.get('http://selenium.dev/')

def google_search(search):
    browser.get('https://www.google.com/')
    assert 'Google' in browser.title
    elem = browser.find_element(By.NAME, 'q')  # Find the search box
    elem.send_keys(search + Keys.RETURN)       # type, then return

# __name__ is built-in variable contains the running module name
# Only run this block if this file was run in the terminal
#    python src/main.py
if __name__ == "__main__":

    # this is a module level environment
    browser = webdriver.Firefox()

    data = get_csv_data('data/form_data.csv')

    for search in data:
        google_search(search['Search']) 
        sleep(5)
    
    sleep(5)
    
browser.quit()


