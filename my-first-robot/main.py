# # main.py
# def main():
#     print("Hello from Robocorp Python robot!")

# if __name__ == "__main__":
#     main()

from RPA.Browser.Selenium import Selenium
import time

browser = Selenium()
browser.open_available_browser("https://google.com")
# time.sleep(5)
browser.input_text("name=q", "Robocorp")
time.sleep(5)
browser.press_keys("name=q", "ENTER")
time.sleep(5)
browser.capture_page_screenshot()
time.sleep(5)
browser.close_browser()
 