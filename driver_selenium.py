import time
from pprint import pprint

from selenium.common.exceptions import (ElementNotInteractableException,
                                        NoSuchElementException)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)

search = input('Input ')
result = []

driver.get(f'https://pypi.org/search/?o=&q={search}')
pagination_buttons = driver.find_element(
    by=By.XPATH,
    value='//*[@id="content"]/div/div/div[2]/form/div[3]/div'
)
last_page_number = pagination_buttons.find_elements_by_tag_name('a')[-2].text
if str(last_page_number) == 'Previous':
    last_page_number = 1


for i in range(1, int(last_page_number)+1):
    driver.get(f'https://pypi.org/search/?o=&q={search}&page={i}')

    for j in range(1, 22):
        try:
            # time.sleep(15)
            name = driver.find_element(
                by=By.CSS_SELECTOR,
                value=f"#content > div > div > div.left-layout__main > form > div:nth-child(3) > ul > li:nth-child({j}) > a > h3 > span.package-snippet__name"
            ).text
            version = driver.find_element(
                by=By.XPATH,
                value=f"html / body / main / div / div / div[2] / form / div[3] / ul / li[{j}] / a / h3 / span[2]"
            ).text

            result.append(
                {
                    'name': name,
                    'version': version,
                    'command': f'pip install {name}=={version}'
                }
            )

        except NoSuchElementException as e:
            print(e)
            break

with open(f'result_{search}.txt', 'w', encoding='utf-8') as f:
    for el in result:
        result_str = f"""
        name = {el['name']} \n
        version = {el['version']} \n
        command': {el['command']} \n
        --------------------------------
        """
        f.write(result_str)




