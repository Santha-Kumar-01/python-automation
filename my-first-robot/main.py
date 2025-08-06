# # main.py
# def main():
#     print("Hello from Robocorp Python robot!")

# if __name__ == "__main__":
#     main()

# from RPA.Browser.Selenium import Selenium
# import time

# browser = Selenium()
# browser.open_available_browser("https://google.com")
# # time.sleep(5)
# browser.input_text("name=q", "Robocorp")
# time.sleep(5)
# browser.press_keys("name=q", "ENTER")
# time.sleep(5)
# browser.capture_page_screenshot()
# time.sleep(5)
# browser.close_browser()
 

from RPA.Browser.Selenium import Selenium
import time

# Initialize browser automation
browser = Selenium()

# Step 1: Open Google
browser.open_available_browser("https://www.google.com")
browser.maximize_browser_window()

# Step 2: Wait until the visible search input is ready
browser.wait_until_element_is_visible("name=q", timeout=10)

# Step 3: Input the search term
browser.input_text("name=q", "Robocorp")
time.sleep(3)

# Step 4: Press ENTER to search
browser.press_keys("name=q", "ENTER")
time.sleep(3)

# Step 5: Wait for the search results to load
browser.wait_until_page_contains("Robocorp", timeout=10)
time.sleep(3)

# Step 6: Take a screenshot of the search results
browser.capture_page_screenshot("google_search_results.png")
time.sleep(3)

# Step 7: Close the browser
browser.close_browser()
 