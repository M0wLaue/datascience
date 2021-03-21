import crawler
import pickle

fetcher = crawler.WebsiteFetcher(wait_time_max=1)  # pylint: disable=no-member
fetcher.add_website("https://bytewerk.org")
fetcher.add_website("https://blog.bytewerk.org")
fetcher.add_website("https://stats.bytewerk.org")
fetcher.add_website("https://gaestehausleeste.de")
fetcher.add_website("https://k-tronik.de")
fetcher.add_website("https://k-tronik.digital")

for website in fetcher.fetch(10):
    for link in website:
        print(link)

with open("fetcher.data", "wb") as output_file:
    pickle.dump(fetcher, output_file)


