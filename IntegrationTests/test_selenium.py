from time import sleep
from selenium import webdriver
from django.test import TestCase


class SeleniumTests(TestCase):
    def test_signup(self):
        driver = webdriver.Chrome()
        driver.get('http://127.0.0.1:8000/')
        driver.find_element_by_id("signup").click()
        driver.find_element_by_id("id_username").send_keys("user")
        driver.find_element_by_id("id_email").send_keys("user@test.com")
        driver.find_element_by_id("id_password1").send_keys("2C326t3AfFCS6g53")
        driver.find_element_by_id("id_password2").send_keys("2C326t3AfFCS6g53")
        driver.find_element_by_id("signup").click()
        self.assertEqual(driver.current_url, "http://127.0.0.1:8000/accounts/signup/")

    def test_login_success(self):
        driver = webdriver.Chrome()
        driver.get('http://127.0.0.1:8000/')
        driver.find_element_by_id("login").click()
        driver.find_element_by_id("id_username").send_keys("user")
        driver.find_element_by_id("id_password").send_keys("2C326t3AfFCS6g53")
        driver.find_element_by_id("login").click()
        self.assertEqual(driver.current_url, "http://127.0.0.1:8000/")

    def test_login_fail(self):
        driver = webdriver.Chrome()
        driver.get('http://127.0.0.1:8000/')
        driver.find_element_by_id("login").click()
        driver.find_element_by_id("id_username").send_keys("user")
        driver.find_element_by_id("id_password").send_keys("password")
        driver.find_element_by_id("login").click()
        self.assertEqual(driver.current_url, "http://127.0.0.1:8000/accounts/login/")

    def test_launcher_success(self):
        driver = webdriver.Chrome()
        driver.get('http://127.0.0.1:8000/')
        driver.find_element_by_id("login").click()
        driver.find_element_by_id("id_username").send_keys("user")
        driver.find_element_by_id("id_password").send_keys("2C326t3AfFCS6g53")
        driver.find_element_by_id("login").click()
        self.assertEqual(driver.current_url, "http://127.0.0.1:8000/")
        driver.find_element_by_id("launcher").click()
        driver.find_element_by_id("getworkspace").click()
        sleep(2)
        driver.find_element_by_id("destroyworkspace").click()
        self.assertEqual(driver.current_url, "http://127.0.0.1:8000/launcher")