from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('./chromedriver')
driver.get('http://127.0.0.1:5000/edit')

sleep(1)

task = driver.find_element_by_xpath('/html/body/div/form/div/input')
task.send_keys('Test')

add = driver.find_element_by_xpath('/html/body/div/form/button')
add.click()

sleep(1)

update = driver.find_element_by_xpath('/html/body/div/div/a[1]')
update.click()

sleep(1)

delete = driver.find_element_by_xpath('/html/body/div/div/a[2]')
delete.click()

sleep(1)
driver.close()
driver.quit()

list = webdriver.Chrome('./chromedriver')
list.get('http://127.0.0.1:5000/')

sleep(1)
list.close()
list.quit()
