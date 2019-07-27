from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import serial
import time

ArduinoSerial=serial.Serial('COM4',9600)

def led_yellow():
        ArduinoSerial.write(b'1')

def led_blue():
        ArduinoSerial.write(b'0')        

time.sleep(2)
led_yellow()
chromedriver="C:/Users/asus/Downloads/chromedriver_win32 (2)/chromedriver"
driver=webdriver.Chrome(chromedriver)
driver.get("https://www.youtube.com/feed/trending")
print("Trending 1: ")
try:
    title1=driver.find_element_by_css_selector('#video-title')
    print(title1.text)
except:
    print("The title contains characters that are not supported")
views1=driver.find_element_by_css_selector('#metadata-line > span:nth-child(1)')
print("Views count: ",(views1.text))
up_t1=driver.find_element_by_css_selector('#metadata-line > span:nth-child(2)')
print("Time since now: ",(up_t1.text))

#Trending loop
for i in range(1,5):
    led_yellow()
    tmp=str(i+1)
    title="#grid-container > ytd-video-renderer:nth-child("+tmp+")"
    wait=WebDriverWait(driver,30)
    link=wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,title)))
    #print(link.text)
    link.click()
    
    new_link=driver.current_url
    #print(new_second_link)
    driver.get(new_link)

    print("\n")
    nu=str(i+1)
    tr="Trending "+nu+":"
    print(tr)
    wait=WebDriverWait(driver,30)
    try:
        title2=wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,'h1.ytd-video-primary-info-renderer yt-formatted-string')))
        print("Title : " + title2.text)
    except:
        print("The title contains characters that are not supported")
    count2=wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,'#count > yt-view-count-renderer > span.view-count.style-scope.yt-view-count-renderer')))
    print("Views Count :" + count2.text)
    time2=wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,'#upload-info > span')))
    print("Time since now :" + time2.text)

    driver.execute_script("window.history.go(-1)")

led_blue()
