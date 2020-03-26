import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
options = webdriver.chrome.options.Options()
profile_path = r'C:\Users\shite\AppData\Local\Google\Chrome\User Data'
options.add_argument('--user-data-dir=' + profile_path)
driver = webdriver.Chrome(executable_path=r"C:\Develop\nats\scraping\chromedriver.exe", options=options)
#reCAPTCHA対策でユーザーProfileを指定しているためコメントアウトしている。
#driver.get('https://www.linkedin.com/uas/login?session_redirect=&trk=hb_signin&_l=ja')
#driver.find_element_by_name("session_key").send_keys("zukatakudesu@gmail.com", Keys.RETURN)
#driver.find_element_by_name("session_password").send_keys("natsworld55")
#driver.find_element_by_class_name("login__form_action_container").click()
#time.sleep(5)
driver.get('https://www.linkedin.com/mynetwork/invite-connect/connections/')
time.sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
lastHeight = driver.execute_script("return document.body.scrollHeight")
while True:
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")   
      time.sleep(2)
      newHeight = driver.execute_script("return document.body.scrollHeight")
      if newHeight == lastHeight:
          break
      lastHeight = newHeight
      
status = driver.find_elements_by_css_selector('.mn-connection-card__name.t-16.t-black.t-bold')
status = driver.find_elements_by_css_selector('.mn-connection-card__details')
src = driver.find_elements_by_css_selector(".list-style-none img")
href = driver.find_elements_by_css_selector(".mn-connection-card__details a")
for summary, image, link in zip(status, src, href):
  #時間かかるのでコメントアウト
  #print(summary.text)
  #print("\t" + image.get_attribute("src"))
  #print("\t" + link.get_attribute("href"))
  status = summary.text
  src = "profilePicture:" + "\t" + image.get_attribute("src")
  href = "profileLink：" + "\t" + link.get_attribute("href")
  with open('text', mode='a', encoding = 'utf-8') as fw:
        fw.write(status + '\n' + src + '\n' + href + '\n')
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.quit()