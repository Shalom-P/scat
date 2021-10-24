from bs4 import BeautifulSoup as BS
import requests
from selenium import webdriver
import json, time



def scrap_news(quest):
    PATH='./driver/chromedriver.exe'
    driver = webdriver.Chrome(PATH)

    driver.get(quest)

    youtube_data = []

    for result in driver.find_elements_by_css_selector('.text-wrapper.style-scope.ytd-video-renderer'):
        title = result.find_element_by_css_selector('.title-and-badge.style-scope.ytd-video-renderer').text
        link = result.find_element_by_css_selector('.title-and-badge.style-scope.ytd-video-renderer a').get_attribute('href')
        channel_name = result.find_element_by_css_selector('.long-byline').text
        channel_link = result.find_element_by_css_selector('#text > a').get_attribute('href')
        views = result.find_element_by_css_selector('.style-scope ytd-video-meta-block').text.split('\n')[0]

        try:
            time_published = result.find_element_by_css_selector('.style-scope ytd-video-meta-block').text.split('\n')[1]
        except:
            time_published = None

        try:
            snippet = result.find_element_by_css_selector('.metadata-snippet-container').text
        except:
            snippet = None

        try:
            if result.find_element_by_css_selector('#channel-name .ytd-badge-supported-renderer') is not None:
                verified_badge = True
            else:
                verified_badge = False
        except:
            verified_badge = None

        try:
            extensions = result.find_element_by_css_selector('#badges .ytd-badge-supported-renderer').text
        except:
            extensions = None

        youtube_data.append({
            'title': title,
            'link': link,
            'channel': {'channel_name': channel_name, 'channel_link': channel_link},
            'views': views,
            'time_published': time_published,
            'snippet': snippet,
            'verified_badge': verified_badge,
            'extensions': extensions,
        })
    '''aaa = open("tits.json","w")
    json.dump(youtube_data, aaa, indent=2)
    aaa.close()
    with open('tits.json', 'r') as f:
        distros_dict = json.load(f)

    for distro in distros_dict:
        print(distro['title'])
    f.close()'''

    driver.quit()
    return youtube_data

a = scrap_news("https://www.youtube.com/results?search_query=myanmar+had+a+coup+bbc")
s = []
for i in a:
    w = 0
    s.append({'title':i['title'],'channel':i['channel']})
    if w == 4:
        break
    else:
        w =+ 1
print(len(s))