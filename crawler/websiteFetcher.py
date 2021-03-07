import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from .crawledWebsite import CrawledWebsite

class WebsiteFetcher():
    def __init__(self):
        self.website_list = {}

    def fetch(self):
        url = input("Website die gecrawled werden soll: ")
        self.website_list[url] = CrawledWebsite(url)
        depth = 0
        while url != "" and depth < 10:

            print("checking: " + url)
            time.sleep(1)
            r = requests.get(url)
            doc = BeautifulSoup(r.text, "html.parser")
            link_list = []
            for a in doc.find_all("a"):
                if "href" in a.attrs:
                    link = a.get('href')
                    if link[0] == "/":
                        link = urljoin(url, link)
                    elif link[0] == "#":
                        continue
                    elif link[0] == "?":
                        continue
                    elif link.startswith("tel:"):
                        continue
                    elif link.startswith("mailto:"):
                        continue
                    link_list.append(link)
                    if link not in self.website_list:
                        self.website_list[link] = CrawledWebsite(link)
            self.website_list[url].set_link_list(link_list)
            yield link_list

            for website in self.website_list.keys():
                if self.website_list[website].iscrawled():
                    url = ""
                else:
                    url = website
                    depth = depth + 1
                    break
