from bs4 import BeautifulSoup
import pprint
import requests
import json
import collections
import time
import re
pp = pprint.PrettyPrinter(indent=4)

all_my_data = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}

therapist_alpha = re.compile("[a-z]")
url = "https://www.psychologytoday.com/us/therapists/profile-listings/alabama/"
results_page = requests.get(url, headers=headers)
page_html = results_page.text
soup = BeautifulSoup(page_html, "html.parser")


all_labels = soup.find_all("div", attrs = {'id':'AZ'})
for a_div in all_labels:
    # print('------------')
    # print(a_div.text)

    alink = a_div.find('a')
    abs_url = alink['href']
    # print(abs_url)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }

    item_request = requests.get(abs_url, headers=headers)
    item_html = item_request.text
    item_soup = BeautifulSoup(item_html, "html.parser")
    # print(item_soup)
    all_prof = soup.find_all("div", attrs = {'class':'listing-profile'})
    for prof in all_prof:
        proflink =a_div.find('a')
        proflink

        address = item_soup.find("div", attrs = {'itemprop' : 'address'})
        # print(address)
        time.sleep(5)
        alabama_address = {}
        alabama_address["address"] = address.text
        alabama_address["url"] = abs_url
        all_my_data.append(alabama_address)
        json_file = open('alabama.json','w')
        json.dump(all_my_data,json_file, indent=2)
        json_file.close()
