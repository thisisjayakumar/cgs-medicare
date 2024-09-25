from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time


def run_selenium_script(input_numbers):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)

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

    results = []

    for input_number in input_numbers:
        search_input = driver.find_element(By.NAME, "txtProcCode")
        search_input.clear()
        search_input.send_keys(str(input_number))

        time.sleep(1)

        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "Button1"))
        )
        search_button.click()

        time.sleep(1)

        wait = WebDriverWait(driver, 5)
        table = wait.until(EC.presence_of_element_located((By.ID, "DataGrid1")))

        rows = table.find_elements(By.TAG_NAME, "tr")

        current_results = []
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            row_data = [cell.text for cell in cells]
            current_results.append(row_data)

        results.append({
            'input_number': input_number,
            'results': current_results
        })

    driver.quit()
    return results
