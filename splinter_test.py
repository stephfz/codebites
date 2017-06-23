from splinter  import Browser


browser = Browser('firefox')
browser.visit("www.consumeraffairs.com")
browser.save_screenshot('test.png')
browser.quit()
