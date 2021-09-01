from selenium import webdriver


#make sure you have selenium library if not, type in cmd: pip install selenium
#this will install selenium
path=input("Enter WebDriver Path for linux or windows ")
driver =  webdriver.Chrome(path)

driver.get("https://web.whatsapp.com/")


print("Login now...\n")

name = input("Enter the WP name:(victim)")
count = int(input("Count: "))
msg = input("Enter The Message: ")


user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msgBox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]')

for i in range(count):
    msgBox.send_keys(msg)
    sendButton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    sendButton.click()


print("Mission Successful")
print(f"{count} messages were sent to {name}")
