         # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         #█░██░███░▄▄█░▄▄▀█░▄▄▀█▀▄▄▀█░██░█░▄▄▀██▄████░▄▀██▄██░▄▀███▄░▄█░████░▄▄▀█▄░▄
         #█░██░███░▄▄█░██░█░██░█░██░█░██░█░▀▀▄██░▄███░█░██░▄█░█░████░██░▄▄░█░▀▀░██░█ <<< u/ennouri did that
         #██▄▄▄███▄▄▄█▄██▄█▄██▄██▄▄███▄▄▄█▄█▄▄█▄▄▄███▄▄██▄▄▄█▄▄█████▄██▄██▄█▄██▄██▄█
         #▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

#hope u enjoyed this little script i did, to support me; u can donate:
# BITCOIN: bc1qne5um5g8yw87jvet20yt8yvkkkzxjhazmvavda
# DOGECOIN (to the moon btw): DSAbPC7hPmYWUuAPffRvzTWEDDnTab9C42
# LITECOIN:LRHnRj92ngfC4Fo2R2ZArNSTZ9qkjDmQm9

from selenium import webdriver
driver= webdriver.Chrome("chromedriver.exe")
TARGET = 'replace me i am usless' #replace the text 'replace me i am useless" with the target email
driver.get('https://www.crosswalk.com/newsletters/')

user_input = driver.find_element_by_xpath('/html/body/div[3]/div[4]/div/div[1]/div/div/div/div/div/div/div[1]/input[2]')
user_input.send_keys(TARGET)

import time 
time.sleep(2)

for i in range(2,16):
    btn = driver.find_element_by_xpath(f'/html/body/div[3]/div[4]/div/div[1]/div/div/div/div/div/div/div[6]/div[1]/div[1]/div[{i}]/input')
    btn.click()

signup = driver.find_element_by_xpath('/html/body/div[3]/div[4]/div/div[1]/div/div/div/div/div/div/div[1]/a')
signup.click()

