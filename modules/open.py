#### preinstalled python dependancies
import webbrowser
from time import sleep
import random
from datetime import datetime

### pip installed dependancies
# https://pypi.org/project/webdriver-manager/
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as coptions
from selenium.webdriver.firefox.options import Options as foptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd

### user created dependancies
from config import login, selenium_browser


def open_url(url):
    if 'http://' not in url:
        url = 'http://' + url
    webbrowser.get().open_new_tab(url)

def auto_login(name):
    found = False
    for website in login:
        if name.lower() in website['website'].lower():
            found = True
            #print(f"found {name} url is {website['website']}")
            try:
                if selenium_browser == 'chrome':
                    chrome_options = coptions()
                    chrome_options.add_experimental_option("detach", True)
                    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
                elif selenium_browser == 'firefox':
                    #firefox_options = foptions()
                    #firefox_options.add_experimental_option("detach", True)
                    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
                driver.get(website['website'])
                # wait for website to open
                sleep(4)
                for command in website['selenium_commands']:
                    if command['type'] == 'input':
                        input_field = driver.find_element_by_xpath(command['xpath'])
                        input_field.send_keys(website[command['input_variable']])
                    elif command['type'] == 'button':
                        button = driver.find_element_by_xpath(command['xpath'])
                        button.click()
                #driver.close()
            except:
                found = 'Error'
    return found


# file should contain the path to the file as well as the name.
def open_xls(file):
    df = pd.read_excel(file)
    return df


def add_row_xls(df, new_row):
    #new_row = {'Done?': False, 'Description':'Do things.', 'Date Added':datetime.now()}
    df.append(new_row, ignore_index=True)
    return df


def save_xls(df, file):
    try:
        writer = pd.ExcelWriter(file)
        df.to_excel(writer)
        writer.save()
        return f'Saved file {file}'
    except:
        return f'Failed to write data to file {file}'

#df = open_xls('./spreadsheets/todo.xlsx')
#new_row = {'Done?': False, 'Description':'Do things.', 'Date Added':datetime.now()}
#add_row_xls(df, new_row)