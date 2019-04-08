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
url_list = ["https://www.psychologytoday.com/us/therapists/profile-listings/alabama/a", "https://www.psychologytoday.com/us/therapists/profile-listings/alabama/b", "https://www.psychologytoday.com/us/therapists/profile-listings/alabama/c", "https://www.psychologytoday.com/us/therapists/profile-listings/alabama/d", "https://www.psychologytoday.com/us/therapists/profile-listings/alabama/e", "https://www.psychologytoday.com/us/therapists/profile-listings/alabama/f", "https://www.psychologytoday.com/us/therapists/profile-listings/alabama/g", "https://www.psychologytoday.com/us/therapists/profile-listings/alabama/h", "https://www.psychologytoday.com/us/therapists/profile-listings/alabama/i", "https://www.psychologytoday.com/us/therapists/profile-listings/alabama/j", "https://www.psychologytoday.com/us/therapists/profile-listings/alabama/k", "https://www.psychologytoday.com/us/therapists/profile-listings/alabama/l", "https://www.psychologytoday.com/us/therapists/profile-listings/alabama/m", "https://www.psychologytoday.com/us/therapists/profile-listings/alabama/n", "https://www.psychologytoday.com/us/therapists/profile-listings/alabama/o", "https://www.psychologytoday.com/us/therapists/profile-listings/alabama/p", "https://www.psychologytoday.com/us/therapists/profile-listings/alabama/q", "https://www.psychologytoday.com/us/therapists/profile-listings/alabama/r", "https://www.psychologytoday.com/us/therapists/profile-listings/alabama/s", "https://www.psychologytoday.com/us/therapists/profile-listings/alabama/t", "https://www.psychologytoday.com/us/therapists/profile-listings/alabama/u", "https://www.psychologytoday.com/us/therapists/profile-listings/alabama/v", "https://www.psychologytoday.com/us/therapists/profile-listings/alabama/w", "https://www.psychologytoday.com/us/therapists/profile-listings/alabama/y", "https://www.psychologytoday.com/us/therapists/profile-listings/alabama/z"]
results_page = requests.get(url, headers=headers)
page_html = results_page.text
soup = BeautifulSoup(page_html, "html.parser")


all_listings = soup.find_all("div", attrs = {'class':'prof-listing'})
#pull all a tags out of the alphabetical list of therapists
for a_div in all_listings:
    alink = a_div.find('a')
    abs_url = alink['href']


    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }

    item_request = requests.get(abs_url, headers=headers)
    item_html = item_request.text
    item_soup = BeautifulSoup(item_html, "html.parser")

    #pull all listing profiles in a letter category
    all_prof = item_soup.find_all("div", attrs = {'class':'col-9 col-sm-9 col-md-10 col-lg-10 col-xl-10 col-tight-left'})

    for prof in all_prof:
        proflink = prof.find('a')
        profurl = proflink['href']

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
        }
        prof_request = requests.get(profurl, headers=headers)
        prof_html = prof_request.text
        prof_soup = BeautifulSoup(prof_html, "html.parser")

        address = prof_soup.find("div", attrs = {'itemprop' : 'address'})
        time.sleep(5)
        alabama_address = {}
        alabama_address["address"] = address.text
        alabama_address["url"] = profurl
        all_my_data.append(alabama_address)
        json_file = open('alabama.json','w')
        json.dump(all_my_data,json_file, indent=2)
        json_file.close()
