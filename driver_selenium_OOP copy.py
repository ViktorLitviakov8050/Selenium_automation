
from selenium.common.exceptions import NoSuchElementException                                   
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import constants
import os

'''
1. Make separate constants
2. Remove redundant imports
3. Add fix for pagination buttons
4. Parse pages until 404 (Page hasn't list items)
'''



class WebScrapper:
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()))

    def __init__(self):
        self.search = input('Input ')
        self.result = []
        self.driver.get(constants.SEARCH_URL.format(search_query=self.search, page=1))

    def get_last_page_number(self):
        try:
            pagination_buttons = self.get_pagination_buttons()
        except NoSuchElementException:
            last_page_number = 1
        else:    
            last_page_number = pagination_buttons.find_elements(by=By.TAG_NAME, value='a')[-2].text
            
        return int(last_page_number)

    def get_pagination_buttons(self):
        return self.driver.find_element(
            by=By.CLASS_NAME,
            value='button-group--pagination'
        )
        

    def collect_elements(self):
        for page in range(1, self.get_last_page_number() + 1):
            self.driver.get(constants.SEARCH_URL.format(search_query=self.search, page=page))
            for package_index in range(1, 22):
                try:
                    package = self.driver.find_element(
                        by=By.XPATH,
                        value=constants.PACKAGE_XPATH_VALUE.format(package_index=package_index)
                    )
                except NoSuchElementException as e:
                    print(e)
                    break
                    
                else:
                    name, version, date = package.find_elements(by=By.XPATH, value="span")

                    self.result.append(
                        {
                            'name': name.text,
                            'version': version.text,
                            'date': date.text,
                            'command': f'pip install {name.text}=={version.text}'
                        }
                    )


    def save_result(self):
        if not os.path.exists("results"):
            os.mkdir("results")
        with open(f'results/result_{self.search}.txt', 'w', encoding='utf-8') as f:
            f.write(f"Found projects {len(self.result)}\n")
            for el in self.result:
                result_str = f"""
name = {el['name']}
version = {el['version']}
command': {el['command']}
--------------------------------
"""
                f.write(result_str)



if __name__ == "__main__":
    scrapper = WebScrapper()
    scrapper.collect_elements()
    scrapper.save_result()
    print("Finish")


