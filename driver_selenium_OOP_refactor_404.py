
from selenium.common.exceptions import NoSuchElementException                                   
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import constants
import os

class WebScrapper:
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()))

    def __init__(self):
        self.search = input('Input ')
        self.result = []
        self.driver.get(constants.SEARCH_URL.format(search_query=self.search, page=1))

    @staticmethod
    def get_package_info(package):
        name, version, date = package.find_elements(by=By.XPATH, value="span")
        return {
            'name': name.text,
            'version': version.text,
            'date': date.text,
            'command': f'pip install {name.text}=={version.text}'
        }
    
    def collect_elements(self):
        page = 1
        while True:
            self.driver.get(constants.SEARCH_URL.format(search_query=self.search, page=page))
            packages = self.driver.find_elements(
                by=By.XPATH,
                value=constants.PACKAGES_XPATH_VALUE
            )
            if not packages:
                break
            
            packages_info = list(map(self.get_package_info, packages))
            self.result.extend(packages_info)
                
            page += 1


    def save_result(self):
        if not os.path.exists("results"):
            os.mkdir("results")
        with open(f'results/result_{self.search}.txt', 'w', encoding='utf-8') as f:
            f.write(f"Found projects {len(self.result)}\n")
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
    print("Finish")


