import time
import random
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from .crawledWebsite import CrawledWebsite

class WebsiteFetcher():
    def __init__(self, url, wait_time_max = 10):
        self.website_list = {}
        self.add_website(url)
        self.wait_time_max = wait_time_max
        random.seed()

    def add_website(self, url, depth=0):
        self.website_list[url] = CrawledWebsite(url, depth)

    def get_next_website(self):
        for website in self.website_list.keys():
            if self.website_list[website].iscrawled():
                url = ""
            else:
                url = website
                break
        return url

    def fetch(self, crawl_depth):
        url = self.get_next_website()
        depth = 0
        while url != "" and depth < crawl_depth:

            print("checking: " + url)
            time.sleep(random.randrange(self.wait_time_max))
            depth = self.website_list[url].depth
            r = requests.get(url)
            doc = BeautifulSoup(r.text, "html.parser")
            link_list = set()
            for a in doc.find_all("a"):
                if "href" in a.attrs:
                    link = a.get('href').rstrip("/")
                    if link == "":
                        continue
                    elif link[0] == "/":
                        link = urljoin(url, link)
                    elif link[0] == "#":
                        continue
                    elif link[0] == "?":
                        continue
                    elif link.startswith("tel:"):
                        continue
                    elif link.startswith("mailto:"):
                        self.website_list[url].add_mail(link)
                        continue
                    elif link.startswith("javascript:"):
                        continue
                    elif link.startswith("{"):
                        continue

                    link_list.add(link)
                    if link not in self.website_list and link.startswith(url):
                        self.add_website(link, depth + 1)
            self.website_list[url].set_link_list(link_list)
            self.website_list[url].set_external_link_list(link_list)
            self.website_list[url].finish_crawling()
            yield link_list

            url = self.get_next_website()

