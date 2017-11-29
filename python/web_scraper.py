"""
I built this for a prior project so you'll notice lots of placeholders
throughout,just swap in your desired inputs and you should be good.

The goal here is starting at a given URL, crawl and scrape the linked 
subpages to make a structure mapping a target object to elements that 
contain additional info about that object. When done, output the collected
data to a json file.
"""

import urllib.request
from bs4 import BeautifulSoup
import re
import json

start = 'http://<siteurl>'

# get the html from the main page, specify the user agent (sometimes necessary)
def url_to_soup(start):
    req = urllib.request.Request(start, headers={ 'User-Agent': 'Mozilla/5.0' })
    html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

# from the main page, locate all the links for the subpages
def get_subpage_reports(report):
    subpages = []
    for link in report.find_all(href=re.compile('/<subpage')):
        subpages.append(link.get('href'))
    return subpages

# take the list of sub-page links and scrape the desired data from each page
def gather_target_info(target):
    maps = {}
    for link in target:
        # grab the html for each target page
        current_link = url_to_soup(start + link)
        # separate the third element from the link
        main_element = link.split('/')[2]
        # get the third element content from the page, in this example it's rows
        for row in current_link.find_all('tr'):
            # since we have rows we now want to get the columns from the rows
            columns = row.find_all('td')
            # check that there is data present in all fields
            if len(columns) > 0:
                # remove the beginning letters from the targets
                present_target = re.findall(r'\d+', columns[0].string)[0]
                # grab the desired data from the column fields
                second_element = columns[1].string
                third_element = columns[3].string
                fourth_element = columns[5].string
                # add data to 'maps' dictionary, use target as key
                maps[present_target] = {'Main Element': main_element,
                                        'Second Element': second_element,
                                        'Third Element': third_element,
                                        'Fourth Element': fourth_element}
    return maps

# take the data from the 'maps' dictionary and write it to a file in json format
def generate_json(maps):
    with open('target_map_complete.txt', 'w') as output_file:
        json.dump(maps, output_file)

def __main__():
    # define the starting link
    top_page = url_to_soup(start + '</path/to/starting/point>')
    # grab the links to each subpage
    target_links = get_subpage_reports(top_page)
    # scrape each subpages to gather desired info
    mappings = gather_target_info(target_links)
    # write compiled dictionary contents to a json formatted file
    generate_json(mappings)

__main__()