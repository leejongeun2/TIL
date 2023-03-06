from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install()) # 1. webdrive 킨다. 
driver.get("https://www.opinet.co.kr/searRgSelect.do") # 2. 지역별 주유소 찾기 접속
time.sleep(2)
driver.execute_script('goSubPage(0,0,99)') # 함수실행 
time.sleep(2)
# sido = webdriver.find_element_by_xpath('//*[@id="SIDO_NM0"]') # 3. sido 목록 가져온다.
# sido = WebDriverWait(driver,timeout=5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="SIDO_NM0"]'))) # 문법바뀜 driver.find_element(By.XPATH,~~),  from selenium.webdriver.common.by import By
sido = driver.find_element(By.XPATH, '//*[@id="SIDO_NM0"]')
sido_names = sido.find_elements(By.TAG_NAME, 'option')

sido_list = [ ]
for sido_name in sido_names:
    sido_list.append(sido_name.get_attribute('value'))

sido_list1 = sido_list[1:]

for sido_name in sido_list1:
    sido = driver.find_element(By.XPATH, '//*[@id="SIDO_NM0"]')
    sido.send_keys(sido_name) # 4. 원하는 지역으로 이동한다. 
    time.sleep(2)

    # 5. 시군구 목록을 가져온다. 
    # sigungu = WebDriverWait(driver,timeout=10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="SIGUNGU_NM0"]'))) # 문법바뀜 driver.find_element(By.XPATH,~~),  from selenium.webdriver.common.by import By
    sigungu = driver.find_element(By.XPATH, '//*[@id="SIGUNGU_NM0"]')
    sigungu_names = sigungu.find_elements(By.TAG_NAME, 'option')

    sigungu_list = [ ] # 5. 얻어온 목록으로 반복문을 수행하면서, 
    for sigungu_name in sigungu_names:
        sigungu_list.append(sigungu_name.get_attribute('value'))

    sigungu_list1 = sigungu_list[1:]
    print(sigungu_list1)
    

    # 6. 조회를 누르고
    for sigungu_name in sigungu_list1:
        sigungu = driver.find_element(By.XPATH, '//*[@id="SIGUNGU_NM0"]')
        time.sleep(2)
        sigungu.send_keys(sigungu_name)
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="searRgSelect"]').click()
        # WebDriverWait(driver,timeout=15).until(EC.presence_of_element_located((By.XPATH,'//*[@id="searRgSelect"]'))).click() # 문법바뀜 driver.find_element(By.XPATH,~~),  from selenium.webdriver.common.by import By
        time.sleep(2) 
        # 7. 엑셀 저장을 누른다. 
        driver.find_element(By.XPATH, '//*[@id="glopopd_excel"]').click()
        # WebDriverWait(driver,timeout=20).until(EC.presence_of_element_located((By.XPATH,'//*[@id="glopopd_excel"]'))).click()






