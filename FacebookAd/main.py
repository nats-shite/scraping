import os
import sys
import time
import slackweb
import requests
import datetime
import schedule
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.chrome.options.Options()
profile_path = r'C:\Users\shite\AppData\Local\Google\Chrome\User Data'
options.add_argument('--user-data-dir=' + profile_path)
options.add_argument('--profile-directory=Profile 1') 
#options.add_argument('--headless')

driver = webdriver.Chrome(executable_path=r"C:\Develop\nats\scraping\chromedriver.exe", options=options)
#reCAPTCHA対策でユーザーProfileを指定しているためコメントアウトしている。
#driver.get('https://ja-jp.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=110')
#driver.find_element_by_css_selector("#email").send_keys("zukatakudesu@gmail.com", Keys.RETURN)
#driver.find_element_by_css_selector("#pass").send_keys("gantz-33055")
#driver.find_element_by_css_selector("#loginbutton").click()
#time.sleep(5)
driver.get('https://www.facebook.com/adsmanager/reporting/view?act=544933962304837&metrics=delivery_info%2Cresults%2Creach%2Cimpressions%2Cspend%2Cclicks%2Ccpc%2Cctr%2Ccpm%2Ccost_per_result%2Cresult_rate%2Cfrequency%2Cdelivery_start&selected_report_id=23844378815800366&sort_spec=results~desc')
time.sleep(2)
driver.maximize_window()

now = datetime.datetime.now()
filename = 'FB_screen_' + now.strftime('%Y%m%d_%H') + '.png'
# File Name
FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "image/" + filename)

# get width and height of the page
w = driver.execute_script("return document.body.scrollWidth;")
h = driver.execute_script("return document.body.scrollHeight;")

# set window size
driver.set_window_size(w,h)

# Get Screen Shot
driver.save_screenshot(FILENAME)

# Close Web Browser
driver.quit()

# send message & screenshot to slack
TOKEN = "xoxp-877798255249-888041067616-1023677282513-dd3077bc19836f29d363c178a93c3e1e"
CHANNEL = "C0111MCHH9V"

files = {'file': open(FILENAME, 'rb')}
param = {'token':TOKEN, 'channels':CHANNEL}
res = requests.post(url="https://slack.com/api/files.upload",params=param, files=files)

slack = slackweb.Slack(url="https://hooks.slack.com/services/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")
slack.notify(text='<https://www.facebook.com/adsmanager/reporting/view?act=544933962304837&metrics=delivery_info%2Cresults%2Creach%2Cimpressions%2Cspend%2Cclicks%2Ccpc%2Cctr%2Ccpm%2Ccost_per_result%2Cresult_rate%2Cfrequency%2Cdelivery_start&selected_report_id=23844378815800366&sort_spec=results~desc| 広告レポート> <!channel>')
exit()