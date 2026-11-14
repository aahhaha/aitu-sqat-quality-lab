from pathlib import Path
import os
import allure,pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.browser
@allure.feature('Student question submission')
@pytest.mark.parametrize('text',['Explain the next step','<img src=x onerror="window.injected=true">'])
def test_student_flow_in_real_browser(live_server,text):
    browser=os.environ.get('TEST_BROWSER','chrome')
    options=webdriver.FirefoxOptions() if browser=='firefox' else webdriver.ChromeOptions()
    options.add_argument('-headless' if browser=='firefox' else '--headless=new')
    if browser!='firefox':options.add_argument('--no-sandbox');options.add_argument('--disable-dev-shm-usage')
    driver=webdriver.Firefox(options=options) if browser=='firefox' else webdriver.Chrome(options=options)
    try:
        driver.get(live_server)
        with allure.step('Read the teacher-visible identity notice'):
            assert 'teacher' in driver.find_element(By.ID,'privacy').text
        driver.find_element(By.ID,'author').send_keys('Synthetic Student')
        driver.find_element(By.ID,'question').send_keys(text)
        driver.find_element(By.ID,'submit').click()
        WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.ID,'message'),'Question submitted'))
        assert text in driver.find_element(By.ID,'questions').text
        assert 'Synthetic Student' not in driver.find_element(By.ID,'questions').text
        assert driver.execute_script('return window.injected || false') is False
        driver.find_element(By.CSS_SELECTOR,'#questions button').click()
        WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.ID,'questions'),'1 votes'))
        allure.attach(driver.get_screenshot_as_png(),name=f'{browser}-student-result',attachment_type=allure.attachment_type.PNG)
        Path('reports/screenshots').mkdir(parents=True,exist_ok=True)
        driver.save_screenshot(f'reports/screenshots/{browser}-{len(text)}.png')
    finally:driver.quit()
