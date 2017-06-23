from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.PhantomJS()
driver.get("https://www.google.com")
script = "return window.dataLayer"
js_object = driver.execute_script(script)

if js_object == None:
    print "none"

for os in js_object:
    if os["event"] == 'dataLayer-initialized':
        print "- %s" % os["event"]
        break
