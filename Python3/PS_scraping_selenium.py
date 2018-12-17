from bs4 import BeautifulSoup
import requests
import re
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.common.exceptions import TimeoutException
URL = 'https://shopping.thinkwithgoogle.com'
EXAMPLES = ["Demonstrate unexpected use-case",
            "Demonstrate google search",
            "Demonstrate search on thinkwithgoogle",
            "Demonstrate search on WebDriverWait",
            "Demonstrate search on thinkwithgoogle search result",
            "Download and extract additional data",
            "Demonstrate maximizing screen",
            "Demonstrate mouse actions for Chrome",
            "Demonstrate navigation"]

# remove parser, content 
def run(input, URL = '', parser = 'html.parser', content = ''):
    if(input == 0):
        content = requests.get(URL)
        soup = BeautifulSoup(content.text,'html.parser')
        print(soup.prettify())            # Print row with HTML formatting
    elif(input == 1):
        driver = webdriver.Safari()             # Google Search
        driver.get("https://www.google.com")
        search = driver.find_element_by_name("q")
        search.send_keys("Selenium")
        search.submit()
    elif(input == 2):
        browser = webdriver.Safari()             # thinkwithgooglesearch
        browser.get(URL)
        time.sleep(5)
        search = browser.find_elements_by_id('subjectInput')[1]
        search.send_keys('Google Pixel 3')
        time.sleep(5)
        search.send_keys(Keys.RETURN)
    elif(input == 3):
        browser = webdriver.Safari()             # thinkwithgooglesearch
        browser.maximize_window()                # Required for the input tag visibility
        browser.get('https://trends.google.com/trends/')
        try: # proceed if element is found within 3 seconds otherwise raise TimeoutException
            element = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.ID, 'input-254')))
        except TimeoutException:
            print("Loading took too much time!")
        search = browser.find_elements(By.ID,'input-254')[0]
        search.send_keys('Google Pixel 3')
    elif(input == 4):
        browser = webdriver.Safari()    # thinkwithgooglesearch
        browser.get(URL)                # with visibility search
        time.sleep(2)
        search = returnVisibleElement(browser.find_elements_by_id('subjectInput'))
        search.send_keys('Google Pixel 3')
        time.sleep(2)
        search.send_keys(Keys.ENTER)
    elif(input == 5):
        browser = webdriver.Safari()    # thinkwithgooglesearch
        browser.maximize_window()       # Required for the button visibility
        browser.get(URL)                # with visibility search
        time.sleep(2)
        search = returnVisibleElement(browser.find_elements_by_id('subjectInput'))
        search.send_keys('Google Pixel 3')
        time.sleep(2)
        search.send_keys(Keys.ENTER)
        time.sleep(2)
        browser.find_element_by_class_name('si-button-data download-all').click()
        data = browser.find_element_by_class_name('content content-breakpoint-gt-md')
        dataList = data.find_elements_by_tag_name('li')
        for item in dataList:
            text = item.text
            print(text)
    elif(input == 6):
        browser = webdriver.Safari()    # thinkwithgooglesearch
        browser.maximize_window()       # Required for the button visibility
        browser.get(URL)                # with visibility search
        time.sleep(2)
        element_to_hover_over = returnVisibleElement(browser.find_elements_by_xpath("//i[@class='material-icons'][contains(./text(),'help')]"))
    elif(input == 7):
        browser = webdriver.Chrome()    # thinkwithgooglesearch
        browser.maximize_window()       # Required for the button visibility
        browser.get(URL)                # with visibility search
        time.sleep(2)
        element_to_hover_over = returnVisibleElement(browser.find_elements_by_xpath("//i[@class='material-icons'][contains(./text(),'help')]"))
##      ActionChains are not supported in safari but will work on other browser
##      https://github.com/seleniumhq/selenium-google-code-issue-archive/issues/4136
        ActionChains(browser).click(element_to_hover_over).perform()
        TouchActions(browser).long_press(element_to_hover_over).perform()
    elif(input == 8):
        browser = webdriver.Safari()    # thinkwithgooglesearch
        browser.maximize_window()       # Required for the button visibility
        browser.get(URL)                # with visibility search
        time.sleep(2)
        search = returnVisibleElement(browser.find_elements_by_id('subjectInput'))
        search.send_keys('Google Pixel 3')
        time.sleep(2)
        search.send_keys(Keys.ENTER)
        time.sleep(2)
        data = browser.find_element_by_class_name('content content-breakpoint-gt-md')
        dataList = data.find_elements_by_tag_name('li')
        for item in dataList:
            text = item.text
            print(text)
        browser.back()
        

    print('\n' * 5) # For convenient visual


def returnVisibleElement(listOfInputElements):
    for element in listOfInputElements:
        if element.is_displayed():
            return element    

def printSelection():
    print('Press:')
    for i in range(0, len(EXAMPLES)):
        print('',i,'to',EXAMPLES[i], sep = ' ')

if __name__ == '__main__':
    while(True):
        printSelection()
        choice = input('Enter choice: ')
        try:
            choice = int(choice)
        except ValueError:
            print('Invalid input, stop program')
            break
        if(choice not in range(0,9)):
            print('Invalid input, stop program')
            break
        run(int(choice), URL)
