from bs4 import BeautifulSoup as bs
import requests
import os
from splinter import Browser
import pymongo
import pandas as pd
import re
import time

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
	hemisphere_images_urls = {};

	browser = init_browser()
	news_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
	browser.visit(url_news)

	time.sleep(1)
    html = browser.html
    soup = bs(html, "html.parser")

    news_title = soup.find("div", class_='list_text').find('div', class_='content_title').text
    news_title = news_title.replace('\n', '')
    final_dict("news_title") = news_title

    news_text = soup.find("div", class_='list_text').find('div', class_= 'rollover_description').text
    news_text = news_text.replace('\n', '')
    final_dict("news_text") = news_text

    browser.quit()

    browser = init_browser()
    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url)

    time.sleep(1)
    html = browser.html
    soup = bs(html, "html.parser")

    feat_img = soup_img.find("div", class_='carousel_items').find("article", class_='carousel_item').find("a")['data-fancybox-href']
    full_url = f'https://www.jpl.nasa.gov{feat_img}'
    hemisphere_images_urls['image'] = full_url

    broswer.quit()

    browser = init_browser()
    twitter_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(twitter_url)
    
	time.sleep(1)
    url = 'https://twitter.com/marswxreport?lang=en'
    response = requests.get(url)
    soup = bs(response.text, 'lxml')
    tweet = soup.find('p', class_ = "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    final_dict['tweet'] = tweet

    browser.quit()

    facts_url = 'https://space-facts.com/mars/'
	tables = pd.read_html(url_facts)
	mars_facts = tables[0]
    mars_facts.to_html('mars_facts.html')
    final_dict['mars_fact'] = mars_facts.to_html()

    hem_dict = {}
	hem_titles = []
	hem_urls = []

	hem_text = soup.find_all('div', class_ = 'description')
	hem_text = soup.find_all('h3')
	for i in hem_text:
	    hem_titles.append(i.text)
	

	hem_url = soup.find_all('a', class_ = 'itemLink product-item', href=True)

	for j in hem_url:
	    hem_urls.append(j['href'])
	hem_urls

	hemi_url = 'https://astrogeology.usgs.gov/'
	images = []
	for i in hem_urls:
	    response = requests.get(f'{hemi_url}{i}')
	    soup = bs(response.text, 'lxml')
	    finder =  soup.find('img', class_ = 'wide-image')
	    full_url_img = f'{hemi_url}{finder["src"]}'
	    images.append(full_url_img)
	images

	hemisphere_urls = []

	y=0
	for x in hem_titles:
	    hem_dict = {'title': x, 'images_url': imgs[y]}
	    hemisphere_urls.append(hem_dict)
	    y=y+1
	    
	hemisphere_images_urls['hemisphere_urls'] = hemisphere_urls

	return hemisphere_urls
