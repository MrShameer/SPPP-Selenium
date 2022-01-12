import os, selenium, time, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

### SET WHAR BUTTON YOU WANT TO CLICK, I.E, I WANT TO CLICK 4 OR 5
BUTTON = [4,5]

### INSERT YOUR MATRIC NUMBER
MATRIC = 'A123456'

### INSERT YOUR PASSWORD
PASSWORD = 'password123'

### SET THE PATH TO YOUR CHROMEDRIVER. USE YOUR OWN PATH.
CHROMEDRIVER_PATH = 'E:\\Python\\Sppp Selenium\\chromedriver.exe'

driver = webdriver.Chrome(CHROMEDRIVER_PATH)
driver.get('https://appsmu.ukm.my/sppp/penilaiankursus')

try:
	x=driver.find_element_by_name("username")
	x.send_keys(MATRIC)
	x.send_keys(Keys.ENTER)

	x=driver.find_element_by_name("password")
	x.send_keys(PASSWORD)
	x.send_keys(Keys.ENTER)


	### IF YOU HAVE A SLOW LINE INCREASE THE VALUE OF 2. 
	time.sleep(2) # I should have used webdriver wait function but nvm...
	urls = []

	links = driver.find_elements_by_class_name("dropdown-item")
	for link in links:
		if link.get_attribute("href"):
			if "nilai" in link.get_attribute("href"):
				urls.append(link.get_attribute("href"))


	### USE THIS IS YOU WANT DIFFERENT INPUT/BUTTON
	for link in urls:
		driver.get(link)
		rows = driver.find_elements_by_tag_name('tr')
		for row in rows:
			try:
				radio = row.find_element_by_css_selector("input[value='"+str(random.choice(BUTTON))+"']")
				radio.click()
			except Exception as e:
				pass
		driver.find_element_by_name("b_simpan").click()


	#### USE THIS IF YOU WANT SAME INPUT/button
	# for link in urls:
	#     driver.get(link)
	#     radios = driver.find_elements_by_css_selector("input[value='5']")
	#     for radio in radios:
	#       radio.click()

except Exception as e:
	print(e)

driver.quit()