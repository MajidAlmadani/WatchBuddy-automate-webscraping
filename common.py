import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from telegram.ext import Application,CommandHandler,MessageHandler,ContextTypes,Updater, filters
from telegram import Update
from typing import Final

def reading_input_search(choice_type):
    input_value = f"Enter the searching {choice_type}: "
    search_input = input(input_value)
    return search_input

def reading_num_season(num_season):
    input_value = f"There is {num_season} Seasons\nEnter the number of Season to download: "
    while True:
        search_input = input(input_value)
        if search_input.isdigit():
            search_input = int(search_input)
            if( 1 <= search_input <= num_season): return search_input
        else:
            print("There is no Season with this number/character, Please enter again.")
            search_input = input(input_value)

def wait_click_XPATH(driver,XPATH):
    WebDriverWait(driver,20).until(visibility_of_element_located((By.XPATH, XPATH)))
    driver.find_element(By.XPATH,XPATH).click()
    return  

def wait_get_XPATH(driver,XPATH):
    WebDriverWait(driver,20).until(visibility_of_element_located((By.XPATH, XPATH)))
    link = driver.find_element(By.XPATH,XPATH).get_attribute('href')
    driver.get(link)
    return

def wait_find_XPATH(driver,XPATH):
    WebDriverWait(driver,20).until(visibility_of_element_located((By.XPATH, XPATH)))
    element = driver.find_element(By.XPATH,XPATH)
    return element

def wait_finds_XPATH(driver,XPATH):
    WebDriverWait(driver,20).until(visibility_of_element_located((By.XPATH, XPATH)))
    elements = driver.find_elements(By.XPATH,XPATH)
    return elements