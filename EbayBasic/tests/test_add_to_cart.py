import pytest
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def setup():
    chrome_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrome_service)
    yield driver
    # driver.quit()


def test_R001_add_item_to_cart(setup):
    driver = setup
    driver.get("https://www.ebay.com")
    search_box = driver.find_element(By.ID, "gh-ac")
    search_box.send_keys("book")
    search_box.send_keys(Keys.RETURN)
    print("log: book page")
    # s-item__link
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".s-item__link:nth-of-type(1)"))
    )
    books = driver.find_elements((By.CSS_SELECTOR, ".s-item__link:nth-of-type(1)"))
    print(len(books))

    action = ActionChains(driver)
    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[1])

    # first_book.click()
    print("log: clicked_ON_First_book")

    add_to_card_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "atcBtn_btn_1"))
    )
    add_to_card_button.click()
    cart_icon = driver.find_element(By.ID, "gh-cart-n")
    assert cart_icon.text == "1"
