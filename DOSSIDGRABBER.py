import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def fancy_print():
    ascii_art = """
██████╗  ██████╗ ██████╗ ███████╗███████╗███████╗███████╗    ███████╗██╗██████╗ 
██╔══██╗██╔═══██╗██╔══██╗██╔════╝╚══███╔╝╚══███╔╝╚══███╔╝    ██╔════╝██║██╔══██╗
██║  ██║██║   ██║██████╔╝█████╗    ███╔╝   ███╔╝   ███╔╝     ███████╗██║██║  ██║
██║  ██║██║   ██║██╔═══╝ ██╔══╝   ███╔╝   ███╔╝   ███╔╝      ╚════██║██║██║  ██║
██████╔╝╚██████╔╝██║     ███████╗███████╗███████╗███████╗    ███████║██║██████╔╝
╚═════╝  ╚═════╝ ╚═╝     ╚══════╝╚══════╝╚══════╝╚══════╝    ╚══════╝╚═╝╚═════╝ 
                                                                                    
    """
    print(ascii_art)

def get_user_input():
    fancy_print()
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    password_asterisks = '*' * len(password)
    print(f"Password: {password_asterisks}")
    return username, password

def obtain_sid(username, password):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s, options=chrome_options)

    driver.get("https://www.darkorbit.com/?originalURL=darkorbit.com&")

    accept_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".css-47sehv"))
    )
    accept_button.click()

    user_field = driver.find_element(By.ID, "bgcdw_login_form_username")
    password_field = driver.find_element(By.ID, "bgcdw_login_form_password")

    user_field.send_keys(username)
    password_field.send_keys(password)

    login_button = driver.find_element(By.CSS_SELECTOR, ".bgcdw_button.bgcdw_login_form_login")
    login_button.click()

    WebDriverWait(driver, 10).until(EC.url_contains(".darkorbit.com/indexInternal.es"))

    current_url = driver.current_url
    server = current_url.split("//")[1].split(".")[0]

    cookie_dosid = driver.get_cookie("dosid")
    sid = None
    if cookie_dosid:
        sid = cookie_dosid["value"]

    driver.quit()
    return sid, server

def main():
    username, password = get_user_input()
    sid, server = obtain_sid(username, password)
    print(f"SID: {sid}")
    print(f"Server: {server}")
    input("Press any key and then 'Enter' to close...")

if __name__ == "__main__":
    main()
