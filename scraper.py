import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NewsScraper:
    def __init__(self, driver_path, firefox_binary_path):
        service = Service(driver_path)
        options = Options()
        options.binary_location = firefox_binary_path
        self.driver = webdriver.Firefox(service=service, options=options)

    def fetch_ei_nerd_news(self):
        try:
            self.driver.get("https://www.einerd.com.br/")
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "article"))
            )
            articles = self.driver.find_elements(By.CSS_SELECTOR, "article h2 a")
            print("\nEi Nerd News:")
            for article in articles[:3]: 
                title = article.text
                link = article.get_attribute("href")
                print(f"• {title}")
                print(f"  (Link: {link})\n")
        except Exception as e:
            print(f"Ocorreu um erro ao buscar notícias do Ei Nerd: {e}")

    def fetch_tec_mundo_news(self):
        try:
            self.driver.get("https://www.tecmundo.com.br/")
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "h3"))
            )
            articles = self.driver.find_elements(By.CSS_SELECTOR, "h3 a")
            print("TecMundo News:")
            count = 0
            for article in articles: 
                title = article.text
                link = article.get_attribute("href")
                if "Mais Lidas" not in title:  
                    print(f"• {title}")
                    print(f"  (Link: {link})\n")
                    count += 1
                    if count == 3:  
                        break
        except Exception as e:
            print(f"Ocorreu um erro ao buscar notícias do TecMundo: {e}")

    def close_driver(self):
        self.driver.quit()

if __name__ == "__main__":
    DRIVER_PATH = "C:\\Users\\Tonton\\Downloads\\geckodriver-v0.35.0-win32\\geckodriver.exe"
    FIREFOX_BINARY_PATH = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    
    scraper = NewsScraper(DRIVER_PATH, FIREFOX_BINARY_PATH)

    start_time = time.time()
    
    scraper.fetch_ei_nerd_news()
    scraper.fetch_tec_mundo_news()

    end_time = time.time()
    execution_time = end_time - start_time
    
    print(f"\nTempo total de execução: {execution_time:.2f} segundos")
    
    scraper.close_driver()
