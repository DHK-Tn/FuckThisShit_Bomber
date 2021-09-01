from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time
import os


class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

os.system("clear")
def banner():
    print(bcolors.GREEN + '+[+[+[ FuckThisSh!t Bomber ]+]+]+')
    print(bcolors.GREEN + '+[+[+[ made with Love      ]+]+]+')
    

print(bcolors.GREEN + " __      __.__            __                              __________              ___.     ") 
print(bcolors.GREEN + "/  \    /  \  |__ _____ _/  |_  ___________  ______ ______\______   \ ____   _____\_ |__   ")
print(bcolors.GREEN + "\   \/\/   /  |  \\__  \\   __\/  ___/\__  \ \____ \\____ \|    |  _//  _ \ /     \| __ \  ")
print(bcolors.GREEN + " \        /|   Y  \/ __ \|  |  \___ \  / __ \|  |_> >  |_> >    |   (  <_> )  Y Y  \ \_\ \ ")
print(bcolors.GREEN + "    _/\  / |___|  (____  /__| /____  >(____  /   __/|   __/|______  /\____/|__|_|  /___  / ")
print(bcolors.GREEN + "       \/       \/     \/          \/      \/|__|   |__|          \/             \/    \/  ")

print(banner())
# contact name can also be the name of a group
target=input('enter the contact name: ')
n=int(input('enter the number of messages you want to send: '))
string=input('enter the message you want to send: ')
# path = Path of your chromedriver file
driver = webdriver.Chrome('<path>')
driver.get("https://web.whatsapp.com/")
# wait for 6 seconds for whatsapp web to load and for you to login
wait = WebDriverWait(driver, 600)
# Check for the contact name in the title attribute of the span on the given page
x_arg = '//span[contains(@title,\"' + target + '\")]'
group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg))) 
# if the contact is found in the title attribute then it will select it and open the chats
group_title.click()
# Send the message for the number of times you have specified
for i in range(n):
    # select the send button which it searches using the CSS attribute
    element=driver.find_element_by_css_selector("div[data-tab='1']")
    element.send_keys(string+Keys.ENTER)
