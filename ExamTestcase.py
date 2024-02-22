import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestCustomerForm(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="D:\webdriver\chromedriver.exe")
        self.driver.get("http://localhost/custommer/form.html")

    def tearDown(self):
        self.driver.quit()

    def test_case1(self):
        driver = self.driver
        first_name_input = driver.find_element(By.ID, "first-name")
        last_name_input = driver.find_element(By.ID, "last-name")
        age_input = driver.find_element(By.ID, "age")
        submit_button = driver.find_element(By.ID, "sub")
        first_name_input.send_keys("johnjohn")
        last_name_input.send_keys("canonc")
        age_input.send_keys("2")
        submit_button.click()
        result = driver.find_element(By.ID, "firstname").text
        self.assertEqual("First Name: johnjohn", result)
       
        # ถ่ายภาพหน้าจอ
        self.take_screenshot("customer_form_test_case1.png")

    def test_case2(self):
        driver = self.driver
        first_name_input = driver.find_element(By.ID, "first-name")
        last_name_input = driver.find_element(By.ID, "last-name")
        age_input = driver.find_element(By.ID, "age")
        submit_button = driver.find_element(By.ID, "sub")
        first_name_input.send_keys("Johnj")
        last_name_input.send_keys("canoncanoncano")
        age_input.send_keys("149")
        submit_button.click()
        result = driver.find_element(By.ID, "firstname").text
        self.assertEqual("First Name: Johnj", result)
       
        # ถ่ายภาพหน้าจอ
        self.take_screenshot("customer_form_test_case2.png")

    def test_case3(self):
        driver = self.driver
        first_name_input = driver.find_element(By.ID, "first-name")
        last_name_input = driver.find_element(By.ID, "last-name")
        age_input = driver.find_element(By.ID, "age")
        submit_button = driver.find_element(By.ID, "sub")
        first_name_input.send_keys("johnjo")
        last_name_input.send_keys("canoncanoncanon")
        age_input.send_keys("150")

        # Submit the form
        submit_button.click()
        
        result = driver.find_element(By.ID, "firstname").text
        self.assertEqual("First Name: johnjo", result)

        # ถ่ายภาพหน้าจอ
        self.take_screenshot("customer_form_test_case3.png")

    def test_case4(self):
        driver = self.driver
        first_name_input = driver.find_element(By.ID, "first-name")
        last_name_input = driver.find_element(By.ID, "last-name")
        age_input = driver.find_element(By.ID, "age")
        submit_button = driver.find_element(By.ID, "sub")
        first_name_input.send_keys("johnjohnjohnjo")
        last_name_input.send_keys("canoncan")
        age_input.send_keys("75")

        # Submit the form
        submit_button.click()
        
        result = driver.find_element(By.ID, "firstname").text
        self.assertEqual("First Name: johnjohnjohnjo", result)

        # ถ่ายภาพหน้าจอ
        self.take_screenshot("customer_form_test_case4.png")

    def test_case5(self):
        driver = self.driver
        first_name_input = driver.find_element(By.ID, "first-name")
        last_name_input = driver.find_element(By.ID, "last-name")
        age_input = driver.find_element(By.ID, "age")
        submit_button = driver.find_element(By.ID, "sub")
        first_name_input.send_keys("johnjohnjohnjoh")
        last_name_input.send_keys("canoncan")
        age_input.send_keys("75")

        # Submit the form
        submit_button.click()
        
        result = driver.find_element(By.ID, "firstname").text
        self.assertEqual("First Name: johnjohnjohnjoh", result)

        # ถ่ายภาพหน้าจอ
        self.take_screenshot("customer_form_test_case5.png")



if __name__ == "__main__":
    unittest.main()
