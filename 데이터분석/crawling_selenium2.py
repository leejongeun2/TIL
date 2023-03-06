from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.opinet.co.kr/searRgSelect.do")
time.sleep(2)
driver.execute_script('goSubPage(0,0,99)') # 함수실행

# sido = webdriver.find_element_by_xpath('//*[@id="SIDO_NM0"]')
sigungu = WebDriverWait(driver,timeout=5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="SIGUNGU_NM0"]'))) # 문법바뀜 driver.find_element(By.XPATH,~~),  from selenium.webdriver.common.by import By
sigungu_names = sigungu.find_elements(By.TAG_NAME, 'option')

sigungu_list = [ ]
for sigungu_name in sigungu_names:
    sigungu_list.append(sigungu_name.get_attribute('value'))

sigungu_list1 = sigungu_list[1:]
print(sigungu_list1)
# sido.send_keys('서울특별시')

# *[@id="SIGUNGU_NM0"]
