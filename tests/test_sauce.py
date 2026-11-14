"""Optional external integration; absence of credentials is a reported skip."""
import os,pytest
from selenium import webdriver
@pytest.mark.external
def test_remote_browser():
    user=os.environ.get('SAUCE_USERNAME');key=os.environ.get('SAUCE_ACCESS_KEY');url=os.environ.get('PUBLIC_TEST_URL')
    if not all([user,key,url]):pytest.skip('Configure Sauce Labs credentials and an accessible test deployment')
    options=webdriver.ChromeOptions();options.browser_version='latest';options.platform_name='Windows 11'
    options.set_capability('sauce:options',{'username':user,'accessKey':key,'name':'ClearQuestion privacy notice'})
    d=webdriver.Remote(command_executor='https://ondemand.eu-central-1.saucelabs.com/wd/hub',options=options)
    try:d.get(url);assert 'ClearQuestion' in d.title
    finally:d.quit()
