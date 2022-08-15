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


class WebScrapper:
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)

    def __init__(self):
        self.search = input('Input ')
        self.result = []
        self.driver.get(f'https://pypi.org/search/?o=&q={self.search}')


    def get_last_page_number(self, pagination_buttons):
        last_page_number = pagination_buttons.find_elements_by_tag_name('a')[-2].text
        if str(last_page_number) == 'Previous':
            last_page_number = 1
        return last_page_number

    def get_pagination_buttons(self):
        return self.driver.find_element(
            by=By.XPATH,
            value='//*[@id="content"]/div/div/div[2]/form/div[3]/div'
        )

    def collect_elements(self):
        for i in range(1, int(self.get_last_page_number(self.get_pagination_buttons()) + 1)):
            self.driver.get(f'https://pypi.org/search/?o=&q={self.search}&page={i}')

            for j in range(1, 22):
                try:
                    # time.sleep(15)
                    name = self.driver.find_element(
                        by=By.CSS_SELECTOR,
                        value=f"#content > div > div > div.left-layout__main > form > div:nth-child(3) > ul > li:nth-child({j}) > a > h3 > span.package-snippet__name"
                    ).text
                    version = self.driver.find_element(
                        by=By.XPATH,
                        value=f"html / body / main / div / div / div[2] / form / div[3] / ul / li[{j}] / a / h3 / span[2]"
                    ).text

                    self.result.append(
                        {
                            'name': name,
                            'version': version,
                            'command': f'pip install {name}=={version}'
                        }
                    )

                except NoSuchElementException as e:
                    print(e)
                    break

    def save_result(self):
        with open(f'result_{self.search}.txt', 'w', encoding='utf-8') as f:
            for el in self.result:
                result_str = f"""
                name = {el['name']} \n
                version = {el['version']} \n
                command': {el['command']} \n
                --------------------------------
                """
                f.write(result_str)



if __name__ == "__main__":
    scrapper = WebScrapper()
    scrapper.collect_elements()
    scrapper.save_result()
    print("run")


