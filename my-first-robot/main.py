from RPA.Browser.Selenium import Selenium
import time

browser = Selenium()

# Step 1: Open browser and go to Google
browser.open_available_browser("https://www.google.com")
browser.maximize_browser_window()

# Step 2: Wait until the visible search input field is present
search_box_xpath = '//textarea[@name="q"]'
browser.wait_until_element_is_visible(search_box_xpath, timeout=10)
time.sleep(3)

# Step 3: Type into search box
browser.input_text(search_box_xpath, "Robocorp")
time.sleep(3)

# Step 4: Submit the search
browser.press_keys(search_box_xpath, "ENTER")
time.sleep(3)

# Step 5: Wait for results page
browser.wait_until_page_contains("Robocorp", timeout=10)
time.sleep(3)

# Step 6: Capture screenshot
browser.capture_page_screenshot("google_search_results.png")
time.sleep(3)

# Step 7: Close browser
browser.close_browser()
 