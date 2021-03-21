import crawler
import pickle
import os
import zlib

sites = set()
sites.add("https://bytewerk.org")
sites.add("https://blog.bytewerk.org")
sites.add("https://stats.bytewerk.org")
sites.add("https://gaestehausleeste.de")
sites.add("https://k-tronik.de")
sites.add("https://k-tronik.digital")
sites.add("https://mantis.zettacloud.de")
sites.add("https://toyako.de")
sites.add("https://wttr.in")

while len(sites) != 0:
    site = sites.pop()
    fetcher = crawler.WebsiteFetcher(site, wait_time_max=10)
    for website in fetcher.fetch(10):
        for link in website:
            print(link)
    filename = zlib.crc32(bytearray(site, encoding="utf-8"))
    with open(os.path.join("data", str(filename)), "wb") as output_file:
        pickle.dump(fetcher, output_file)

