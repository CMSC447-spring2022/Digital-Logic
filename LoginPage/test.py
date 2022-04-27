from contextlib import contextmanager
import time

from django.test import override_setting, TestCase
from django.urls import reverse
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from models.py
#put our url in here once we have a url
#page.get("https://ourURLhere.com")

#tests login
def test_login(self):
    with self.browser("index") as page:
        elem = page.find_element_by_id('Username')  # Find the search box
        elem.send_keys('admin') #inputs admin as user
        elem = page.find_element_by_id('Password')
        elem.send_keys('password') #inputs password as input
        elem.submit() #submits login info

        #working progress
        self.assertIsNotNone(elem, 1 == 1, "Login test done")

#tests create account (working progress)
def test_create_account(self):
    with self.browser("index") as page:
        elem = page.find_element_by_id("Create Account").click()
        self.assertIsNotNone(elem, 1 == 1, "Login test done")
