from selenium import webdriver
import ast
driver = webdriver.PhantomJS()
#driver.get("https://www.consumeraffairs.com/automotive/caterpillar.html")
driver.get("https://www.consumeraffairs.com/homeowners/frontpoint-security.html ")
#xpath_string = "//a[@data-param_type='sidebar_button-click']"
#elem = driver.find_element_by_xpath(xpath_string)
xpath_string = '//div[@id="brand-logo"]/a'
elem = driver.find_element_by_xpath(xpath_string)
attribute = elem.get_attribute("data-ga-data-layer")
#("data-cta_text")
print "-%s-" % attribute
u= ast.literal_eval(attribute)

print u["element_label"]
#print attribute["element_label"]

#company-description-box_click
#sticky-header_click
