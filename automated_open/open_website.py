from selenium import webdriver
chrome_browser=webdriver.Chrome("./chromedriver")
chrome_browser.maximize_window()
chrome_browser.get("https://aditya22.pythonanywhere.com")
assert 'My Website' in chrome_browser