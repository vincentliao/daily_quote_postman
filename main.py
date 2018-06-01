import re
import os
import requests
import json
import config
from bs4 import BeautifulSoup

def send_slack(message):
    data = {
        'username': config.SLACK_USERNAME,
        'icon_emoji': config.SLACK_ICON_EMOJI,
        'text': message
    }

    requests.post(config.SLACK_WEBHOOK_URL, data=json.dumps(data), headers={'Content-Type': 'application/json'})

def get_soup_by(url):
    html = requests.post(url).content
    return BeautifulSoup(html, 'html.parser')

def get_1st_quote(soup):
    first_post= soup.find(id=re.compile(r'post-[0-9]+'))
    first_quote = first_post.find('div', {'class': 'entry cf'})
    return str.strip(first_quote.text)

def main():
    SITE_URL = 'http://www.dailyenglishquote.com/'
    soup = get_soup_by(SITE_URL)
    quote = get_1st_quote(soup)
    send_slack(quote)

if __name__ == '__main__':
    main()





