import datetime as dt
import requests
from bs4 import BeautifulSoup
import slackweb

url = "https://jp.techcrunch.com/tag/fundraising/?tc_side_bnr"
headers = {"User-Agent": "hoge"}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.content, "html.parser")

now = dt.datetime.today()
today = "{}年{}月{}日".format(now.year, now.month, now.day)

for article in soup.find_all(class_="block block-thumb"):
    #published = article.find(class_="timestamp").string  # 記事の日付
    published = article.select_one(".block-content>div.byline>time").text
    if published != today:
        continue  # 今日の日付でない場合はスキップ

    # 記事のリンクとタイトルを取得
    header = article.find(class_="post-title")

    link = header.a["href"]
    title = header.string
    #info = title,"\n",link
    l = ["<!channel>" + "■" + today + "の調達情報", title,link]
    info = "\n".join(l)
    
    slack = slackweb.Slack(url="https://hooks.slack.com/services/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")
    slack.notify(text= info)
exit()