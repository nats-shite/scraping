import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options
import csv
import pandas as pd
import os

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

#lastHeight = driver.execute_script("return document.body.scrollHeight")
#while True:
#      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")   
#      time.sleep(2)
#      newHeight = driver.execute_script("return document.body.scrollHeight")
#      if newHeight == lastHeight:
#          break
#      lastHeight = newHeight
#detail_urls = []

#lastHeight = driver.execute_script("return document.body.scrollHeight")      
elems_detail_url = [i.get_attribute('href') for i in driver.find_elements_by_css_selector(".mn-connection-card__details a") ]
for url in elems_detail_url:
 #newHeight = driver.execute_script("return document.body.scrollHeight")
 #if newHeight == lastHeight:
 # break
 elems_detail_url.append(url)
 for url_list in elems_detail_url:
              driver.get(url_list)
              time.sleep(3)
              name = driver.find_elements_by_css_selector('.inline.t-24.t-black.t-normal.break-words')
              corp = driver.find_elements_by_css_selector('.pv-entity__logo.company-logo img')
              service_years = driver.find_elements_by_css_selector('.display-flex h4')              
              occupation = driver.find_elements_by_css_selector('.pv-profile-section__card-item-v2.pv-profile-section.pv-position-entity.ember-view h3')
              school = driver.find_elements_by_css_selector('.pv-entity__school-name.t-16.t-black.t-bold')
              enrollment_period = driver.find_elements_by_css_selector('.pv-entity__degree-info time')
              detail_school = driver.find_elements_by_css_selector('.pv-entity__comma-item')
              name.append("")
              corp.append("")
              service_years.append("")
              occupation.append("")
              school.append("")
              enrollment_period.append("")
              detail_school.append("")
              for na, cor, sev_year, occu, shc, en_period, dtl_sch,   in zip(name, corp,service_years, occupation, school, enrollment_period, detail_school):
                 print("" if na == "" else na.text)
                 print("" if cor == "" else cor.get_attribute("alt"))
                 print("" if sev_year == "" else sev_year.text)
                 print("" if occu == "" else occu.text)
                 print("" if shc == "" else shc.text)
                 print("" if en_period == "" else en_period.text)
                 print("" if dtl_sch == "" else dtl_sch.text)
                 #print(ski.text)-
                 name = "" if na == "" else na.text
                 corp = "" if cor == "" else cor.get_attribute("alt")
                 service_years = "" if sev_year == "" else sev_year.text
                 occupation = "" if occu == "" else occu.text
                 school = "" if shc == "" else shc.text
                 enrollment_period = "" if en_period == "" else en_period.text
                 detail_school = "" if dtl_sch == "" else dtl_sch.text
                 with open('dtl_text', mode='a', encoding = 'utf-8') as fw:
                   fw.write(name + '\n' + "【職歴】" + '\n' + corp + '\n' + service_years + '\n' + occupation + '\n' + "【学歴】" + '\n' + school + '\n' + enrollment_period + '\n' + detail_school + '\n')
                   #driver.back()
                   #cur_url = driver.current_url
                   #if cur_url == "https://www.linkedin.com/mynetwork/invite-connect/connections/":
                   #  break

#status = driver.find_elements_by_css_selector('.mn-connection-card__name.t-16.t-black.t-bold')
#status = driver.find_elements_by_css_selector('.mn-connection-card__details')
#src = driver.find_elements_by_css_selector(".list-style-none img")
#href = driver.find_elements_by_css_selector(".mn-connection-card__details a")
#for summary, image, link in zip(status, src, href):
#  print(summary.text)
#  print("\t" + image.get_attribute("src"))
#  print("\t" + link.get_attribute("href"))
#  status = summary.text
#  src = "profilePicture:" + "\t" + image.get_attribute("src")
#  href = "profileLink：" + "\t" + link.get_attribute("href")
#  with open('text', mode='a', encoding = 'utf-8') as fw:
#        fw.write(status + '\n' + src + '\n' + href + '\n')
#        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

driver.quit()