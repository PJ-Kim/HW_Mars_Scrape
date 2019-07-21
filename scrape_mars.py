# # Mission to Mars
from bs4 import BeautifulSoup as bs
import requests
import os
import re
import pandas as pd
from splinter import Browser
import time
# Import Splinter and set the chromedriver path
def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()



# ## NASA MARS News
## NASA MARS News Visit the following URL
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
# Retrieve page with the requests module
#    response = requests.get(url)

    results = soup.select_one('li.slide')
    print(results)
# title - from first article
    title = results.find('div',class_='content_title').get_text()
    

# teaser - from first article
    teaser = results.find('div',class_='article_teaser_body').get_text()




# ## JPL Mars Space Images - Featured Image

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
# Retrieve page with the requests module
#    response = requests.get(url)


#results2 = soup.find(id)
#results2 = soup.find('body')
    big_part = soup.find('section', class_="centered_text clearfix main_feature primary_media_feature single")
    pic = big_part.article['style']
    featured = pic.split("'")
    half_img = 'https://www.jpl.nasa.gov/'
    almost = featured[1]
    final_img = half_img + almost
    

    



# ## Mars Weather

#Use Pandas to scrape Mars weather twitter site and decode the list
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
# Retrieve page with the requests module
#    response = requests.get(url)

#    zz = soup(text=re.compile(r'InSight sol'))
    for elem in soup(text=re.compile(r'InSight sol')):
        tweet_result = elem
#    tweet_result = soup.find('div', class_='js-tweet-text-container').find('p').get_text()

## Mars Facts
# Use Pandas to scrape table on Mars Facts
    url = 'https://space-facts.com/mars/'

# Use Panda's `read_html` to parse the url
    tables = pd.read_html(url)

# Isolate date on Mars
    mars_df = tables[1]
    mars_df.columns = ['Facts', 'Data']
 
# Drop df index column
    mars_df.set_index('Facts', inplace = True)
# Standardize header row
    mars_df.columns.name = mars_df.index.name
    mars_df.index.name = None

#for Facts in marsfacts:
    mars_tbl = mars_df.to_html()


## Mars Hemispheres
#   BS soup, splinter, and chromepath drivers
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    links = browser.find_by_css("a.product-item h3")
    
#   Hemisphere list containing the 4 seperate dictionaries    
    hemisphere_image_urls = []
    del hemisphere_image_urls [:]


    for i in range(len(links)):
        browser.find_by_css("a.product-item h3")[i].click()
        html = browser.html
        soup = bs(html, 'html.parser')    
        hemi_link = soup.find('a', {'target': '_blank', 'href': True}).get('href')
        result2 = soup.find('h2',class_= 'title')
        titles = result2.text
        thisdict = {"title": titles, "img_url": hemi_link}
        hemisphere_image_urls.append(dict(thisdict))
        hemi_link 
        browser.back()

# main dictionary to return to the app.py
    mars_dict = {
        "news_title": title,
        "news_teaser": teaser,
        "featured_image": final_img,
        "weather_tweet": tweet_result,
        "facts": mars_tbl,
        "hemis" : hemisphere_image_urls
    }
   
    browser.quit

    return mars_dict



