import crawler

fetcher = crawler.WebsiteFetcher()
fetcher.add_website("https://www.whatsapp.com/download/")

for website in fetcher.fetch(3):
    for link in website:
        print(link)

