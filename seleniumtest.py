from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def run_selenium_script(input_numbers):
    driver = webdriver.Chrome()

    driver.get("https://www.cgsmedicare.com/medicare_dynamic/j15/ptpb/ptp/ptp.aspx")

    try:
        accept_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "Accept"))
        )
        accept_button.click()
        print("License agreement accepted.")
    except Exception as e:
        print("Error accepting license agreement:", e)

    time.sleep(1)

    search_input = driver.find_element(By.NAME, "txtProcCode")

    search_input.send_keys(input_numbers)

    time.sleep(1)

    search_button = driver.find_element(By.NAME, "Button1")

    search_button.click()

    time.sleep(1)

    wait = WebDriverWait(driver, 5)
    table = wait.until(EC.presence_of_element_located((By.ID, "DataGrid1")))

    rows = table.find_elements(By.TAG_NAME, "tr")

    results = []
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        row_data = [cell.text for cell in cells]
        results.append(row_data)

    driver.quit()
    return results