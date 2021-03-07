import crawler

fetcher = crawler.WebsiteFetcher()

for website in fetcher.fetch():
    for link in website:
        print(link)