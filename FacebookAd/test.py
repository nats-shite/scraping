import slackweb
import requests
import os
import sys

FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "image/screen.png")
TOKEN = "xoxp-877798255249-888041067616-1023677282513-dd3077bc19836f29d363c178a93c3e1e"
CHANNEL = "C0111MCHH9V"

files = {'file': open(FILENAME, 'rb')}
param = {'token':TOKEN, 'channels':CHANNEL}
res = requests.post(url="https://slack.com/api/files.upload",params=param, files=files)

#slack = slackweb.Slack(url="https://hooks.slack.com/services/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")
#slack.notify(text="pythonからslackへpostできるかのテスト <!channel>")
