import crawler

fetcher = crawler.WebsiteFetcher()
fetcher.add_website("https://www.bytewerk.org/")

for website in fetcher.fetch(10):
    for link in website:
        print(link)

