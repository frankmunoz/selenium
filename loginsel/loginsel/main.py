from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


# Test Ekaa
username = "franciscomunoz"
password = "helloween"
url = "http://localhost:8001/admin"


'''
# KoBo Producción
username = "Francisco_Munoz"
password = "Simple,21"
url = "https://frm.mtr.pnud.org.co/admin"
'''


driver = webdriver.Chrome("/Users/franciscomunoz/Documents/Development/selenium/drivers/chromedriver")
driver.get(url)

'''
# SSL Issue
driver.find_element_by_id("details-button").click()
driver.find_element_by_id("proceed-link").click()
'''

driver.find_element_by_name("username").send_keys(username)
driver.find_element_by_name("password").send_keys(password)

driver.find_element_by_css_selector("input[type=\"submit\" i]").click()
print("Logged in successfully")


addUser = '/auth/user/add/'
driver.get(url + addUser)


# Crear usuario
for i in range(36, 66):	  
	add_username = "Antioquia" + str(i)
	add_password = "dinatablet" + str(i)

	driver.find_element_by_name("username").send_keys(add_username)
	driver.find_element_by_name("password1").send_keys(add_password)
	driver.find_element_by_name("password2").send_keys(add_password)
	driver.find_element_by_name("_addanother").click()

for i in range(1, 66):	  
	add_username = "Narino" + str(i)
	add_password = "dinatablet" + str(i)

	driver.find_element_by_name("username").send_keys(add_username)
	driver.find_element_by_name("password1").send_keys(add_password)
	driver.find_element_by_name("password2").send_keys(add_password)
	driver.find_element_by_name("_addanother").click()


#	driver.find_element_by_name("_save").click()
'''
	group = driver.find_element_by_xpath("//*[@title='Cash for data']")
	actionChains = ActionChains(driver)
	actionChains.double_click(group).perform()
'''

#	driver.find_element_by_id("id_groups_input").send_keys('Cash for data')

#driver.find_element_by_name("_addanother").click()s


