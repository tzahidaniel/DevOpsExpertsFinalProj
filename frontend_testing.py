from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def run_fronted_test(user_id):
    driver = webdriver.Chrome(service=Service("C:/Users/Tzahi/Downloads/chromedriver_win32/chromedriver.exe"))
    url = f"http://127.0.0.1:5001/users/get_user_data/{user_id}"
    driver.get(url)
    driver.implicitly_wait(10)

    user_name = driver.find_element(By.ID, value="user_name").text
    print(user_name)

    driver.close()


run_fronted_test("99ed1db2-4abc-42a9-8074-60a9584de1f1")
