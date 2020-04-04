import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options
import csv
import pandas as pd
import os
from collections import defaultdict

options = webdriver.chrome.options.Options()
profile_path = r'C:\Users\shite\AppData\Local\Google\Chrome\User Data'
options.add_argument('--user-data-dir=' + profile_path)
driver = webdriver.Chrome(executable_path=r"C:\Develop\nats\scraping\chromedriver.exe", options=options)
#reCAPTCHA対策でユーザーProfileを指定しているためコメントアウトしている。
#driver.get('https://www.linkedin.com/uas/login?session_redirect=&trk=hb_signin&_l=ja')
#driver.find_element_by_name("session_key").send_keys("zukatakudesu@gmail.com", Keys.RETURN)
#driver.find_element_by_name("session_password").send_keys("natsworld55")
#driver.find_element_by_class_name("login__form_action_container").click()
#time.sleep(30)
driver.get('https://www.linkedin.com/mynetwork/invite-connect/connections/')
time.sleep(5)
pause = 5
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
lastHeight = driver.execute_script("return document.body.scrollHeight")
while True:
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")   
      time.sleep(2)
      newHeight = driver.execute_script("return document.body.scrollHeight")
      if newHeight == lastHeight:
          break
      lastHeight = newHeight

elems_detail_url = [i.get_attribute('href') for i in driver.find_elements_by_css_selector(".mn-connection-card__details a") ]
for url_list in elems_detail_url:
              driver.get(url_list)
              time.sleep(3)      
              names = driver.find_elements_by_css_selector('.inline.t-24.t-black.t-normal.break-words')
              names.append("")
              for name in names:
                print("" if name == "" else "名前：" + name.text)
                name = "" if name == "" else name.text
                with open('dtl_text', mode='a', encoding = 'utf-8') as fw:
                  fw.write('\n' + "名前：" + name + '\n')

              corps = driver.find_elements_by_css_selector('.pv-entity__summary-info.pv-entity__summary-info--background-section>p.pv-entity__secondary-title.t-14.t-black.t-normal')
              corps.append("")
              positions = driver.find_elements_by_css_selector('.pv-entity__summary-info.pv-entity__summary-info--background-section>h3')
              positions.append("")
              periods = driver.find_elements_by_css_selector('.pv-entity__summary-info.pv-entity__summary-info--background-section>div>h4.pv-entity__date-range.t-14.t-black--light.t-normal>span:nth-child(2)')
              periods.append("")
              for corp, position, period in zip(corps, positions, periods):
                 print("" if corp == "" else "会社名：" + corp.text)
                 print("" if position == "" else "ポジション名：" + position.text)
                 print("" if period == "" else "在籍期間：" + period.text)
                 corp = "" if corp == "" else corp.text
                 position = "" if position == "" else position.text
                 period = "" if period == "" else period.text
                 with open('dtl_text', mode='a', encoding = 'utf-8') as fw:
                  fw.write("会社名：" + corp + '\n' + "ポジション名：" + position + '\n' + "在籍期間：" + period + '\n')

              corps2 = driver.find_elements_by_css_selector('.pv-entity__company-summary-info>h3>span:nth-child(2)')
              corps2.append("")
              positions2 = driver.find_elements_by_css_selector('.pv-entity__summary-info-v2.pv-entity__summary-info--background-section.pv-entity__summary-info-margin-top>h3>span:nth-child(2)')
              positions2.append("")
              periods2 = driver.find_elements_by_css_selector('h4.pv-entity__date-range.t-14.t-black--light.t-normal>span:nth-child(2)')
              periods2.append("")
              #occu_sections = driver.find_elements_by_css_selector('pv-entity__position-group-pager.pv-profile-section__list-item.ember-view')
              #for occu_section in occu_sections:
              for corp2, position2, period2 in zip(corps2, positions2, periods2):
                 oc = defaultdict(list)
                 for corp2, position2 in zip(corps2, positions2):
                  corp_text = "" if corp2 == "" else corp2.text
                  position_text = "" if position2 == "" else position2.text
                  oc[corp_text].append(position_text)
                  print(oc)
                  print("" if corp2 == "" else "会社名：" + corp2.text)
                  print("" if position2 == "" else "ポジション名：" + position2.text)
                  print("" if period2 == "" and positions2  == "" else "在籍期間：" + period2.text)
                  corp2 = "" if corp2 == "" else corp2.text
                  position2 = "" if position2 == "" else position2.text
                  period2 = "" if period2 == "" and positions2  == "" else period2.text
                  with open('dtl_text', mode='a', encoding = 'utf-8') as fw:
                   fw.write("会社名2：" + corp2 + '\n' + "ポジション名2：" + position2 + '\n' + "在籍期間2：" + period2 + '\n')
              
              schools = driver.find_elements_by_css_selector('.pv-entity__summary-info.pv-entity__summary-info--background-section>div>h3')
              schools.append("")
              admissions = driver.find_elements_by_css_selector('.pv-entity__summary-info.pv-entity__summary-info--background-section>p>span:nth-child(2)>time:nth-child(1)')
              admissions.append("")
              graduations = driver.find_elements_by_css_selector('.pv-entity__summary-info.pv-entity__summary-info--background-section>p>span:nth-child(2)>time:nth-child(2)')
              graduations.append("")
              for school, admission, graduation in zip(schools, admissions, graduations):
                print("" if school == "" else "学校名：" + school.text)
                print("" if admission == "" else "入学時期：" + admission.text)
                print("" if graduation == "" else "卒業時期：" + graduation.text)
                school = "" if school == "" else school.text
                admission = "" if admission == "" else admission.text
                graduation = "" if graduation == "" else graduation.text
                with open('dtl_text', mode='a', encoding = 'utf-8') as fw:
                  fw.write("学校名：" + school + '\n' + "入学時期：" + admission + '\n' + "卒業時期：" + graduation + '\n')
              
driver.quit()