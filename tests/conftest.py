import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import  Options as chrome_options


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome') # Use headless if you do need a browser UI
    options.add_argument('start-maximized')
    options.add_argument('windows-size=1800,600')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):

    driver = webdriver.Chrome(executable_path='Source/chromedriver.exe')
    return driver


@pytest.fixture(scope='function')
def setup(request,get_webdriver):
    driver = get_webdriver
    url = 'https://www.tase.co.il/en'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.close()








