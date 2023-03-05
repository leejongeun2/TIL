from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.opinet.co.kr/searRgSelect.do")
time.sleep(2)
driver.execute_script('goSubPage(0,0,99)') # 함수실행