from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InstagramScraper:
    def __init__(self, username):
        self.username = username
        self.url = f"https://www.instagram.com/{username}/"
        self.driver = webdriver.Firefox()  # Use Firefox webdriver

    def _get_element_text(self, xpath):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            return element.text
        except Exception as e:
            print(f"Error: {e}")
            return None

    def get_followers_count(self):
        followers_xpath = "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[2]/button/span/span"
        return self._get_element_text(followers_xpath)

    def get_following_count(self):
        following_xpath = "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[3]/button/span/span"
        return self._get_element_text(following_xpath)

    def scrape_profile_info(self):
        self.driver.get(self.url)

        followers_count = self.get_followers_count()
        following_count = self.get_following_count()

        print(f"Followers: {followers_count}")
        print(f"Following: {following_count}")

    def close(self):
        self.driver.quit()

# Example usage
if __name__ == "__main__":
    username = "guviofficial"
    scraper = InstagramScraper(username)
    
    try:
        scraper.scrape_profile_info()
    finally:
        scraper.close()