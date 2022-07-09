import sys
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import unittest

import util

class Test(unittest.TestCase):

    def setUp(self):
        self.options = Options()
        self.options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)

    def tearDown(self):
        self.driver.quit()

    def test_fullpage_screenshot(self):
        #url = "https://docs.gimp.org/2.10/en/gimp-filter-noise-rgb.html"
        url = sys.argv[1]
        self.driver.get(url)
        util.fullpage_screenshot(self.driver, "image.png")
        os.system("xdg-open image.png")

if __name__ == "__main__":
    unittest.main(argv=[sys.argv[0]])
