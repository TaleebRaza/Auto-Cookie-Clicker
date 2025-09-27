import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option(name="detach", value=True)

driver = webdriver.Edge(options=edge_options)
driver.get("https://ozh.github.io/cookieclicker/")

time.sleep(2)
driver.find_element(by=By.ID, value="langSelect-EN").click()
time.sleep(2)

driver.find_element(by=By.CLASS_NAME, value="cc_btn.cc_btn_accept_all").click()

cookie = driver.find_element(by=By.ID, value="bigCookie")
start_time = current_time = notification_check_delay = upgrade_check_delay = time.time()

while True:
    cookie.click()
    now = time.time()

    if now - current_time > 5:
        current_time = now

        if now - upgrade_check_delay > 30:
            print("upgrade check")
            upgrade_check_delay = now
            upgrades = driver.find_elements(by=By.CLASS_NAME, value="crate.upgrade.enabled")
            if upgrades:
                upgrades[-1].click()
        else:
            print("product check")
            products = driver.find_elements(by=By.CLASS_NAME, value="product.unlocked")
            cookies = driver.find_element(by=By.ID, value="cookies")

            try:
                cookies = int(cookies.text.split(" ")[0])
            except ValueError:
                cookies = int("".join(cookies.text.split(" ")[0].split(",")))



            for product in reversed(products):
                try:
                    if cookies >= int(product.text.split("\n")[1]):
                        product.click()
                except ValueError:
                    if cookies >= int("".join(product.text.split("\n")[1].split(","))):
                        product.click()


    if now - notification_check_delay > 10.0:
        try: driver.find_element(by=By.CLASS_NAME, value="framed.close.sidenote").click()

        except (NoSuchElementException, StaleElementReferenceException): continue

        finally: notification_check_delay = now + 10.0


    # if now - start_time > 90:
    #     break
driver.quit()