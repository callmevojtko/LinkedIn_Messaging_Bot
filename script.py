import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=options)

#enter the link 
driver.get("https://www.linkedin.com/")

# hitting signin 
signin = driver.find_element_by_xpath("/html/body/nav/a[3]")
signin.click()

#waits for some time 
driver.implicitly_wait(40)

username = driver.find_element_by_xpath('//*[@id="username"]')
# enter phone/email
username.send_keys("")

password = driver.find_element_by_xpath('//*[@id="password"]')
# enter password
password.send_keys("")

#waits for some time 
driver.implicitly_wait(30)

# sigin button click
sign_in = driver.find_element_by_xpath('//*[@id="app__container"]/main/div[2]/form/div[3]/button')
sign_in.click()

#waits for some time 
driver.implicitly_wait(30)


# to close default popup of message box
messagec = driver.find_element_by_class_name("msg-overlay-bubble-header")
messagec.click()

# go to recruiter tab
driver.get("https://www.linkedin.com/talent/home")

# waits for some time
driver.implicitly_wait(30)

# scroll to mynetwork
driver.execute_script("window.scrollTo(0,500)")

# click on project
connect = driver.find_element_by_class_name("project-lockup-title__item t-bold")
connect.click()

driver.implicitly_wait(10)

# click uncontacted
connectuncon = driver.find_element_by_class_name("hiring-pipeline__link-name")
connectuncon.click()

# click send message
connecthit = driver.find_element_by_xpath('//*[@id="ember9258"]/li-icon/svg')
connecthit.click()

# click template
template = driver.find_element_by_class_name("artdeco-typeahead__input ts-common-typeahead__input")
template.click()

# click desired template
addTemplate = driver.find_element_by_name('West Creek - remote front-end')
addTemplate.click()

# hitting done button
done = driver.find_element_by_xpath('//*[@id="ember13537"]/div/button/span[2]')
done.click()

driver.implicitly_wait(20)
driver.quit()
